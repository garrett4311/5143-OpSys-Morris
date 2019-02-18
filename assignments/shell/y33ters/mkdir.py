import os

def mkdir(command, flags, params, output):
    try:
        os.mkdir(params[0])
    except OSError:
        print("Cannot create " + name + " directory")
    return