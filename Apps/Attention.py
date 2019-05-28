import tkinter


mystring = 'Your request has been sent to server. Please be \nsure to send your resources(gather result if your resource is labor) or golds to Sassii in game.'

def close():
    main.quit()


main = tkinter.Tk()
main.title("Attention")
main.resizable(False,False)

mainFrame = tkinter.Frame(main, background = "gray")
mainFrame.pack(fill = tkinter.BOTH)

text = tkinter.Text(mainFrame, height = 4, width = 50, background = "gray", fg = "gold")
text.pack()
text.insert(tkinter.END, mystring)
text.config(state = tkinter.DISABLED)


button = tkinter.Button(mainFrame, text = "Okay", width = 10, height = 2, background = "gray", fg = "darkred", command = close)
button.pack()

tkinter.mainloop()
