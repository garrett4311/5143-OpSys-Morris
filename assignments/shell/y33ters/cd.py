import os
#change directory
def cd(command, flags, params, output):
    if len(params) == 1:
        if params[0] == '~':
            os.chdir(os.path.expanduser('~'))
        elif params[0] == '..':
            os.chdir('..')
        elif params[0] == '.':
            os.chdir('.')
        else:
            try:
                os.chdir('./' + params[0])
            except OSError:
                print("ERROR: " + params[0] + " directory not found" )
    elif len(params) > 1:
        print("ERROR: cd takes 0-1 arguments (cd, cd *directoryName*, cd ~, cd ..")
    else:
        os.chdir(os.path.expanduser('~'))


    return