from tkinter import*
root=Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")
Label(root, text="Login Form", font="arial 15 bold").grid(row=0, column=3)

name= Label(root, text="name")
Lastname= Label(root, text="LastName")
Emailid=  Label(root, text="Emailid")
Password= Label(root, text="Password")

name.grid(row=1, column=2)
Lastname.grid(row=2, column=2)
Emailid.grid(row=3, column=2)
Password.grid(row=4, column=2)

namevalue=StringVar
Lastnamevalue=StringVar
Emailidvalue=StringVar
Passwordvalue=StringVar
checkvalue=IntVar

nameentry= Entry(root, textvariable =namevalue)
Lastnameentry=  Entry(root, textvariable =Lastnamevalue)
Emailidentry= Entry(root, textvariable =Emailidvalue)
Passwordentry=Entry(root, textvariable =Passwordvalue)

nameentry.grid(row=1, column=3)
Lastnameentry.grid(row=2, column=3)
Emailidentry.grid(row=3, column=3)
Passwordentry.grid(row=4, column=3)

checkbtn=Checkbutton(text="remember me?",variable= checkvalue)
checkbtn.grid(row=5,column=2)
Button(text="Submit",command=getvals).grid(row=6,column=2)
root.mainloop()
