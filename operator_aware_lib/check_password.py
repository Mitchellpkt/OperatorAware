# check_password()
# Input string to be verified (pswd_from_user)
# Optional, specify password_file_path

def check_password(pswd_from_user, password_file_path='SupervisorPassword.txt'):
    password_file = open(password_file_path, 'r')
    pswd_read = password_file.readlines(0)
    pswd_from_file = pswd_read[0].rstrip()
    password_file.close()

    if pswd_from_user == pswd_from_file:
        print('Password accepted')
        return 1
    else:
        print('Wrong supervisor password')
        return 0


