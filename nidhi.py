# import email
import PIL
from PIL import ImageTk, Image
from tkinter import *


root = Tk()

root.title("Bulk Email Sender Application")
root.geometry('780x620+100+50')
root.resizable(0,0)
root.config(bg="powder blue")

titleFrame = Frame(root)
titleFrame.grid(row=0, column=0)

logoImage = PhotoImage(file= '../Bulk_Email_Sender/Assests/self_email_logo.png' )

<<<<<<< HEAD
# logo_old = Image.open('../Bulk_Email_Sender/Assests/self_email_logo.png')
# logo_resize = logo_old.resize((72, 72))
# logoImage = ImageTk.PhotoImage(logo_resize)
=======
logo_old=PIL.Image.open('../Bulk-Email-Sender/Assests/self_email_logo.png')
#logo_old = Image.open('../Bulk-Email-Sender/Assests/self_email_logo.png')
logo_resize = logo_old.resize((72, 72))
logoImage = ImageTk.PhotoImage(logo_resize)
>>>>>>> e94757bb7cfe4b0111dda4af29624c731b7fd162

titleLabel = Label(titleFrame, text= "    Email Sender   ", image= logoImage, compound=LEFT,bg= "pink", font=('arial','15','bold'))
titleLabel.grid(row=0, column=0)

settings_old = PIL.Image.open('../Bulk-Email-Sender/Assests/self_settings.png')
#settings_old = Image.open('../Bulk-Email-Sender/Assests/self_settings.png')
settings_resize = settings_old.resize((72, 74))
settingsImage = ImageTk.PhotoImage(settings_resize)

Button(titleFrame,image=settingsImage,bd=0,bg='pink',cursor='hand2',
       activebackground='pink').grid(row=0,column=1)

#for radio buttons
chooseFrame=Frame(root,bg='powder blue')
chooseFrame.grid(row=1,column=0,pady=10)
singleVariable=StringVar()
multipleVariable=StringVar()
singleRadioButton=Radiobutton(chooseFrame,text='Single     ',font=('Times New Roman', 22, 'bold'),
                              variable=singleVariable, value='Single', bg='powder blue',
                              activebackground='powder blue')
singleRadioButton.grid(row=0,column=0,padx=20)
multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('Times New Roman', 22, 'bold'),
                              variable=multipleVariable, value='Multiple', bg='powder blue',
                              activebackground='powder blue')
multipleRadioButton.grid(row=0,column=1,padx=20)

#label frame for email address
toLabelFrame=LabelFrame(root, text='To (Email address)', font=('Times New Roman', 12, 'bold'),
                        bg='powder blue', fg='blue', bd='5')
toLabelFrame.grid(row=2, column=0, padx=100)

toEntryField=Entry(toLabelFrame,font=('time new roman',15,'bold'), width='40')
toEntryField.grid(row=0, column=0)

#search button
search_old=PIL.Image.open('../Bulk-Email-Sender/Assests/self_search.png')
search_resize = search_old.resize((40, 40))
searchImage = ImageTk.PhotoImage(search_resize)

Button(toLabelFrame,text='  Search', image=searchImage,compound=LEFT, font=('times new roman',13,'bold'),
       bd=0,bg='powder blue',cursor='hand2',
       activebackground='powder blue').grid(row=0,column=1,padx=20)

#subject button
subjectLabelFrame=LabelFrame(root, text='Subject', font=('Times New Roman', 12, 'bold'),
                        bg='powder blue', fg='blue', bd='5')
subjectLabelFrame.grid(row=3, column=0,pady=10)

subjectEntryField=Entry(subjectLabelFrame,font=('time new roman',15,'bold'), width='40')
subjectEntryField.grid(row=0, column=0)

#text area to compose email
emailLabelFrame=LabelFrame(root, text='Compose email', font=('Times New Roman', 12, 'bold'),
                        bg='powder blue', fg='blue', bd='5')
emailLabelFrame.grid(row=4, column=0)

#mic button
mic_old=PIL.Image.open('../Bulk-Email-Sender/Assests/self_mic.png')
mic_resize = mic_old.resize((40, 40))
micImage = ImageTk.PhotoImage(mic_resize)
Button(emailLabelFrame,text='  Speak', image=micImage,compound=LEFT, font=('times new roman',13,'bold'),
       bd=0,bg='powder blue',cursor='hand2',
       activebackground='powder blue').grid(row=0,column=0)

#attachment button
attachment_old=PIL.Image.open('../Bulk-Email-Sender/Assests/self_attachments.png')
attachment_resize = attachment_old.resize((40, 40))
attachmentImage = ImageTk.PhotoImage(attachment_resize)
Button(emailLabelFrame,text='  Attachment', image=attachmentImage,compound=LEFT, font=('times new roman',13,'bold'),
       bd=0,bg='powder blue',cursor='hand2',
       activebackground='powder blue').grid(row=0,column=1)


textarea=Text(emailLabelFrame, font=('times new roman', 14,), height=8)
textarea.grid(row=1,column=0,columnspan=2)


send_old=PIL.Image.open('../Bulk-Email-Sender/Assests/self_send.png')
send_resize = send_old.resize((37, 37))
sendImage = ImageTk.PhotoImage(send_resize)
Button(root,image=sendImage,bd=0,bg='powder blue',cursor='hand2',
       activebackground='powder blue').place(x=490,y=540)

clear_old=PIL.Image.open('../Bulk-Email-Sender/Assests/self_clear.png')
clear_resize = clear_old.resize((43, 43))
clearImage = ImageTk.PhotoImage(clear_resize)
Button(root,image=clearImage,bd=0,bg='powder blue',cursor='hand2',
       activebackground='powder blue').place(x=590,y=550)

exit_old=PIL.Image.open('../Bulk-Email-Sender/Assests/self_exit.png')
exit_resize = exit_old.resize((40, 40))
exitImage = ImageTk.PhotoImage(exit_resize)
Button(root,image=exitImage,bd=0,bg='powder blue',cursor='hand2',
       activebackground='powder blue').place(x=690,y=550)


totalLabel=Label(root,font=('times new roman', 18,'bold'), bg='powder blue', fg='black')
totalLabel.place(x=10,y=560)
sentLabel=Label(root,font=('times new roman', 18,'bold'), bg='powder blue', fg='black')
sentLabel.place(x=100,y=560)
leftLabel=Label(root,font=('times new roman', 18,'bold'), bg='powder blue', fg='black')
leftLabel.place(x=190,y=560)
failedLabel=Label(root,font=('times new roman', 18,'bold'), bg='powder blue', fg='black')
failedLabel.place(x=280,y=560)
root.mainloop()