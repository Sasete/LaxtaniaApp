import tkinter
from subprocess import Popen
import json

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
    Popen('Python UserList.py')
    

def openMarket():
    Popen('Python Market.py')
    
def setData():
    username = nameEntry.get()
    path = './Data/'
    fileName = "UserData"
    newData = {}
    newData['username'] = username
    writeToJson(path, fileName, newData)

def writeToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

main = tkinter.Tk()
main.title("Laxtania")
main.resizable(False,False)



mainFrame = tkinter.Frame(main)
mainFrame.pack()

mainText = tkinter.Text(mainFrame, height = 10, width = 30)
mainText.pack( side = tkinter.LEFT)
mainText.insert(tkinter.END, mainString )
mainText.config(state = tkinter.DISABLED)

panelFrame = tkinter.Frame(mainFrame)
panelFrame.pack( side = tkinter.RIGHT )

sign_inFrame = tkinter.Frame(main)
sign_inFrame.pack( side = tkinter.BOTTOM )

textFrame = tkinter.Frame(sign_inFrame)
textFrame.pack( side = tkinter.LEFT )

buttonFrame = tkinter.Frame(sign_inFrame)
buttonFrame.pack( side = tkinter.RIGHT )

username = tkinter.StringVar()
username.set("")

userListButton = tkinter.Button(panelFrame, text = "Userlist", fg = "green", width = 10, height = 5, command = openUserList)
userListButton.pack(side = tkinter.TOP)

marketButton = tkinter.Button(panelFrame, text = "Market",fg = "black", width = 10, height = 5, command = openMarket)
marketButton.pack(side = tkinter.BOTTOM)

userText = tkinter.Text(sign_inFrame, width = 12, height = 1)
userText.pack(side = tkinter.LEFT)
userText.insert(tkinter.END, "Username:" )
userText.config(state = tkinter.DISABLED)

nameEntry = tkinter.Entry(sign_inFrame, width = 15, textvariable = username, justify = tkinter.CENTER)
nameEntry.pack(side = tkinter.RIGHT)

setButton = tkinter.Button(buttonFrame, text = "SET", width = 15, height = 1, command = setData)
setButton.pack(side = tkinter.RIGHT)

tkinter.mainloop()
