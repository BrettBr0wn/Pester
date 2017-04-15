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

from Tkinter import *
window = Tk()

label1 = Label(window,text="Name")
label2 = Label(window,text="Password")

entry1 = Entry(window)
entry2 = Entry(window)

#E stands for east
label1.grid(row=0, column=0, sticky=E)
label2.grid(row=1, column=0, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkBox = Checkbutton(window, text="Keep Me Logged In")

checkBox.grid(row=2, columnspan=2)

window.mainloop()


##Tkinter Lesson 6

from Tkinter import *
window = Tk()





window.mainloop()