from tkinter import*
import tkinter as TK
from tkinter import messagebox

def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                         with open("credential.txt", "a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                         messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                     messagebox.showinfo("Error", "Please fill the complete field!!")
                             
def redirectlogin():
     RegisterUser.destroy()
     import login



RegisterUser = Tk()  
RegisterUser.geometry('600x500')  
RegisterUser.title('  RegisterDisease Predication System ')
RegisterUser.configure(bg="Orange")

lbl=Label(RegisterUser,text="Registration Form ",bg="sky blue",font=("Lucida Bright",20,"bold"))
lbl.place(x=180, y=10)

l1 = Label(RegisterUser, text="Username:", font=("Arial",15), bg="deep sky blue")
l1.place(x=10, y=70)
t1 = Entry(RegisterUser, width=30, bd=5)
t1.place(x = 200, y=70)
            
l2 = Label(RegisterUser, text="Password:", font=("Arial",15), bg="deep sky blue")
l2.place(x=10, y=120)
t2 = Entry(RegisterUser, width=30, show="*", bd=5)
t2.place(x = 200, y=120)
            
l3 = Label(RegisterUser, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
l3.place(x=10, y=170)
t3 = Entry(RegisterUser, width=30, show="*", bd=5)
t3.place(x = 200, y=170)

b1 = Button(RegisterUser, text="Sign in",command=check, font=("Arial",15), bg="red")
b1.place(x=170, y=250)

b2 = Button(RegisterUser, text="Log In",command=redirectlogin, font=("Arial",15), bg="green")
b2.place(x=300, y=250)


          





RegisterUser.mainloop()