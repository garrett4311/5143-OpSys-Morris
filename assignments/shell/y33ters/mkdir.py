import os

#create a new directory
def mkdir(command, flags, params, output):
    try:
        os.mkdir(params[0])
    except OSError:
        print("Cannot create " + params[0] + " directory")
    return