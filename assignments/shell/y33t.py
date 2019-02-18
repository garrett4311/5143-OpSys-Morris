import y33ters as yt
import os

if __name__ == "__main__":
    
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
    
    argsDic = {"Command": [], "Params": [], "Flags": [], "Output":[]}
    history = []

    loop = True


    while(loop):
        print("\033[1;36;40m" + os.getcwd())
        cmd = input("\033[1;37;40m >> ")
        if cmd != "history":
            history.append(cmd)

        cmd = cmd.split()

        if cmd[0] == "REEE":
            loop = False
        elif cmd[0] == "history":
            x = int(0)
            for line in history:
                print(str(x) + ": " + line)
                x += 1
        elif cmd[0] == "chmod":
            try:
                os.chmod(cmd[2], '0o'+cmd[1])
            except:
                print("ERROR: Something wrong with chmod or file name")
        else:
            if cmd[0][0] == '!':
                try:
                    cmd = history[int(cmd[0][1])]
                    cmd = cmd.split()
                except:
                    print("ERROR:" + cmd[0][1] + "th command in history not found")

            for arg in cmd:
                if arg in commandDic:
                    argsDic["Command"].append(arg)
                elif arg[0] == '-' or arg == '*':
                    argsDic["Flags"].append(arg)
                elif arg == '>' or arg == '>>':
                    try:
                        argsDic["Output"].append(cmd[cmd.index(arg) + 1])
                    except:
                        print("Something went wrong brother.")
                else:
                    if arg not in argsDic["Output"] or arg != "|":
                        argsDic["Params"].append(arg)

            for command in argsDic["Command"]:
                try:
                    commandDic[command](argsDic["Command"], argsDic["Flags"], argsDic["Params"], argsDic["Output"])
                except:
                    print("ERROR:" + command + " not a valid command")

            if not argsDic["Command"]:
                print("ERROR: " + cmd[0] + " Command not found")



        for k in argsDic:
            argsDic[k] = []

        cmd = []

