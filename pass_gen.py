from tkinter import *
from PIL import Image,ImageTk
import pyperclip
from pyperclip import *
import random

#make a window area
window = Tk()
window.title("Password Generator")
window.geometry("400x250")
img = Image.open('copy-button-icon.png')
resized_image = img.resize((30,30), Image.ANTIALIAS)
copy_button =ImageTk.PhotoImage(resized_image)
#create frame to assign buttons and labels to
frame = Frame(window,width=400,height=300,bg="#454545")
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
    global joined_pass
    joined_pass = "".join(generated_password)
    # display the output on the label textbox
    mystring.set(str(joined_pass))
    password_length=len(joined_pass)
    text_Box.config(width=password_length)
def copy_pass ():
    pyperclip.copy(joined_pass)
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

text_Box = Label(frame,justify=CENTER,textvariable=mystring,font=("courier",13),bg="#FF6000",fg="#212121",
                 height=2,width=100)
text_Box.place(relx=0.5,y=40,anchor=CENTER)

#check button to select if the password has Symboles
check_symboles = Checkbutton(frame,text="Symboles",bg="#FF6000",variable=symboles_checked,
                             onvalue=1,offvalue=0)
check_symboles.place(x=82,y=65)

#check button to select if the password has Numbers
check_numbers = Checkbutton(frame,text="Numbers",bg="#FF6000",variable=numbers_checked,
                             onvalue=1,offvalue=0)
check_numbers.place(relx=0.5,y=77,anchor=CENTER)

#check button to select if the password has Capitals
check_capital = Checkbutton(frame,text="Capitals",bg="#FF6000",variable=capital_checked,width=10,
                             onvalue=1,offvalue=0)
check_capital.place(x=240,y=65)

#slider to choose Password Length
pass_scale = Scale(frame, from_=12, to=36,orient=HORIZONTAL,variable=pass_slider,length=250,bd=0,fg="white", bg="#454545")
pass_scale.place(x=82,y=95)

title_label = Button(frame,text="Generate Password",font=("Roboto",14),fg="black",bg="#FF6000",
                     width=15,height=1,command=generate)
title_label.place(x=100,y=150)

title_label = Button(frame,image=copy_button, bg="#039B5F", width=35, height=35, command=copy_pass)
title_label.place(x=280,y=150)

#///////////////////////////////////////////////////////////////////
window.mainloop()
