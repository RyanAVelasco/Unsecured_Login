from tkinter import *
from PIL import ImageTk, Image

mainWindow = Tk()
mainWindow.title("Unsecure Login System")

# === Labels/Grid
username = Label(mainWindow, text="Username: ").grid(row=0, column=0, padx=5)
password = Label(mainWindow, text="Password: ").grid(row=1, column=0, padx=5)


# === Entry fields
usernameEntry = Entry(mainWindow, text="").grid(row=0, column=1, padx=5)
passwordEntry = Entry(mainWindow, text="").grid(row=1, column=1, padx=5)

# === Buttons
confirm = Button(mainWindow, text="Log In", command=lambda: showContents()).grid(row=2, column=1, padx=20)
cancel = Button(mainWindow, text="Cancel", command=lambda: mainWindow.quit()).grid(row=2, column=0, padx=20)

def hiddenImage():
    global hidden6
    global secret_imager

def showContents():
    global hidden
    global secret_label

    secret = Tk()
    secret.title("Hidden Archives!")


    hidden1 = Label(secret, text="39247891237359016235903126565as4ds504d684086468486e4ar")
    hidden2 = Label(secret, text="5412310441236844624468123443289144ds4f84dsaf84da80f4a4")
    hidden3 = Label(secret, text="65as4ds504d684086468486e4ar392478912373590162359031265")
    hidden4 = Label(secret, text="325614604d6s4fads4f068ds4a1392478912373590162359031265")
    hidden5 = Label(secret, text="3289144ds4f84dsaf84da80f4a465as4ds504d684086468486e4ar")

    hidden1.grid(row=0, column=0)
    hidden2.grid(row=1, column=0)
    hidden3.grid(row=2, column=0)
    hidden4.grid(row=3, column=0)
    hidden5.grid(row=4, column=0)

    secret.mainloop()
    
mainWindow.mainloop()
