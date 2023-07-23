from logging import root
from tkinter import *
from functools import partial
from tkinter import messagebox

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
def redirectregster():
    uslogin.destroy()
    import Register    

def verify():
    with open ("credential.txt") as f:
        i = 0
        new = f.readlines()
       
        for r in new:
           
            u,p = r.split(",")
            #messagebox.showinfo("invalid",u)
            #messagebox.showinfo("invalid",p)
       
            if  u.strip()==username.get() and p.strip()==password.get() :
             import disease_predictor
                         
             i = 1
             break
        if i == 0 :
            messagebox.showinfo("invalid","check password")
       
    #else:
        #messagebox.showinfo("invalid")        
           
#window
uslogin = Tk()  
uslogin.geometry('500x500')  
uslogin.title("LOG-IN")
uslogin.configure(bg="gold")

lbl1=Label(uslogin,text="LOGIN TO DISEASE PREDICATION SYSTEM",bg="gold",bd=10,font=("lucida bright",15,"bold"))
lbl1.place(x=25,y=10)

#username label and text entry box
usernameLabel = Label(uslogin, text="User Name",bg="gold", font=("Lucida Bright",13,"bold"))#.grid(row=0, column=0)
usernameLabel.place(x=50,y=100,width=100)
username = StringVar()
usernameEntry = Entry(uslogin, textvariable=username,bd=5)#.grid(row=0, column=1)
usernameEntry.place(x=200,y=100,width=200)  

#password label and password entry box
passwordLabel = Label(uslogin,text="Password",bg="gold", font=("Lucida Bright",13,"bold"))#.grid(row=1, column=0) 
passwordLabel.place(x=50,y=150,width=100)
password = StringVar()
passwordEntry = Entry(uslogin, textvariable=password, show='*',bd=5)#.grid(row=1, column=1)  
passwordEntry.place(x=200,y=150,width=200)


#validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(uslogin, text="Login", command=verify,bg="green", font=("lucida bright",12,"bold"))#.grid(row=4, column=0)  
loginButton.place(x=130,y=200,width=100)

redirectreg = Button(uslogin, text="Register", command=redirectregster,bg="red", font=("lucida bright",12,"bold"))#.grid(row=4, column=0)  
redirectreg.place(x=270,y=200,width=100)


uslogin.mainloop()