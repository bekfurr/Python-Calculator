
#This application is in test mode and is under development
#Powered By BEKFURR
from tkinter import * #Tkinter library called

window = Tk()
#Function of add
def Qosh():
    son = int(Raqam.get())
    son1 = int(Raqam2.get())
    C = son + son1
    text.insert(0.0, C)
#Function of Separation
def Ayr():
    son = int(Raqam.get())
    son1 = int(Raqam2.get())
    C = son - son1
    text1.insert(0.0, C)
#Function of Increase        
def Kop():
    son = int(Raqam.get())
    son1 = int(Raqam2.get())
    C = son * son1
    text2.insert(0.0, C)    
#Function of / (I couldn't find the translation)
def Bol():
    son = int(Raqam.get())
    son1 = int(Raqam2.get())
    son3 = str("Noto^g^ri")
    C = son / son1
    text3.insert(0.0, C)
#Function of Degree
def Dar():
    son = int(Raqam.get())
    son1 = int(Raqam2.get())
    C = son ** son1
    text4.insert(0.0, C)
#Function of The rest
def Qol():
    son = int(Raqam.get())
    son1 = int(Raqam2.get())
    C = son % son1
    text5.insert(0.0, C)

window.title('Python Calculator')
window.geometry('320x390')
label = Label(window,text="First Number") 
label.grid(row=1, column=1, sticky=W) 
Raqam = Entry(window, width=25)
Raqam.grid(row=2, column=1, sticky=W) 
label = Label(window,text="First Number") 
label.grid(row=3, column=1, sticky=W) 
Raqam2 = Entry(window, width=25) 
Raqam2.grid(row=4, column=1, sticky=W) 

button = Button(window, text="    +    ", command=Qosh) 
button.grid(row=6, column=0, ) 

button = Button(window, text="    -    ", command=Ayr)
button.grid(row=7, column=0,)

button = Button(window, text="    x     ", command=Kop) 
button.grid(row=6, column=1, ) #F
button = Button(window, text="    /   ", command=Bol) 
button.grid(row=6, column=2, sticky=W) 
button = Button(window, text="degree", command=Dar)
button.grid(row=7, column=1,) 
button = Button(window, text="residual", command=Qol) 
button.grid(row=7, column=2, sticky=W) 
label = Label(window,text="Total") 
label.grid(row=8, column=1, sticky=W)
text = Text(window, width=25, height=1) 
text.grid(row=9, column=1, sticky=W) 
label = Label(window,text="Minus") 
label.grid(row=10, column=1, sticky=W) 
text1 = Text(window, width=25, height=1)
text1.grid(row=11, column=1, sticky=W) 
label = Label(window,text="Multiplication") 
label.grid(row=12, column=1, sticky=W) 
text2 = Text(window, width=25, height=1) 
text2.grid(row=13, column=1, sticky=W)
label = Label(window,text="Division") 
label.grid(row=14, column=1, sticky=W)
text3 = Text(window, width=25, height=1) 
text3.grid(row=15, column=1, sticky=W) 
label = Label(window,text="Degree") 
label.grid(row=16, column=1, sticky=W)
text4 = Text(window, width=25, height=1) 
text4.grid(row=17, column=1, sticky=W) 
label = Label(window,text="The rest")
label.grid(row=18, column=1, sticky=W) 
text5 = Text(window, width=25, height=1) 
text5.grid(row=19, column=1, sticky=W) 

window.mainloop()

