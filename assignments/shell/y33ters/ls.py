import os
import sys
from os import stat
from datetime import datetime

path = '.'



def ls(command, flags, params, output):

    # stores all the files/directors
    files = os.listdir(path)

    #dictionary for rwx output
    permission ={
        0:('---'),
        1:('--x'),
        2:('-w-'),
        3:('-wx'),
        4:('r--'),
        5:('r-x'),
        6:('rw-'),
        7:('rwx')
        }

    if not output:
        for file in files:
            if not flags:
                if not file.startswith('.'):
                    print(file)
            else:
                info = os.lstat(file) # info for current file
                octalPerms = oct(info.st_mode)[-3:] # permissions
                octalPerms = int(octalPerms) #convert the permissions to an int
                one = octalPerms % 10 #third digit
                octalPerms = octalPerms // 10
                ten = octalPerms % 10 #second digit
                octalPerms = octalPerms // 10 #first digit
                time = info.st_mtime 
                name = stat(file).st_uid
                group = stat(file).st_gid
                for f in flags:
                    if f == '-la': #long listing with hidden files
                        print(permission[one] + permission[ten] + permission[octalPerms], end =" ")
                        print('@' + str(info.st_nlink), end =" ")
                        #print(name, end = " ")
                        #print(group, end = " ")
                        size = info.st_size #size of file
                        print(size, end =" ")
                        print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'), end =" ") #print the time
                        print(file)
                    elif f == '-a':
                        print(file)
                    elif f == '-l':
                        if not file.startswith('.'):
                            print(permission[one] + permission[ten] + permission[octalPerms], end =" ")
                            print('@' + str(info.st_nlink), end =" ")
                            #print(name, end = " ")
                            #print(group, end = " ")
                            size = info.st_size
                            print(size, end =" ")
                            print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'), end =" ")
                            print(file)
                    elif f == '-lh': #human readable
                        if not file.startswith('.'):
                            print(permission[one] + permission[ten] + permission[octalPerms], end =" ")
                            print('@' + str(info.st_nlink), end =" ")
                            #print(name, end = " ")
                            #print(group, end = " ")
                            size = info.st_size
                            for unit in ['bytes', 'MB', 'KB', 'GB']: #check for size unit
                                if size < 1024:
                                    hr_size = str(size) + unit
                                    break
                                else:
                                    size /= 1024
                            print(hr_size, end =" ")
                            print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'), end =" ")
                            print(file)
                    elif f == '-lah':
                        print(permission[one] + permission[ten] + permission[octalPerms], end =" ")
                        print('@' + str(info.st_nlink), end =" ")
                        #print(name, end = " ")
                        #print(group, end = " ")
                        size = info.st_size
                        for unit in ['bytes', 'MB', 'KB', 'GB']: #check for size unit
                            if size < 1024:
                                hr_size = str(size) + unit
                                break
                            else:
                                size /= 1024
                        print(hr_size, end =" ")
                        print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'), end =" ")
                        print(file)
    else:
        with open(output[0], 'w') as outfile:
            for file in files:
                outfile.write(file)
    return 



