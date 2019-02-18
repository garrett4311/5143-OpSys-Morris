import os


def pwd(command, flags, params, output):
    if not output:
        print(os.getcwd())
    else:
        with open(output[0], 'w') as outfile:
            outfile.write(os.getcwd())
    return