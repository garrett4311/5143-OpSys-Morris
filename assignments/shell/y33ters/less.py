import os
# display a file or file(s)
def less(command, flags, params, output):
        if not output:
                for f in params: 
                        with open(f) as treasure:
                                for line in treasure:
                                        print(line) 
        else:
                with open(output[0], "w") as outfile:
                        for f in params:
                                with open(f) as treasure:
                                        for line in treasure:
                                                outfile.write(line)

        return