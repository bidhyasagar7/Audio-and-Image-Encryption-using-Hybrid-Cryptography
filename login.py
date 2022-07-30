from tkinter import *
import tkinter.messagebox
import mysql.connector
from PIL import ImageTk, Image
from tkinter import ttk
# from tkinter import ttk
#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="abcd@123",database="test")
cursordb = connectiondb.cursor()


def login():
    global root2
    root2 = Toplevel(root)
    #root2.config(bg="white")

    #Title
    root2.title("Account Login")
    icon = PhotoImage(file="images/icon.png")  # icon for the window
    root2.iconphoto(False, icon)

    # Designate center location
    app_width = 1360
    app_height = 768
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    root2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # background image
    img2 = Image.open("D:\Python\Projects\Minor_Project\Hybrid_Encryption/Username1.png")
    img3 = ImageTk.PhotoImage(img2)

    # creating canvas
    canvas1 = Canvas(root2, width=1360, height=768)
    canvas1.pack(fill=BOTH, expand=True)

    # adding image to the canvas
    canvas1.create_image(0, 0, image=img3, anchor='nw')

    # function to resize the window
    def resize_img(e1):
        global image, resized, image2
        image = Image.open(("Username1.png"))  # open image to resize it
        resized = image.resize((e1.width, e1.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas1.create_image(0, 0, image=image2, anchor='nw')

    root2.bind("<Configure>", resize_img)

    global username_verification
    global password_verification

    username_verification = StringVar()
    password_verification = StringVar()

    btn4 = Label(root2, text="Username", fg="black", bg="white", font=('arial', 12, 'bold'), width=8, anchor='w')
    btn4.place(x=100, y=250)
    btn5 = Entry(root2, textvariable=username_verification, width=40)
    btn5.place(x=100, y=290)
    btn6 = Label(root2, text="Password", fg="black", bg="white", font=('arial', 12, 'bold'), width=8, anchor='w')
    btn6.place(x=100, y=340)
    btn7 = Entry(root2, textvariable=password_verification, show="*", width=40)
    btn7.place(x=100, y=380)
    btn8 = Button(root2, text="Log In", bg="black", fg='white', relief="groove", font=('arial', 12, 'bold'), command=login_verification,)
    btn8.place(x=190, y=430)
    btn9 = Button(root2, text="Forgot password?", fg="black", bg="white", font=('arial', 12, 'bold'), width=14, anchor='w', command=forgot_pwd)
    btn9.place(x=100, y=490)

def forgot_pwd():
    btn10 = Label(root2, text="Contact Customer Service: abcd@gmail.com", fg="black", bg="white", font=('arial', 12, 'bold'), width=35, anchor='w')
    btn10.place(x=100, y=550)
def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    root2.destroy()
    root.destroy()

    import setup
    setup.root.mainloop()
    #connectiondb.close()
    #Label(logged_message, text="").pack()
    #Button(logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Try Again", bg="#134f5c", fg='white', relief="groove", font=('arial', 12, 'bold'), command = failed_destroy).pack()

def about():
    #Title
    global about_message
    about_message = Toplevel(root)
    about_message.title("About")
    icon = PhotoImage(file="images/icon.png")  # icon for the window
    about_message.iconphoto(False, icon)
    about_message.geometry("500x400")

    #About Info
    text_label1 = Label(about_message, text="HYBRID ENCRYPTION\n ", font=('Brush Script', 17, 'bold'))
    text_label1.pack()
    text_label2 = Label(about_message, text = "Hybrid encryption is a mode of encryption that merges\n two or more encryption systems. It incorporates a\n combination of asymmetric and symmetric encryption to\n benefit from the strengths of each form of encryption. These \nstrengths are respectively defined as speed and security.", font=('Times New Roman', 14))
    text_label2.pack()
    text_label3 = Label(about_message, text = "\nWith the help of this application, you can secure your\n file in plain sight. Anyone with whom you are sharing\n this device won't be able to snoop in your personal \nand private items. The application  keeps you safe.\n Thank You for using this app! ", font=('Times New Roman', 14))
    text_label3.pack()

def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from usertable where username = %s and password = %s"
    cursordb.execute(sql, [(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return

def main_display():
    global root
    root = Tk()
    root.config(bg="white")

    # background image
    img = Image.open("D:\Python\Projects\Minor_Project\Hybrid_Encryption/Lock.jpg")
    img1 = ImageTk.PhotoImage(img)
    # Desginate height and width of app
    app_width = 1360
    app_height = 768
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    #Title
    root.title("Hybrid Encryption")
    icon = PhotoImage(file="images/icon.png")  # icon for the window
    root.iconphoto(False, icon)

    # creating canvas
    canvas = Canvas(root, width=1360, height=768)
    canvas.pack(fill=BOTH, expand=True)

    #adding image to the canvas
    canvas.create_image(0, 0, image=img1, anchor='nw')

    # function to resize the window
    def resize_img(e):
        global image, resized, image2
        image = Image.open(("Lock.jpg")) # open image to resize it
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image = image2, anchor='nw')

    root.bind("<Configure>", resize_img)

    btn = Label(root, text='Welcome to Hybrid Encryption', bd=15, font=('Helvetica', 20, 'bold'), relief="groove",fg="white", bg="#0E3059", width=78)
    btn.place(x=5, y=3)
    #btn = Button(root, text="").pack()

    btn1 = Button(root, text='Log In', height="1", width="20", bd=10, font=('Helvetica', 12, 'bold'), relief="groove", fg="white", bg="#0E3059", command=login)
    btn1.place(x=950, y=300)

    btn1 = Button(root, text='About', height="1", width="20", bd=10, font=('Helvetica', 12, 'bold'), relief="groove", fg="white", bg="#0E3059", command=about)
    btn1.place(x=950, y=380)

    btn2 = Button(root, text='Exit', height="1", width="20", bd=10, font=('Helvetica', 12, 'bold'), relief="groove", fg="white",
           bg="#0E3059", command=Exit)
    btn2.place(x=950, y=460)
main_display()
root.mainloop()
