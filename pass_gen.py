import tkinter as Tk
from tkinter import *

#Make A Window Area
window = Tk()
window.title("Password Generator")
window.geometry("300x300")
window.mainloop()

#create frame to assign buttons and labels to
frame = Frame(window,width=300,height=300)
frame.pack(expand=True)

#small characters , capital characters, Numbers , numbers in revers , symboles

small_characters = "abcdefhijklmnopqrstuvwxyz"
cap_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_numbers = "1234567890"
all_numbers_rev = all_numbers[::-1]
all_symboles = "~`!@#$%^&*()_-+={[}]|\:"";'<,>.?/"