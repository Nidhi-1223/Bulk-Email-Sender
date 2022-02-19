# import email
from PIL import ImageTk, Image
from tkinter import *


root = Tk()

root.title("Bulk Email Sender Application")
root.geometry('780x620+100+100')
root.resizable(0,0)
root.config(bg="powder blue")

titleFrame = Frame(root)
titleFrame.grid(row=0, column=0)

# logoImage = PhotoImage(file= '../Bulk_Email_Sender/Assests/self_email_logo.png' )

logo_old = Image.open('../Bulk_Email_Sender/Assests/self_email_logo.png')
logo_resize = logo_old.resize((72, 72))
logoImage = ImageTk.PhotoImage(logo_resize)

titleLabel = Label(titleFrame, text= "Email Sender", image= logoImage, compound=LEFT, bg= "pink")
titleLabel.grid(row=0, column=0)




root.mainloop()