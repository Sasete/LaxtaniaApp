import tkinter
from subprocess import Popen
import json
import urllib.request
import zipfile
import shutil, os, glob
import subprocess


def readGold():# return the host name from json file
    path = 'Data'
    JSONname = "GuildGoldData.json"
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('gold')

gold = readGold()

mainString = "\n\n\t    Welcome \n       to application of \n\tLaxtania Guild!\n\t     Gold: " + str(gold) +"\n\t Leader: Sasete \n"


def openUserList():
    Popen('Python ./Apps/UserList.py')
    

def openMarket():
    Popen('Python ./Apps/Market.py')
    
def setData():
    username = nameEntry.get()
    path = './Data/'
    fileName = "UserData"
    newData = {}
    newData['username'] = username
    writeToJson(path, fileName, newData)
    print("Username set as," + str(username))

def writeToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
def refresh():
    print('File downloading from internet to update Data.')
    url = 'https://github.com/Sasete/LaxtaniaApp/archive/master.zip'
    urllib.request.urlretrieve(url, './LaxtaniaApp.zip')
    
    zipRef = zipfile.ZipFile('./LaxtaniaApp.zip','r')
    zipRef.extractall()
    filelist = glob.glob(os.path.join('./Data', "*.json"))
    for f in filelist:
        os.remove(f)
    os.rmdir('./Data')
    shutil.move('./LaxtaniaApp-master/Data','./')

    filelist = glob.glob(os.path.join('./Items', "*.json"))
    for f in filelist:
        os.remove(f)
    os.rmdir('./Items')
    shutil.move('./LaxtaniaApp-master/Items','./')

    filelist = glob.glob(os.path.join('./Users', "*.json"))
    for f in filelist:
        os.remove(f)    
    os.rmdir('./Users')
    shutil.move('./LaxtaniaApp-master/Users','./')
    
    filelist = glob.glob(os.path.join('./Apps', "*.py"))
    for f in filelist:
        os.remove(f)
    os.rmdir('./Apps')
    shutil.move('./LaxtaniaApp-master/Apps','./')
    zipRef.close()
    
    filelist = glob.glob(os.path.join('./LaxtaniaApp-master', "*.py"))
    for f in filelist:
        os.remove(f)
    os.remove('./Log.txt')    
    shutil.move('./LaxtaniaApp-master/Log.txt','./')
    filelist = glob.glob(os.path.join('./LaxtaniaApp-master', "*.txt"))
    for f in filelist:
        os.remove(f)
    os.remove('./LaxtaniaApp-master/.gitignore')
    os.remove('./LaxtaniaApp-master/.gitattributes')


    
    os.rmdir('./LaxtaniaApp-master')
    
    os.remove('LaxtaniaApp.zip')
    print('Updated succesfully!')
    
def moveAllFilesinDir(srcDir, dstDir):
    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            # Move each file to destination Directory
            shutil.move(filePath, dstDir);
    else:
        print("srcDir & dstDir should be Directories")
        
main = tkinter.Tk()
main.title("Laxtania")
main.resizable(False,False)



mainFrame = tkinter.Frame(main, bg = "gray")
mainFrame.pack()

mainText = tkinter.Text(mainFrame, bg = "gray", fg = "gold", height = 12, width = 30)
mainText.pack( side = tkinter.LEFT)
mainText.insert(tkinter.END, mainString )
mainText.config(state = tkinter.DISABLED)

panelFrame = tkinter.Frame(mainFrame, bg = "gray")
panelFrame.pack( side = tkinter.RIGHT )

sign_inFrame = tkinter.Frame(main, bg = "gray")
sign_inFrame.pack( side = tkinter.BOTTOM , fill = tkinter.X)

textFrame = tkinter.Frame(sign_inFrame, bg = "gray")
textFrame.pack( side = tkinter.LEFT )

buttonFrame = tkinter.Frame(sign_inFrame, bg = "gray")
buttonFrame.pack( side = tkinter.RIGHT )

username = tkinter.StringVar()
username.set("")

userListButton = tkinter.Button(panelFrame, bg = "gray", fg = "white", text = "Userlist", width = 10, height = 3, command = openUserList)
userListButton.pack()

marketButton = tkinter.Button(panelFrame, bg = "gray", fg = "white", text = "Market", width = 10, height = 3, command = openMarket)
marketButton.pack()

updateButton = tkinter.Button(panelFrame, bg = "gray", fg = "blue", text = "Update", width = 10, height = 4, command = refresh)
updateButton.pack()

userText = tkinter.Text(sign_inFrame, bg = "gray", fg = "gold", width = 12, height = 1)
userText.pack(side = tkinter.LEFT)
userText.insert(tkinter.END, "Username:" )
userText.config(state = tkinter.DISABLED)

nameEntry = tkinter.Entry(sign_inFrame, bg = "gray", fg = "white", width = 15, textvariable = username, justify = tkinter.CENTER)
nameEntry.pack(side = tkinter.RIGHT)

setButton = tkinter.Button(buttonFrame, bg = "gray", fg = "gold", text = "SET", width = 15, height = 1, command = setData)
setButton.pack(side = tkinter.RIGHT)


refresh()
tkinter.mainloop()
