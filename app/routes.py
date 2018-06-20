from flask import render_template, request
from app import app
from operator_aware_lib.handler_in_str_to_out_str import handler_in_str_to_out_str
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])

# def dummmy():
#     x = request.form['Item_1']
#     OA_eval = handler_in_str_to_out_str(x)
#     return OA_eval

@app.route("/", methods=["POST"])
@app.route("/index", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT,'static/')

    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Coludn't create upload directory: {}".format(target))

    pswd = request.files.getlist("passwordInput")
    print('{} is the password'.format(pswd))
    #if password == "Insight2018":
    #    print('alright')
    #else:
    #    print('Incorrect password')
    #    kill function before upload

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

