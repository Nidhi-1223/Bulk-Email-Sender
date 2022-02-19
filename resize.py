from re import M
import tkinter as tk
from PIL import Image, ImageTk

my_w = tk.Tk()
my_w.geometry('400x300')
my_w.title("hjfoijoi")
img_old = Image.open('../Bulk_Email_Sender/Assests/self_email_logo.png')
img_resized = img_old.resize((72,72))
my_img = ImageTk.PhotoImage(img_resized)
ii = tk.Label(my_w, image=my_img, text="idk whats going on")
ii.grid(row=1, column=1)

my_w.mainloop()