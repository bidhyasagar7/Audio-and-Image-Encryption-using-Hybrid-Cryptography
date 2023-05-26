from tkinter import *
from tkinter import ttk
import hybrid_encryption
from getpass import getuser
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox
# import tkinter.messagebox

def message(name, button, mgs_label):
    """This function displayed the massage, return by either Encryption or Decryption"""

    button['state'] = DISABLED  # make button state disable'
    if button["text"] == "Encrypt":
        mgs = hybrid_encryption.encryption(name)
        mgs_label.config(text=mgs, background="grey")

    if button["text"] == "Decrypt":
        mgs = hybrid_encryption.decryption(name)
        mgs_label.config(text=mgs, background="grey")


def open_file():
    """
    This function open the file dialog box for choosing the file.
    And then making two buttons : encrypt_button, decrypt_button
    """
    username = getuser()
    initialdirectory = "C:/Users/{}".format(username)
    name = askopenfilename(initialdir=initialdirectory, filetypes=[("All files", "*.*")], title="Choose a file")
    #for x in filetypes:


    if name:
                #file_name = hybrid_encryption.get_file_name(name, extension=True)
                #label.config(text=file_name)

                mgs_label = Label(root)
                mgs_label.place(x=530, y=560)
                encrypt_button = Button(root, text="Encrypt", height="1", width="25", bd=10, relief="groove", fg="white", bg="#29201E", command=lambda: message(name, encrypt_button, mgs_label))
                decrypt_button = Button(root, text="Decrypt", height="1", width="25", bd=10, relief="groove", fg="white", bg="#29201E", command=lambda: message(name, decrypt_button, mgs_label))
                encrypt_button.place(x=530, y=350)
                decrypt_button.place(x=965, y=350)

    else:
        wrongfile()

def wrongfile():
    wayOut = tkinter.messagebox.askyesno("Wrong File Type",
                                                        "Do you want to choose again?")
    if wayOut > 0:
        return
    else:
        root.destroy()

root = Tk()
#root.get_themes()
#root.set_theme("clearlooks")
icon = PhotoImage(file="images/icon.png")  # Icon for the window
root.iconphoto(False, icon)
title = root.title("Hybrid Encryption")

app_width = 1360
app_height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Evaluating X and Y coordinate such that,Window always comes into the center.
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# background image
img = Image.open("D:\Python\Projects\Minor_Project\Hybrid_Encryption/mainwind.png")
img1 = ImageTk.PhotoImage(img)

# creating canvas
canvas = Canvas(root, width=0, height=0)
canvas.pack(fill=BOTH, expand=True)

# adding image to the canvas
canvas.create_image(-210, -150, image=img1, anchor='nw')


# function to resize the window
"""def resize_img(e):
    global image, resized, image2
    image = Image.open(("mainwin.png"))  # open image to resize it
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')"""


root.bind("<Configure>", img1)

#title_label = ttk.Label(root, text="Welcome to Hybrid Encryption Application", font=("Helvetica ", 14))
#title_label.pack()
#title_label(root, text="").pack()
choose_file_button = Button(root, text="Choose File", height="1", width="25", bd=10, relief="groove", fg="white", bg="#29201E", font=('bold'), command=open_file)
choose_file_button.place(x=720, y=180)
"""style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')],
    )"""

# root.iconbitmap('D:\Python\Projects\Minor_Project\Hybrid_Encryption/HE_icon.ico')
root.mainloop()

