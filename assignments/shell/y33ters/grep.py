import os
import re

def grep(command, flags, params, output):
    with open(params[0]) as treasure:
        x = int(0)
        for line in treasure:
            if params[1] in line:
                print("Line " + str(x) + ": " + line)
            x+=1    
                
    return