from flask import render_template, request
from app import app
from operator_aware_lib.handler_in_str_to_out_str import handler_in_str_to_out_str
from operator_aware_lib.check_passphrase import check_passphrase
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/pentest.html")
@app.route("/pentest")
def pentest():
    return render_template('pentest.html')


@app.route("/", methods=["POST"])
@app.route("/index", methods=["POST"])
def indexpost():
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

        # Check which option selected from dropdown
        what_to_load = request.form['dropdown_selection']

        if what_to_load == 'upload_call_option':
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

                results_printout = handler_in_str_to_out_str(audio_file_name_w_extension=filename,
                                                             audio_folder_path=target,
                                                             transcription_directory_path='auto', qVerbose=1,
                                                             str_dict_version='newest')

                call_list.append({
                    'base_filename': str(upload.filename),
                    'net_results': results_printout
                })

        else:
            results_printout = handler_in_str_to_out_str(audio_file_name_w_extension=what_to_load,
                                                         audio_folder_path=os.path.join(target, '..',
                                                                                        'demo_audio_files'),
                                                         transcription_directory_path='auto', qVerbose=1,
                                                         str_dict_version='newest', demo_mode=1)
            call_list.append({
                'base_filename': str(what_to_load),
                'net_results': results_printout
            })

        # Return the result
        # Change this to an output template
        return render_template('output.html', calls=call_list)
