import tkinter
from subprocess import Popen
import json
import os
import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("laxialaxtania","!Qwerty12345")


Items = []

### MAJOR FUNCTIONS ###


def buy():
    path = './Data'
    fileName = "UserData.json"
    msg = ("Hello! I'm; " + str(readUsername(path,fileName)) + ". I want to buy; " + str(itemList.get(tkinter.ACTIVE)) + " x " + str(quantityEntry.get()))
    server.sendmail("laxialaxtania@gmail.com","SaseteS@icloud.com",msg)
    print("Your buy request has been sent to server. Will be answered you in game as soon as possible. ")
    Popen('Python ./Apps/Attention.py')
    
def sell():
    path = './Data'
    fileName = "UserData.json"
    msg = ("Hello! I'm; " + str(readUsername(path,fileName)) + ". I want to sell; " + str(itemList.get(tkinter.ACTIVE)) + " x " + str(quantityEntry.get()))
    server.sendmail("laxialaxtania@gmail.com","SaseteS@icloud.com",msg)
    print("Your sell request has been sent to server. Will be answered you in game as soon as possible. ")
    Popen('Python ./Apps/Attention.py')
    
def close():
    main.quit()

### MAJOR FUNCTIONS ###


### MINOR FUNCTIONS ###

def refresh():
    path = './Items/'
    gold = readGold()
    itemList.delete(0, 'end')
    Items.clear()
    i = 0
    checkItems()
    while i  < len(Items):
        itemList.insert(0,(str(readName(path,str(Items[i]))) + ' Buy:' + str(readBuyValue(path,str(Items[i]))) + 's ')+ ' Sell:' + str(readSellValue(path,str(Items[i]))) + 's' + '   Amount: ' + str(readAmount(path,str(Items[i]))))
        i += 1

def checkItems():
    path = './Items/'
    for r,d,f in os.walk(path):
        for file in f:
            if '.json' in file:
                Items.append(file)

def readName(path, JSONname):# return the host name from json file
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('name')
    
def readUsername(path, JSONname):# return the host name from json file
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('username')
    
def readSellValue(path, JSONname):# return the host name from json file
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('sellvalue')

def readAmount(path, JSONname):# return the host name from json file
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('amount')

def readBuyValue(path, JSONname):# return the host name from json file
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('buyvalue')
    
def readGold():# return the host name from json file
    path = '/Data'
    JSONname = "GuildGoldData.json"
    filePathName = './' + path + '/' + JSONname
    with open(filePathName, 'r') as fp:
        Hostname = json.load(fp)
        return Hostname.get('gold')
    
def writeToJson(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
### MINOR FUNCTIONS ###
                
gold = readGold()
goldString = "Bank Gold: " + str(gold) + " Silver"

### INTERFACE ###

main = tkinter.Tk()
main.title("Market")
main.resizable(False,False)

listFrame = tkinter.Frame(main, background = "grey")
listFrame.pack()

scrollbar = tkinter.Scrollbar(listFrame,  background = "grey")
scrollbar.pack(side = tkinter.LEFT, fill = tkinter.Y)

itemList = tkinter.Listbox(listFrame, background = "grey", fg = "gold", height = 20, width = 60, yscrollcommand = scrollbar.set)
itemList.pack(side = tkinter.LEFT)


panelFrame = tkinter.Frame(listFrame, background = "grey")
panelFrame.pack(side = tkinter.RIGHT)

goldText = tkinter.Text(panelFrame, height = 3, width = 10,  background = "grey", fg = "white")
goldText.pack( side = tkinter.TOP)
goldText.insert(tkinter.END, goldString )
goldText.config(state = tkinter.DISABLED)


quantity = tkinter.IntVar()
quantity.set(0)

quantityEntry = tkinter.Entry(panelFrame, background = "grey", fg = "white", width = 10, textvariable = quantity, justify = tkinter.CENTER)
quantityEntry.pack()

buyButton = tkinter.Button(panelFrame, background = "grey", fg = "white", text = "BUY", width = 10, height = 2, command = buy)
buyButton.pack()

sellButton = tkinter.Button(panelFrame, background = "grey", fg = "white", text = "SELL", width = 10, height = 2, command = sell)
sellButton.pack()


closeButton = tkinter.Button(panelFrame, background = "grey", fg = "white", text = "Close", width = 10, height = 2, command = close)
closeButton.pack()


### INTERFACE ###

refresh()
tkinter.mainloop()

