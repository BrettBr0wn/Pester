# HW2: Draw an application vision and upload it to github
#
##########################################################
#
#
# Pseudo-Code for Pester
#
# Basic Functions:
# 1) Messenger
# 2) Timer
# 3) Date Range
# 4) Application Framework
#   A. Send Button
#   B. Multi-Line Text Field
#   C. Calendar
#   D. Number Drop Down
#   E. Frequency Drop Down
#   F. Send Page
#       a. Complete Message
#       b. Back Button
#
#
#
#
##############################################################
#                      Tkinter Lessons
#
#  https://www.youtube.com/channel/UCJbPGzawDH1njbqV-D5HqKw
#
##############################################################


##Tkinter Lesson 1
#from Tkinter import *



#window = Tk()

#label = Label(window, text="hey")


#label.pack()

#window.mainloop()


##Tkinter Lesson 2

#from Tkinter import *
#window = Tk()

#topFrame = Frame(window)
#topFrame.pack(side=TOP)

#bottomFrame = Frame(window)
#bottomFrame.pack(side=BOTTOM)

#button1 = Button(topFrame,text="Button1",fg="red")
#button2 = Button(topFrame,text="Button2",fg="blue")
#button3 = Button(topFrame,text="Button3",fg="green")
#button4 = Button(bottomFrame,text="Button4",fg="purple")


#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=BOTTOM)


#window.mainloop()

##Tkinter Lesson3

#from Tkinter import *
#window = Tk()

#label1 = Label(window, text="one", bg="red", fg="white")

#label1.pack()

#label2 = Label(window, text="two", bg="green", fg="black")

#label2.pack(fill=X)

#label3 = Label(window, text="three", bg="blue", fg="white")

#label3.pack(side=LEFT, fill=Y)

#window.mainloop()

##Tkinter Lesson 4 & 5

#from Tkinter import *
#window = Tk()

#label1 = Label(window,text="Name")
#label2 = Label(window,text="Password")

#entry1 = Entry(window)
#entry2 = Entry(window)

##E stands for east
#label1.grid(row=0, column=0, sticky=E)
#label2.grid(row=1, column=0, sticky=E)

#entry1.grid(row=0, column=1)
#entry2.grid(row=1, column=1)

#checkBox = Checkbutton(window, text="Keep Me Logged In")

#checkBox.grid(row=2, columnspan=2)

#window.mainloop()


##Tkinter Lesson 6

#from Tkinter import *
#window = Tk()


##Way to do this 1
##def printName():
##    print("Hello my name is Connor!")



##button1 = Button(window,text="Print my name",command=printName)
##button1.pack()

##Way to do this 2
#def printName(event):
#    print("Hello my name is Connor!")

##binds a button click to the functions
#button1 = Button(window,text="Print my name")
#button1.bind("<Button-1>", printName)
#button1.pack()


#window.mainloop()


##Tkinter Lesson 7

#from Tkinter import *
#window = Tk()

#def leftClick(event):
#    print("Left")

#def rightClick(event):
#    print("Right")

#def middleClick(event):
#    print("Middle")


#frame = Frame(window, width=300, height=250)

#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)

#frame.pack()

#window.mainloop()

##Tkinter Lesson 8
from Tkinter import *


#class ConnorsButtons:
    
#    #class constructor
#    #self references the class 
#    def __init__(self, master):
#        frame = Frame(master)
#        frame.pack()
        
#        self.printButton = Button(frame, text="Print Message",command=self.printMessage)
#        self.printButton.pack(side=LEFT)

#        self.quitButton = Button(frame, text="Quit", command=frame.quit)
#        self.quitButton.pack(side=LEFT)

#    def printMessage(self):
#        print("Wow this actually worked")

#window = Tk()

#obj = ConnorsButtons(window)

#window.mainloop()

##Tkinter Lesson 9

#from Tkinter import *

#def doNothing():
#    print("Nothing")

#window = Tk()

#menu = Menu(window)

#window.config(menu=menu)


#subMenu = Menu(menu)
#menu.add_cascade(label="File",menu=subMenu)

#subMenu.add_command(label="New Project...",command=doNothing)
#subMenu.add_command(label="Save",command=doNothing)

#subMenu.add_separator()

#subMenu.add_command(label="Exit",command=doNothing)

#editMenu = Menu(menu)
#menu.add_cascade(label="Edit",menu=editMenu)
#editMenu.add_command(label="Redo",command=doNothing)

## How do you get rid of the dashed line which does weird stuff?
#window.mainloop()




##Tkinter Lesson 10

#from Tkinter import *

#def doNothing():
#    print("Nothing")

#window = Tk()

##***** Main Menu ******

#menu = Menu(window)

#window.config(menu=menu)


#subMenu = Menu(menu)
#menu.add_cascade(label="File",menu=subMenu)

#subMenu.add_command(label="New Project...",command=doNothing)
#subMenu.add_command(label="Save",command=doNothing)

#subMenu.add_separator()

#subMenu.add_command(label="Exit",command=doNothing)

#editMenu = Menu(menu)
#menu.add_cascade(label="Edit",menu=editMenu)
#editMenu.add_command(label="Redo",command=doNothing)


## ***** The Toolbar *****


#toolbar = Frame(window,bg="blue")

#insertButton = Button(toolbar, text="Insert Image",command=doNothing)

#insertButton.pack(side=LEFT,padx=2,pady=2)

#printButton = Button(toolbar, text="Print",command=doNothing)

#printButton.pack(side=LEFT,padx=2,pady=2)


#toolbar.pack(side=TOP,fill=X)

#window.mainloop()


##Tkinter Lesson 11

#from Tkinter import *

#def doNothing():
#    print("Nothing")

#window = Tk()

##***** Main Menu ******

#menu = Menu(window)

#window.config(menu=menu)


#subMenu = Menu(menu)
#menu.add_cascade(label="File",menu=subMenu)

#subMenu.add_command(label="New Project...",command=doNothing)
#subMenu.add_command(label="Save",command=doNothing)

#subMenu.add_separator()

#subMenu.add_command(label="Exit",command=doNothing)

#editMenu = Menu(menu)
#menu.add_cascade(label="Edit",menu=editMenu)
#editMenu.add_command(label="Redo",command=doNothing)


## ***** The Toolbar *****


#toolbar = Frame(window,bg="blue")

#insertButton = Button(toolbar, text="Insert Image",command=doNothing)

#insertButton.pack(side=LEFT,padx=2,pady=2)

#printButton = Button(toolbar, text="Print",command=doNothing)

#printButton.pack(side=LEFT,padx=2,pady=2)


#toolbar.pack(side=TOP,fill=X)


## ***** Status Bar *****
##bd = boarder
#status = Label(window, text="File Saved",bd=1, relief=SUNKEN, anchor=W)
#status.pack(side=BOTTOM, fill=X)


#window.mainloop()

##Tkinter Lesson 12

#from Tkinter import *
#import tkMessageBox


#window = Tk()


#tkMessageBox.showinfo('Window Title', 'Window Message')

#answer = tkMessageBox.askquestion('Window Title', 'Yes or No Question')

#if answer == 'yes':
#    print("Yes")
    

#window.mainloop()

##Tkinter Lesson 13
from Tkinter import *

window = Tk()

canvas = Canvas(window, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0,0,200,100)
redLine = canvas.create_line(200,0,0,100,fill="red")

greenBox = canvas.create_rectangle(50,50,100,100,fill="green")

canvas.delete(redLine)

canvas.delete(ALL)


window.mainloop()