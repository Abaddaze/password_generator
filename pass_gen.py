import tkinter as Tk
from tkinter import *

#Make A Window Area
window = Tk()
window.title("Password Generator")
window.geometry("300x300")

#create frame to assign buttons and labels to
frame = Frame(window,width=300,height=300)
frame.pack(expand=True)

#Adding The data the will be included in the password (Letters , Numbers , Symboles )

small_characters = "abcdefhijklmnopqrstuvwxyz"
cap_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_numbers = "1234567890"
all_numbers_rev = all_numbers[::-1]
all_symboles = "~`!@#$%^&*()_-+={[}]|\:"";'<,>.?/"

#///////////////////////////////////////////////////////////////////
#enteries and number variables
mystring=StringVar()
pass_text = StringVar()
mystring = StringVar()
capital_checked = IntVar()
symbole_checked = IntVar()
numbers_checked = IntVar()
pass_slider = IntVar()
#///////////////////////////////////////////////////////////////////
#DESIGN THE LAYOUT (Buttons and Texbox)
#text label to show the generated password
text_Box = Label(frame,textvariable=mystring,font=("courier",25),bg="#DBDBDB",fg="#039b5f",
                 width=50)
text_Box.place(x=0,y=40)

#check button to select if the password has Symboles
check_symboles = Checkbutton(frame,text="Symboles",bg="#039b5f",variable=symbole_checked,
                             onvalue=1,offvalue=0)
check_symboles.place(x=40,y=90)

#check button to select if the password has Numbers
check_symboles = Checkbutton(frame,text="Numbers",bg="#039b5f",variable=numbers_checked,
                             onvalue=1,offvalue=0)
check_symboles.place(x=130,y=90)

#check button to select if the password has symboles
check_symboles = Checkbutton(frame,text="Capitals",bg="#039b5f",variable=capital_checked,
                             onvalue=1,offvalue=0)
check_symboles.place(x=210,y=90)

#slider to choose Password Length
pass_scale = Scale(frame, from_=0, to=24,orient=HORIZONTAL,variable=pass_slider)
pass_scale.place(x=100,y=120)

title_label = Button(frame,text="GeneratePassword",font=("Roboto",14),fg="white",bg="#039b5f",
                     width=20,height=1,command="")
title_label.place(x=30,y=160)
#///////////////////////////////////////////////////////////////////
window.mainloop()
