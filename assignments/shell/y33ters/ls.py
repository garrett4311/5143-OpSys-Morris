import os
import sys
from os import stat
#from pwd import getpwuid
#from grp import getgrgid
from datetime import datetime
path = '.'



def ls(command, flags, params, output):

    files = os.listdir(path)

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
            #isLink = os.path.islink(file)
            #isDir = os.path.isdir(file)
            if not flags:
                print(file)
            else:
                info = os.lstat(file)
                #if not isLink and not isDir:
                #isFile = True
                octalPerms = oct(info.st_mode)[-3:]
                octalPerms = int(octalPerms)
                one = octalPerms % 10
                octalPerms = octalPerms // 10
                ten = octalPerms % 10
                octalPerms = octalPerms // 10
                time = info.st_mtime
                name = stat(file).st_uid
                group = stat(file).st_gid
                for f in flags:
                    if f == '-l':
                        print(permission[one] + permission[ten] + permission[octalPerms], end =" ")
                        print('@' + str(info.st_nlink), end =" ")
                        #print(name, end = " ")
                        #print(group, end = " ")
                        size = info.st_size
                        print(size, end =" ")
                        print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'), end =" ")
                        print(file)
                    elif f == '-h':
                        print(permission[one] + permission[ten] + permission[octalPerms], end =" ")
                        print('@' + str(info.st_nlink), end =" ")
                        #print(name, end = " ")
                        #print(group, end = " ")
                        size = info.st_size
                        for unit in ['bytes', 'MB', 'KB', 'GB']:
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



