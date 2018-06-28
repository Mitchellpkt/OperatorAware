from flask import render_template, request
from app import app
from operator_aware_lib.handler_in_str_to_out_str import handler_in_str_to_out_str
from operator_aware_lib.check_passphrase import check_passphrase
import time
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/pentest')
def pentest():
    print('route through pentest')
    return render_template('pentest.html')

@app.route('/')
@app.route('/index')
def index():
    print('route through index alone')
    return render_template('index.html')

@app.route('/', methods=["POST"])
@app.route('/index', methods=["POST"])
def indexpost(confidence_threshold=0.6):
    print('route through index post')

    # Generate and create target path for audio file (uploads)
    target = os.path.join(APP_ROOT, 'uploads/')
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    # Check the password
    pswd_from_user = request.form['password']
    authenticated = check_passphrase(pswd_from_user, passphrase_file_path='supervisor_passphrases.keys')

    if authenticated == 0:
        return render_template('wrong_passphrase.html')

    else:
        # Continue ahead
        net_results_printout = ''  # init
        call_list = list()

        # LOOP OVER UPLOADED FILES
        print(request.files.getlist("file"))
        for upload in request.files.getlist("file"):
            print(upload)

            filename = upload.filename
            print("{} is the filename".format(filename))

            destination = "/".join([target, filename])
            print("Accepted incoming file: ", filename)

            upload.save(destination)
            print("Saved it to: ", destination)

            results_printout, audio_length_s, confidence_metric, words_list, categories_list, is_urgent = handler_in_str_to_out_str(
                audio_file_name_w_extension=filename,
                audio_folder_path=os.path.join(target),
                transcription_directory_path='auto', qVerbose=1,
                str_dict_version='newest', demo_mode=1)

            min_conf = float(min(confidence_metric))
            min_conf_prct_str = str(round(min_conf * 100))
            print('min_conf is type: ' + str(type(min_conf)))
            print('confidence_threshold is type: ' + str(type(confidence_threshold)))
            if min_conf < confidence_threshold:
                confidence_warning = ' [Warning: low transcription confidence: ' + min_conf_prct_str + '%]'
            else:
                confidence_warning = ''  # Acceptable audio quality, transcription minimum confidence = ' + min_conf_prct_str + '%'

            call_list.append({
                'base_filename': str(upload.filename),
                'net_results': results_printout,
                'call_duration': time.strftime('%H:%M:%S', time.gmtime(audio_length_s)),
                'confidence_warning': confidence_warning,
                'audio_file_path': filename,
                'words_list': words_list,
                'categories_list': categories_list,
                'is_urgent': is_urgent
            })

        # Return the result
        # Change this to an output template
        return render_template('output.html', calls=call_list)
