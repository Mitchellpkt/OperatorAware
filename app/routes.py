from flask import render_template, request
from app import app
from operator_aware_lib.handler_in_str_to_out_str import handler_in_str_to_out_str
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
@app.route("/index", methods=["POST"])
def upload():
    # Generate and create target path for audio file (static)
    target = os.path.join(APP_ROOT,'static/')
    # print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Coludn't create upload directory: {}".format(target))

    # Check the password
    password_file = open('SupervisorPassword.txt', 'r')
    pswd_read = password_file.readlines(0)
    pswd_from_file = pswd_read[0].rstrip()
    password_file.close()
    # print('#####################################################')
    # print('{} is the supervisor password '.format(pswd_from_file))
    # from pprint import pprint # for troubleshooting
    # pprint(vars(request)) # for troubleshooting
    pswd_from_user = request.form['password']
    # print('{} is the user-given password'.format(pswd_from_user))

    if pswd_from_user == pswd_from_file:
        print('Password accepted')
    else:
        return('Wrong supervisor password')

    # LOOP OVER UPLOADED FILES
    net_results_printout = ''
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

    # for upload in request.files.getlist("file"):
    #     print(upload)
    #     print("{} is the file name".format(upload.filename))
    #     filename = upload.filename
    #     # This is to verify files are supported
    #     ext = os.path.splitext(filename)[1]
    #     if (ext == ".jpg") or (ext == ".png"):
    #         print("File supported moving on...")
    #     else:
    #         render_template("Error.html", message="Files uploaded are not supported...")
    #     destination = "/".join([target, filename])
    #     print("Accept incoming file:", filename)
    #     print("Save it to:", destination)
    #     upload.save(destination)
    #
    # # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("complete.html", image_name=filename)

