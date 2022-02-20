from re import M
from PIL import ImageTk, Image
import tkinter as tk
# from tkinter import *

root = tk.Tk()

root.title("Bulk Email Sender Application")
root.geometry('780x620+100+50')
root.resizable(0,0)
root.config(bg="powder blue")

# titleFrame = Frame(root)
# titleFrame.grid(row=0, column=0)

logo_old = Image.open('/home/hp1/Desktop/Bulk_Email_Sender/Assests/self_email_logo.png')
logo_resize = logo_old.resize((72, 72))
logoImage = ImageTk.PhotoImage(logo_resize)

titleLabel = tk.Label(root,  image= logoImage,bg= "pink")
titleLabel.grid(row=0, column=0)
root.mainloop()