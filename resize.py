from re import M
import tkinter as tk
from PIL import Image, ImageTk

my_w = tk.Tk()
my_w.geometry('400x300')
my_w.title("hjfoijoi")

img_old = Image.open('../Bulk_Email_Sender/Assests/self_email_logo.png')
img_resized = img_old.resize((72,72))
my_img = ImageTk.PhotoImage(img_resized)

ii = tk.Label(my_w, bg= "pink", image=my_img)
ii.grid(row=0, column=0)

ii2 = tk.Label(my_w, bg="powder blue", text="ii2 jifjifjiomsuaf9ouoiasuuieur90w")
ii2.grid(row=0, column=1)

my_w.mainloop()