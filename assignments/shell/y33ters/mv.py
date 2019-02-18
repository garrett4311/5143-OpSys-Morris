from shutil import move

def mv(command, flags, params, output):
    try:
        move(params[0], params[1])

    except IOError:
        print("Destination location (" + pararms[1] + ") is not writable")
    return