from tkinter import *
home=Tk()
home.title('home')
login=Tk()
Signup=Tk()
bgg="#488bc4"
fgg="white"
home.configure(bg=bgg)
home.attributes("-fullscreen",True)

def save():
    data=e1.get()+"\n"+e2.get()+"\n"+e3.get()+"\n"+e4.get()+"\n"+e5.get()+e6.get()+"\n"+e7.get()+"\n"+e8.get()+"\n"+e9.get()+"\n"+e10.get()
    with open("FBdetails.txt",'w')as f:
        f.writelines(data)

def loginn():
    login=Tk()
    login.configure(bg=bgg)
    login.attributes("-fullscreen",True)
    


    title11=Label(login,text="Facebook Login Page",font=('arial 50 bold'),bg=bgg,fg=fgg,pady=40,padx=400)
    title11.grid(columnspan=4)

    email=Label(login,text="Email id",font=('arial 30 bold'),bg=bgg,fg=fgg,padx=10,pady=10)
    email.grid(row=3,column=0)

    e11=Entry(login,bd=5,relief=GROOVE,width=40)
    e11.grid(row=3,column=1)

    password=Label(login,text="Pasword",font=('arial 30 bold'),bg=bgg,fg=fgg,padx=10,pady=10)
    password.grid(row=4,column=0)

    e22=Entry(login,bd=5,relief=GROOVE,width=40)
    e22.grid(row=4,column=1)

    keep=Checkbutton(login,text="Keep me login",font=('arial 20 bold'),bg=bgg,fg=fgg,padx=10,pady=10)
    keep.grid(row=5,column=1)

    signup=Button(login,text="Sign-Up",font=('times 20 bold'),bg='light green',command=Sign_up,fg='black',padx=40,pady=10)
    signup.grid(row=6,column=0)
    Login=Button(login,text="Login",font=('times 20 bold'),bg='light green',command=loginn,fg='black',padx=40,pady=10)
    Login.grid(row=6,column=1)
    Exit=Button(login,text="Clear All",font=('times 20 bold'),bg='#ff2d1e',command=login.destroy,fg='black',padx=40,pady=10)
    Exit.grid(row=6,column=2)

def Sign_up():
    Signup=Tk()
    Signup.configure(bg=bgg)
    Signup.attributes("-fullscreen",True)
    title22=Label(Signup,text="Facebook SignUp Page",font=('times 40 bold'),bg=bgg,fg=fgg,pady=40,padx=400)
    title22.grid(columnspan=4)
    
    def save():
        data="First Name :"+e1.get()+"\n"+"Last Name :"+e2.get()+"\n"+"Email :"+e3.get()+"\n"+"Password :"+e4.get()+"\n"+"Again Password :"+e5.get()+"\n"+"Mobile No :"+e6.get()+"\n"+"Gender: "+e7.get()+"\n"+"Date Of Birth :"+e8.get()+"\n"+"Country :"+e9.get()+"\n"+"City :"+e10.get()
        with open("FBdetails.txt",'w')as f:
            f.writelines(data)


    fname=Label(Signup,text="First Name",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    fname.grid(row=1,column=0)

    e1=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e1.grid(row=1,column=1)

    lname=Label(Signup,text="Last Name",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    lname.grid(row=2,column =0)

    e2=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e2.grid(row=2,column=1)

    email=Label(Signup,text="Email",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    email.grid(row=3,column=0)

    e3=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e3.grid(row=3, column=1)

    password=Label(Signup,text="Password",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    password.grid(row=4,column=0)

    e4=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e4.grid(row=4,column=1)

    apassword=Label(Signup,text="Again Password",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    apassword.grid(row=5,column=0)

    e5=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e5.grid(row=5,column=1)

    mobnumber=Label(Signup,text="Mobile Number",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    mobnumber.grid(row=6,column=0)

    e6=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e6.grid(row=6,column=1)

    gender=Label(Signup,text="Gender",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    gender.grid(row=7,column=0)

    e7=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e7.grid(row=7,column=1)

    DOB=Label(Signup,text="Date Of Birth",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    DOB.grid(row=8,column=0)

    e8=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e8.grid(row=8,column=1)

    country=Label(Signup,text="Country",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    country.grid(row=9,column=0)

    e9=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e9.grid(row=9,column=1)

    city=Label(Signup,text="City",font=('times 20 bold'),bg=bgg,fg=fgg,padx=40,pady=10)
    city.grid(row=10,column=0)

    e10=Entry(Signup,bd=5,relief=GROOVE,width=40)
    e10.grid(row=10,column=1)

    signup=Button(Signup,text="SignUp",font='times 20 bold',bg=fgg,fg='black',padx=40,pady=10)
    signup.grid(row=11,column=0)

    login=Button(Signup,text="Login",font=('times 20 bold'),command=save,bg=fgg,fg='black',padx=40,pady=10)
    login.grid(row=11,column=1)
    
    
    
    Clear=Button(Signup,text="Clear All",font=('times 20 bold'),command=Signup.destroy,bg=fgg,fg='black',padx=40,pady=10)
    Clear.grid(row=11,column=2)

    


title=Label(home,text="Facebook",font=('arial 100 bold'),bg=bgg,fg=fgg,pady=40,padx=400)
title.grid(columnspan=4)
title1=Label(home,text="Facebook helps you connect and share with the people in your life.",font=('arial 20 bold'),bg=bgg,fg=fgg,pady=10,padx=100)
title1.grid(columnspan=4)

Select=Label(home,text="Please Select Operation",font=('arial 40 bold'),bg=bgg,fg=fgg,padx=100,pady=10)
Select.grid(columnspan=4)

signup=Button(home,text="Sign-Up",font=('times 30 bold'),bg='light green',command=Sign_up,fg=fgg,padx=40,pady=10)
signup.grid(row=3,column=0)

Login=Button(home,text="Login",font=('times 30 bold'),bg='light green',command=loginn,fg=fgg,padx=40,pady=10)
Login.grid(row=3,column=1)

Exit=Button(home,text="Exit",font=('times 30 bold'),bg='red',command=home.destroy,fg=fgg,padx=40,pady=10)
Exit.grid(row=3,column=2)


home.mainloop()
