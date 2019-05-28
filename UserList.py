import tkinter
from subprocess import Popen
import json
import os



Users = []

### MAJOR FUNCTIONS ###


def refresh():
    path = './Users/'
    userList.delete(0, 'end')
    Users.clear()
    i = 0
    checkUsers()
    while i  < len(Users):
        userList.insert(0,(str(readUsername(path,str(Users[i]))) + "  :         Trust:   " + str(readTrust(path,str(Users[i])))))
        i += 1
    print('Userlist has been refreshed.')
   


def close():
    main.quit()



### MAJOR FUNCTIONS ###


### MINOR FUNCTIONS ###


def checkUsers():
    path = './Users/'
    for r,d,f in os.walk(path):
        for file in f:
            if '.json' in file:
                Users.append(file)

def readUsername(path, JSONname):# return the host name from json file
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('username')
    
def readTrust(path, JSONname):# return the host name from json file
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('trust')

def writeToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
### MINOR FUNCTIONS ###


### INTERFACE ###
    
main = tkinter.Tk()
main.title("Userlist")
main.resizable(False,False)


listFrame = tkinter.Frame(main)
listFrame.pack()

scrollbar = tkinter.Scrollbar(listFrame)
scrollbar.pack(side = tkinter.LEFT, fill = tkinter.Y)

userList = tkinter.Listbox(listFrame, height = 20, width = 40, yscrollcommand = scrollbar.set)
userList.pack(side = tkinter.LEFT)

panelFrame = tkinter.Frame(listFrame)
panelFrame.pack(side = tkinter.RIGHT)


username = tkinter.StringVar()
username.set("")
trustPoint = tkinter.IntVar()
trustPoint.set(0)


refreshButton = tkinter.Button(panelFrame, text = "Refresh", width = 10, height = 2, command = refresh)
refreshButton.pack()

closeButton = tkinter.Button(panelFrame, text = "Close", width = 10, height = 2, command = close)
closeButton.pack()

### INTERFACE ###



refresh()
tkinter.mainloop()
