from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Systemss")
        self.root.geometry("1350x700+0+0")

        # #======All Images==============
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")

        self.user_icon=PhotoImage(file="images/man-user.png")
        self.user_icon=self.user_icon.subsample(50,50)

        self.pass_icon=PhotoImage(file="images/password.png")
        self.pass_icon=self.pass_icon.subsample(50,50)

        self.logo_icon=PhotoImage(file="images/logo.png")
        self.logo_icon=self.logo_icon.subsample(2,2)
        
        #==========variables==============
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack()
		

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="blue",fg="black",bd=5,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg='white')
        Login_Frame.place(x=450,y=150)

        logolbl=Label(Login_Frame,image=self.logo_icon,bg='white').grid(row=0,columnspan=3,padx=0,pady=20)

        lbluser=Label(Login_Frame,text='Username',image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=2,padx=20)

        lbluser=Label(Login_Frame,text='Password',image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",15)).grid(row=2,column=2,padx=20)


        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="green",fg="white").grid(row=3,column=2,pady=20)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are requied!!")
        elif self.uname.get()=="Akash" and self.pass_.get()=="1234":
            messagebox.showinfo("Successfull",f"Welcome {self.uname.get()}") 
        else:
            messagebox.showerror("Error","Invalid Username or Password!")


root=Tk() 
obj=Login_System(root)
root.mainloop()