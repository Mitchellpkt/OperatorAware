from flask import render_template, request
from app import app
from operator_aware_lib.handler_in_str_to_out_str import handler_in_str_to_out_str
from operator_aware_lib.check_password import check_password
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

    # Generate and create target path for audio file (static)
    target = os.path.join(APP_ROOT,'static/')
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Coludn't create upload directory: {}".format(target))

    # Check the password
    pswd_from_user = request.form['password']
    authenticated = check_password(pswd_from_user, password_file_path='SupervisorPassword.txt')

    if authenticated==0:
        print("FAILED AUTHORIZATION ATTEMPT - PASSWORD:" + pswd_from_user)
        return("WRONG SUPERVISOR PASWORD. <br>Contact mitchellpkt to request access")
    else:
        # Continue ahead
        net_results_printout = '' # init

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

                results_printout = handler_in_str_to_out_str(audio_file_name_w_extension=filename, audio_folder_path=target,
                                          transcription_directory_path='auto', qVerbose=1, str_dict_version='newest')

                net_results_printout += '****************************<br>'
                net_results_printout += 'In file ' + filename + ':<br>'
                net_results_printout += results_printout + "<br><br>"

            return(net_results_printout)

        else:
            results_printout = handler_in_str_to_out_str(audio_file_name_w_extension=what_to_load+'.FLAC', audio_folder_path=target,
                                                         transcription_directory_path='auto', qVerbose=1,
                                                         str_dict_version='newest')

            net_results_printout += '****************************<br>'
            net_results_printout += 'In file ' + what_to_load + ':<br>'
            net_results_printout += results_printout + "<br><br>"

            return(net_results_printout)