from tkinter import *
import mysql.connector
from ADD import *
from DELETE import *
from ISSUE import * 
from RETURN import *
from VIEW import *
from ADD_STUDENT import *
from DELETE_STUDENT import *
from VIEW_STUDENT import *
from VIEW_ISSUED import *

db = mysql.connector.connect(host="localhost", user="root", password="shovik2004", database="library")
cursor = db.cursor()

window = Tk()
window.geometry("650x500")
window.title("SRM Central Library Management System")

greet = Label(window, font=("times new roman", 30, "bold"), fg="red", text="Welcome to SRM Central Library")
greet.grid(row=1, columnspan=3)

addbtn = Button(window, text="Add Books", command=addBooks, fg="white", font=("arial", 20, "bold"))
addbtn.grid(row=3, column=0)
addbtn.configure(bg="red", relief=FLAT)

deletebtn = Button(window, text="Delete Books", command=deleteBooks, fg="white", font=('arial', 20, 'bold'))
deletebtn.grid(row=5, column=0)
deletebtn.configure(bg="red", relief=FLAT)

issuebtn = Button(window, text="Issue Books", command=issueBooks, fg="white", font=('arial', 20, 'bold'))
issuebtn.grid(row=7, column=0)
issuebtn.configure(bg="red", relief=FLAT)

returnbtn = Button(window, text="Return Books", command=returnBooks, fg="white", font=('arial', 20, 'bold'))
returnbtn.grid(row=9, column=0)
returnbtn.configure(bg="red", relief=FLAT)

viewbtn = Button(window, text="View Books", command=viewBooks, fg="white", font=('arial', 20, 'bold'))
viewbtn.grid(row=11, column=0)
viewbtn.configure(bg="red", relief=FLAT)

addstudbtn = Button(window, text="Add Students", command=addStudents, fg="white", font=('arial', 20, 'bold'))
addstudbtn.grid(row=3, column=2)
addstudbtn.configure(bg="red", relief=FLAT)

delstudbtn = Button(window, text="Delete Students", command=deleteStudents, fg="white", font=('arial', 20, 'bold'))
delstudbtn.grid(row=5, column=2)
delstudbtn.configure(bg="red", relief=FLAT)

viewstudbtn = Button(window, text="View Students", command=viewStudents, fg="white", font=('arial', 20, 'bold'))
viewstudbtn.grid(row=7, column=2)
viewstudbtn.configure(bg="red", relief=FLAT)

viewissuedbtn = Button(window, text="View Issued Books", command=viewIssuedBooks, fg="white", font=('arial', 20, 'bold'))
viewissuedbtn.grid(row=9, column=2)
viewissuedbtn.configure(bg="red", relief=FLAT)

greet1 = Label(window, font=('arial', 15, 'bold'), fg='red', text="")
greet1.grid(row=13, columnspan=3)

greet2 = Label(window, font=('arial', 15, 'bold'), fg='red', text=" ")
greet2.grid(row=15, columnspan=3)

greet3 = Label(window, font=('arial', 15, 'bold'), fg='red', text="")
greet3.grid(row=17, columnspan=3)

greet4 = Label(window, font=('arial', 15, 'bold'), fg='red', text="Developed by : Shovik Banerjee")
greet4.grid(row=19, columnspan=3)

window.mainloop()
