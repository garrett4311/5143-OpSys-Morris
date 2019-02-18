import os


def rmdir (command, flags, params, output):
    try:
        os.rmdir(params[0])
    except OSError:
        print("The directory" + params[0] + "is not empty.")
    return