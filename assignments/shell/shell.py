import y33ters as yt
import os

if __name__ == "__main__":
    
    #dictionary that links command names with their respective functions
    commandDic = { 
        'cat': yt.cat,
        'cd': yt.cd,
        'cp': yt.cp,
        'grep': yt.grep,
        'head': yt.head,
        'less': yt.less,
        'ls': yt.ls,
        'mkdir': yt.mkdir,
        'mv': yt.mv,
        'pwd': yt.pwd,
        'rm': yt.rm,
        'rmdir': yt.rmdir,
        'sort': yt.sort,
        'tail': yt.tail,
        'wc': yt.wc,
        'who': yt.who
    }
    #splits up the arguments read in from the command line into their respective categories
    argsDic = {"Command": [], "Params": [], "Flags": [], "Output":[]}
    #list that holds all the commands input
    history = []

    loop = True


    while(loop):
        #prints the current working directory in cyan 
        print("\033[1;36;40m" + os.getcwd())
        cmd = input("\033[1;37;40m >> ")

        #append cmd to list if it's not a call to print the history
        if cmd != "history":
            history.append(cmd)
        #turns the string in to a list of words that made up the string
        cmd = cmd.split()

        #REEE = Exit the shell
        if cmd[0] == "exit":
            loop = False
        #print history
        elif cmd[0] == "history":
            x = int(0)
            for line in history:
                print(str(x) + ": " + line)
                x += 1
        #change permissions
        elif cmd[0] == "chmod":
            try:
                os.chmod(cmd[2], '0o'+str(cmd[1]))
            except:
                print("ERROR: Something wrong with chmod or file name")
        #Else we got a command to run boys        
        else:
            #checks for the !x command
            if cmd[0][0] == '!':
                try:
                    cmd = history[int(cmd[0][1])]
                    cmd = cmd.split()
                except:
                    print("ERROR:" + cmd[0][1] + "th command in history not found")
            #cycles through the list of words and puts them in their respective lists in the argsDic dictionary
            for arg in cmd:
                if arg in commandDic:
                    argsDic["Command"].append(arg)
                elif arg[0] == '-' or arg == '*':
                    argsDic["Flags"].append(arg)
                #if the user wants to pipe the stuff to an outfile
                elif arg == '>' or arg == '>>':
                    try:
                        argsDic["Output"].append(cmd[cmd.index(arg) + 1])
                    except:
                        print("Something went wrong brother.")
                #Else it's a parameter
                else:
                    if arg not in argsDic["Output"] or arg != "|":
                        argsDic["Params"].append(arg)
            #run all of the commands entered
            for command in argsDic["Command"]:
                try:
                    commandDic[command](argsDic["Command"], argsDic["Flags"], argsDic["Params"], argsDic["Output"])
                except:
                    print("ERROR:" + command + " not a valid command")
            #If the command entered isn't valid
            if not argsDic["Command"]:
                print("ERROR: " + cmd[0] + " Command not found")


        #clear argsDic and cmd
        for k in argsDic:
            argsDic[k] = []

        cmd = []

