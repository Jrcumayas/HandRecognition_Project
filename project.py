from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Expressy Login')
root.geometry('925x500+300+200')
root.configure(bg = "#fff")
root.resizable(False, False)

# Functions
def handleTextBox(event):
    textBox = event.widget
    if (textBox == username):
        if event.type == "9": # <FocusIn> event
            if textBox.get() == 'Username':
                textBox.delete(0, 'end')
                textBox.config(show = '')
        elif event.type == "10": # <FocusOut> event
            if textBox.get() == '':
                textBox.insert(0, 'Username')
    elif (textBox == password):
        if event.type == "9": # <FocusIn> event
            if textBox.get() == 'Password':
                textBox.delete(0, 'end')
                textBox.config(show='*')
        elif event.type == "10": # <FocusOut> event
            if textBox.get() == '':
                textBox.insert(0, 'Password')
                textBox.config(show='')

def signin():
    userText = username.get()
    passText = password.get()

    if (userText != 'admin' and passText != 'password'):
        messagebox.showerror("Login failed", "Invalid username and password.")
    elif (userText == 'admin' and passText == 'password'):
        displayHomeScreen()

def displayHomeScreen():
    homeScreen = Toplevel(root)
    homeScreen.title = ("App")
    homeScreen.geometry('925x500+300+200')
    homeScreen.config(bg = 'white')
    homeScreen.resizable(False, False)

    Label(homeScreen, text = 'Hello nice kaayo', bg = "#fff", font = ('Calibri(Body)', 50, 'bold')).pack(expand = True)

    homeScreen.mainloop()

# Main Login Screen with background image
background_image = PhotoImage(file = "C:\\Users\\jerick royce\\Documents\\Programming\\Python\\opencv journey\\OpenCV_Project\\images\\Expressy.png")
Label(root, image = background_image, bg = 'white').place(x = 1, y = 1)

# Login frame with Username and Password

frame = Frame(root, width = 350, height = 350, bg = "white")
frame.place(x = 520, y = 70)

heading = Label(frame, text = 'Sign in', fg = '#57a1f8', bg = 'white', font = ('Arial', 25, 'bold'))
heading.place(x = 125, y = 20)

# Username textbox
username = Entry(frame, width = 25, fg = 'black', border = 0, bg = 'white', font = ('Arial', 12))
username.place(x = 30, y = 100)
username.insert(0, 'Username')
username.bind('<FocusIn>', handleTextBox)
username.bind('<FocusOut>', handleTextBox)

Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 130)

# Password textbox
password = Entry(frame, width = 25, fg = 'black', border = 0, bg = 'white', font = ('Arial', 12))
password.place(x = 30, y = 170)
password.insert(0, 'Password')
password.bind('<FocusIn>', handleTextBox)
password.bind('<FocusOut>', handleTextBox)

Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 200)

# Forgot password
fpassword = Button(frame, width = 25, text = 'Forgot your password?', border = 0, bg = 'white', cursor = 'hand2', fg = '#57a1f8', font = ('Arial', 9))
fpassword.place(x = 165, y = 210)

# Login button
Button(frame, width = 41, pady = 7, text = 'Login', bg = '#57a1f8', fg = 'white', border = 0, command = signin).place(x = 29, y = 240)

label = Label(frame, text = "Don't have an account?", fg = 'black', bg = 'white', font = ('Arial', 9))
label.place(x = 75, y = 300)

# Sign up button
sign_up = Button(frame, width = 6, text = 'Sign up', border = 0, bg = 'white', cursor = 'hand2', fg = '#57a1f8', font = ('Arial', 9))
sign_up.place(x = 210, y = 300)

################################

root.mainloop()