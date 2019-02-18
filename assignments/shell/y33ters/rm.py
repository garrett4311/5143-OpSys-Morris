import os

def rm (command, flags, params, output):
    if not flags:
        if os.path.exists(params[0]):
            try:
                os.remove(params[0])
            except OSError:
                print("Could not remove file(s)")
        else:
            print("This file does not exist")
    else:
        if flags[0] == "-r":
            #code taken from: https://stackoverflow.com/questions/13118029/deleting-the-folders-in-python-recursively
            for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown=False):
                try:
                    os.rmdir(dirpath)
                except OSError as ex:
                    print(ex)

        else:
            print("Flag not valid")
    return