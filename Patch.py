import os
cotList = [
    "<none>",
    "Guest",
    "Shared",
    "Desktop",
    "Download",
    "Applications"
]
cotEnd = [
    ".app"
]
def run_sh(op):
    return os.popen(op).read().split()
def clear():
    os.system("clear")
usrName = run_sh("id -un")[0]
usrDir = "/Users/" + usrName
flag=0

def check_end(file):
    end = ""
    for txt in range(len(file) - 1, -1 - 1):
        end = file[txt] + end
        if file[txt] == ".":
            break
    if end in cotEnd:
        return True
    return False
def find_file(startdir, findname, kind):
    try:
        crtList = os.listdir(startdir)
    except:
        return False
    i = 1
    for name in crtList:
        if kind=="file":
            if name == findname and os.path.isfile(os.path.join(startdir, name)):
                return True
        else:
            if name == findname and os.path.isdir(os.path.join(startdir, name)):
                return True
        if check_end(name) or (name in cotList):
            continue
        if os.path.isdir(os.path.join(startdir, name)):
            if name in cotList or name[len(name) - 1]:
                continue
            find_file(os.path.join(startdir, name), findname, kind)
        i += 1
    return False


########## Main Def ##########

########## 检查Motrix ##########
def main_check_motrix():
    clear()
    if not find_file("/Applications", "Motrix.app", "folder"):
        print("监测到未安装 Motrix, 是否安装")
        op = input("[Y/n] ")
        if op == "Y" or op == "y":
            print("请手动安装")
            os.system("open 'https://motrix.app/zh-CN/'")
        elif op == "n" or op == "N":
            print("请自行安装")
        else:
            print("操作不合法!")
            main_check_motrix()
        print("自行安装完毕后请按回车继续...")
        check = input()

########## Aria2下载 ##########
def main_download_aria2():
    global flag
    clear()
    if not find_file("/Users/" + usrName, "aria2", "folder"):
        print("未发现Aria2源码（注意！你如果是自己下载，文件夹应放在用户目录, 如/Users/xxx，且文件夹名为aria2），是否一键操作（下载）")
        op = input("[Y/n] ")
        if op == "Y" or op == "y":
            print("正在下载...")
            os.system("cd "+usrDir)
            os.system("git clone git://github.com/aria2/aria2.git")
            print("下载完毕!")
        elif op == "n" or op == "N":
            print("请手动下载（请将解压后的文件夹放在用户目录, 如 /Users/xxx 下, 如果文件夹名不是aria2请改为aria2）")
            os.system("open 'https://github.com/aria2/aria2'")
            print("自行下载完毕源码后请按回车继续...")
            check = input()
        else:
            print("操作不合法!")
            main_download_aria2()
        print("下载完成后请运行 python3 " + usrDir + "/aria2/Patch.py")
        os.system("cp Patch.py " + usrDir + "/aria2")
        check = input("点击回车以退出")
        flag = 1
    else:
        if find_file("/Users/" + usrName+"/aria2", "Patch.py", "file"):
            flag=0
            return
        print("发现Aria2源码，是否一键操作（删除并下载最新）")
        op = input("[Y/n] ")
        if op == "Y" or op == "y":
            print("正在删除...")
            os.system("rm -rf " + "'" + usrDir + "/aria2'")
            print("删除完成")
            print("正在下载...")
            os.system("git clone git://github.com/aria2/aria2.git")
            print("下载完毕!")
        elif op == "n" or op == "N":
            print("是否手动删除并下载最新源码（或者你不想也行）")
            op2 = input("[Y/n] ")
            if op2 == "Y" or op2 == "y":
                print("（请将解压后的文件夹放在用户目录, 如 /Users/xxx 下, 如果文件夹名不是aria2请改为aria2）")
                os.system("open 'https://github.com/aria2/aria2'")
                print("自行下载完毕源码后请按回车继续...")
                check = input()
            if op2 == "N" or op2 == "n":
                print("进行下一步操作")
            else:
                print("操作不合法!")
                main_download_aria2()
        else:
            print("操作不合法!")
            main_download_aria2()
        print("下载完成后请运行 python3 " + usrDir + "/aria2/Patch.py")
        os.system("cp Patch.py "+usrDir+"/aria2")
        check=input("点击回车以退出")
        flag=1

########## 突破限制 ##########
def main_patch_aria2():
    clear()
    print("修改文件...")
    with open(usrDir+"/aria2/src/OptionHandlerFactory.cc","r") as f:
        lines=f.readlines()
    os.system("rm -rf "+usrDir+"/aria2/src/OptionHandlerFactory.cc")
    with open(usrDir+"/aria2/src/OptionHandlerFactory.cc", 'w') as f:
        for i in range(len(lines)):
            if lines[i] == '''                                              "1", 1, 16, 'x'));\n''':
                   f.write('''                                              "256", 1, -1, 'x'));\n''')
            elif lines[i] == '''        PREF_MIN_SPLIT_SIZE, TEXT_MIN_SPLIT_SIZE, "20M", 1_m, 1_g, 'k'));\n''':
                     f.write('''        PREF_MIN_SPLIT_SIZE, TEXT_MIN_SPLIT_SIZE, "4K", 1_k, 1_g, 'k'));\n''')
            elif lines[i] == '''        PREF_CONNECT_TIMEOUT, TEXT_CONNECT_TIMEOUT, "60", 1, 600));\n''':
                     f.write('''        PREF_CONNECT_TIMEOUT, TEXT_CONNECT_TIMEOUT, "30", 1, 600));\n''')
            elif lines[i] == '''        PREF_PIECE_LENGTH, TEXT_PIECE_LENGTH, "1M", 1_m, 1_g));\n''':
                     f.write('''        PREF_PIECE_LENGTH, TEXT_PIECE_LENGTH, "4k", 1_k, 1_g));\n''')
            elif lines[i] == '''        new NumberOptionHandler(PREF_RETRY_WAIT, TEXT_RETRY_WAIT, "0", 0, 600));\n''':
                     f.write('''        new NumberOptionHandler(PREF_RETRY_WAIT, TEXT_RETRY_WAIT, "2", 0, 600));\n''')
            elif lines[i] == '''        new NumberOptionHandler(PREF_SPLIT, TEXT_SPLIT, "5", 1, -1, 's'));\n''':
                     f.write('''        new NumberOptionHandler(PREF_SPLIT, TEXT_SPLIT, "8", 1, -1, 's'));\n''')
            else:
                f.write(lines[i])
    print("文件修改完成")

########## 编译Aria2 ##########
def main_build_aria2():
    clear()
    print("安装依赖包, 设置环境变量...")
    os.system("brew install autoconf automake libtool gettext pkg-config")
    os.system('''export PATH="/usr/local/opt/gettext/bin:$PATH"''')
    print("完成")
    print("编译...")
    os.system("cd "+usrDir+"/aria2")
    os.system("autoreconf -i")
    os.system('''ARIA2_STATIC=yes CXXFLAGS="-O2 -std=c++14" ./configure''')
    os.system("make")
    print("完成")
    print("请按回车继续...")
    check = input()

########## 替换Motrix Aria2 ##########
def main_change_aria2():
    clear()
    print("是否一键替换Motrix的Aria2")
    op = input("[Y/n] ")
    if op == "Y" or op == "y":
        print("正在替换...")
        os.system("rm -rf /Applications/Motrix.app/Contents/Resources/engine/aria2c")
        os.system("cp -R "+usrDir+"/aria2/src/aria2c /Applications/Motrix.app/Contents/Resources/engine")
        print("完毕!")
    elif op == "n" or op == "N":
        print("请手动替换")
        print("可以参考: https://github.com/agalwood/Motrix/issues/325")
        print("自行替换完毕后请按回车继续...")
        check = input()
    else:
        print("操作不合法!")
        main_change_aria2()

########## 替换Motrix设置 ##########
def main_update_motrix_settings():
    clear()
    print("正在修改Motrix配置")
    with open(usrDir+"/Library/Application Support/Motrix/system.json","r") as f:
        lines=f.readlines()
    os.system("rm -rf "+usrDir+"/Library/Application Support/Motrix/system.json")
    with open(usrDir+"/Library/Application Support/Motrix/system.json", 'w') as f:
        for i in range(len(lines)):
            if lines[i] == '''	"split": 64,\n''':
                   f.write('''	"split": 128,\n''')
            elif lines[i] == '''	"max-connection-per-server": 64,\n''':
                     f.write('''	"max-connection-per-server": 128,\n''')
            else:
                f.write(lines[i])
    with open(usrDir+"/Library/Application Support/Motrix/user.json","r") as f:
        lines=f.readlines()
    os.system("rm -rf "+usrDir+"/Library/Application Support/Motrix/user.json")
    with open(usrDir+"/Library/Application Support/Motrix/user.json", 'w') as f:
        for i in range(len(lines)):
            if lines[i] == '''	"engine-max-connection-per-server": 64,\n''':
                   f.write('''	"engine-max-connection-per-server": 256,\n''')
            else:
                f.write(lines[i])
    print("文件修改完成, 请手动重启Motrix")

########## Main ##########
print("注意！！本脚本需要Home Brew, 具体如何安装请问问搜索引擎")
print("知晓后按回车进入")
check=input()
if not find_file(usrDir+"/aria2","main.py","file"): # 检查是否在 ~/aria2 文件夹内
    main_check_motrix()
    main_download_aria2()
if not flag:
    main_patch_aria2()
    main_build_aria2()
    main_change_aria2()
    main_update_motrix_settings()
    print("🍺 成功执行所有脚本")
    check=input("点按回车退出")
