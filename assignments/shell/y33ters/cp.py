from shutil import copyfile

# copy file to new file
def cp(command, flags, params, output):
    try:
        copyfile(params[0], params[1]) 
    except IOError:
        print("Destination location (" + params[0] + ") is not writable")
    return