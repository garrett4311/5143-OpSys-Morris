import os

def tail(command, flags, params, output):
    with open(params[0]) as treasure:
        treasure = treasure.readlines()
        i = len(treasure) - int(params[1])
        while i != len(treasure):
            print(treasure[i])
            i = i + 1
    return