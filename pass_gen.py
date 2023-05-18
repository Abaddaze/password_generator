from tkinter import *

import pyperclip
from pyperclip import *
import random

#make a window area
window = Tk()
window.title("Password Generator")
window.geometry("300x300")

#create frame to assign buttons and labels to
frame = Frame(window,width=600,height=300,bg="red")
frame.pack(expand=True)

#our data types for output , small chcarachters , caps , numbers , numbers in reverse order , symboles
small_charachters = "abcdefhijklmnopqrstuvwxyz"
cap_charachters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_numbers = "1234567890"
all_numbers_rev = all_numbers[::-1]
all_symboles = "~`!@#$%^&*()_-+={[}]|\:"";'<,>.?/"

#code logic in here
#writing the logic for the generate button


def generate():
    if (capital_checked.get()==1) and (symboles_checked.get()==1) and (numbers_checked.get()==1):
        all_types = small_charachters + cap_charachters + all_symboles + all_numbers + all_numbers_rev

    elif (capital_checked.get()==1) and (numbers_checked.get()==1) :
        all_types = small_charachters + cap_charachters + all_numbers + all_numbers_rev

    elif (capital_checked.get()==1) and (symboles_checked.get()==1) :
        all_types = small_charachters + cap_charachters + all_symboles 

    elif (numbers_checked.get()==1) and (symboles_checked.get()==1):
        all_types = small_charachters + all_symboles + \
        all_numbers + all_numbers_rev

    elif (symboles_checked.get()==1):
        all_types = small_charachters + all_symboles

    elif (numbers_checked.get()==1):
        all_types = small_charachters + all_numbers
         
    elif (capital_checked.get()==1):
        all_types = small_charachters + cap_charachters
    else:
        all_types = small_charachters
    #display the password that includes (Small Letters , Capital Letters , 
    # Symboles , Numbers)

    #generate password from all_types variable using random.choice and for loop in range method
    generated_password = [random.choice(all_types) for i in range(pass_slider.get())]
    # join password output to make it in 1 sentence
    joined_pass = "".join(generated_password)
    # display the output on the label textbox
    mystring.set(str(joined_pass))
    password_length=len(joined_pass)
    text_Box.config(width=password_length)
#enteries and number variables
mystring=StringVar()
pass_text = StringVar()
mystring = StringVar()
capital_checked = IntVar()
symboles_checked = IntVar()
numbers_checked = IntVar()
pass_slider = IntVar()

#DESIGN THE LAYOUT (Buttons and Texbox)
#text label to show the generated password

text_Box = Label(frame,justify=CENTER,textvariable=mystring,font=("courier",25),bg="#DBDBDB",fg="#039b5f",
                 width=100)
text_Box.place(relx=0.5,y=40,anchor=CENTER)

#check button to select if the password has Symboles
check_symboles = Checkbutton(frame,text="Symboles",bg="#039b5f",variable=symboles_checked,
                             onvalue=1,offvalue=0)
check_symboles.place(x=110,y=90)

#check button to select if the password has Numbers
check_numbers = Checkbutton(frame,text="Numbers",bg="#039b5f",variable=numbers_checked,
                             onvalue=1,offvalue=0)
check_numbers.place(x=210,y=90)

#check button to select if the password has Capitals
check_capital = Checkbutton(frame,text="Capitals",bg="#039b5f",variable=capital_checked,width=10,
                             onvalue=1,offvalue=0)
check_capital.place(x=310,y=90)

#slider to choose Password Length
pass_scale = Scale(frame, from_=0, to=24,orient=HORIZONTAL,variable=pass_slider)
pass_scale.place(x=210,y=125)

title_label = Button(frame,text="GeneratePassword",font=("Roboto",14),fg="white",bg="#039b5f",
                     width=20,height=1,command=generate)
title_label.place(y=200, relx=0.5,anchor=CENTER)
#///////////////////////////////////////////////////////////////////
window.mainloop()
