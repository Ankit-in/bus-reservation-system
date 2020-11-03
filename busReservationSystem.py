import tkinter
from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk #pip install pillow
import mysql.connector
def search_data():
    lbl1=entry.get()
    lbl2=entry1.get()
    lbl3=entry2.get()

    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ankit@77",database="BusR")
    mycursor=mydb.cursor()

    mycursor.execute("select * from students where"+str(lbl1)+str(lbl2)+str(lbl3))
    rows=mycursor.fetchall()
    if len(row)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',END,values=rows)
        mydb.commit()
    mydb.close()

    entry.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
def register_user():

    lbl4=entry3.get()
    lbl5=entry4.get()
    lbl6=entry5.get()
    lbl7=entry6.get()
    lbl8=entry7.get()
    lbl9=entry8.get()


    if(lbl4=="" or lbl5=="" or lbl6=="" or lbl6=="" or lbl7=="" or lbl8==""):
        messagebox.showerror("Error","All Fields are Required",parent=screen1)
    elif lbl8!=lbl9:
        messagebox.showerror("Error", "password & confrimpassword should be same",parent=screen1)
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Ankit@77", database="Ankit2")
        mycursor = mydb.cursor()
        # mycursor.execute("create database Ankit2")
        # mycursor.execute("show databases")
        # for db in mycursor:
        # print(db)
        mycursor.execute("create table ABC(fname varchar(45),lname varchar(45),contact varchar(45),email varchar(45),password varchar(45))")
        mycursor.execute("insert into ABC values('"+ lbl4 +"','"+ lbl5 +"','"+ lbl6 +"','"+ lbl7 +"','"+ lbl8 +"')")
        mydb.commit()
        messagebox.showinfo("Success", "Register Successful", parent=screen1)
        mydb.close()


        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        entry8.delete(0, END)



def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("1024x790")
    screen1.resizable(False,False)

    global fname
    global lname
    global contact
    global email
    global password
    global confirmpassword
    global entry3
    global entry4
    global entry5
    global entry6
    global entry7
    global entry8
    global lbl4
    global lbl5
    global lbl6
    global lbl7
    global lbl8
    global lbl9
    fname=StringVar()
    lname=StringVar()
    contact=StringVar()
    email=StringVar()
    password=StringVar()
    confirmpassword=StringVar()


    #--------image_connection------
    screen1.bg=ImageTk.PhotoImage(file="/Users/sonusingh/Downloads/BusLog.jpeg")
    screen1.bg_image=Label(screen1,image=screen1.bg).place(x=0,y=100,width=1024,height=700)
    #-----------frame----------
    frm3=Frame(screen1,bg="light blue")
    frm3.place(x=0,y=0,height=150,width=1024)
    title4=Label(frm3,text="BUS RESERVATION SYSTEM",font=("impact",60,"bold"), fg="red",bg="light blue",bd=10,relief=GROOVE).place(x=50, y=40)
    frm4=Frame(screen1,bg="light blue")
    frm4.place(x=100,y=240,height=430,width=700)
    title5=Label(frm4,text="BUS RESERVATION SYSTEM",font=("impact",35,"bold"),fg="#d25d17",bg="light blue").pack()
    title6=Label(frm4, text="REGISTER HERE", font=("impact", 40, "bold"), fg="#d25d17",bg="light blue").pack()
    lbl4=Label(frm4,text="FirstName", font=("Goudy old style",18, "bold"), fg="black", bg="light blue").place(x=60,y=130)
    entry3=Entry(frm4,font=("times of roman",18),bg="light gray")
    entry3.place(x=60,y=155,width=250,height=35)
    lbl5=Label(frm4,text="LastName",font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=400,y=130)
    entry4=Entry(frm4,font=("times of roman", 18), bg="light gray")
    entry4.place(x=400, y=155, width=250, height=35)
    lbl6=Label(frm4, text="Contact", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60,y=200)
    entry5=Entry(frm4, font=("times new roman", 18), bg="light gray")
    entry5.place(x=60, y=225, width=250, height=35)
    lbl7=Label(frm4, text="Email", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=400,y=200)
    entry6=Entry(frm4, font=("times new roman", 18), bg="light gray")
    entry6.place(x=400, y=225, width=250, height=35)
    lbl8=Label(frm4, text="password", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60,y=270)
    entry7=Entry(frm4, font=("times new roman", 18), bg="light gray")
    entry7.place(x=60, y=295, width=250, height=35)
    lbl9=Label(frm4, text="ConfirmPassword", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=400,y=270)
    entry8=Entry(frm4, font=("times new roman", 18), bg="light gray")
    entry8.place(x=400, y=295, width=250, height=35)
    #--------------button-----------
    chk=Checkbutton(frm4, text="I Agree The Terms & Conditon",onvalue=1,offvalue=0, font=("Goudy old style", 12),cursor="hand2",bg="light blue").place(x=60,y=340)
    btn6=Button(screen1,text="Register",fg="#d25d17",font=("times new roman",25,"bold"),command=register_user,cursor="hand2")
    btn6.place(x=158,y=620,width=190,height=40)
    btn7=Button(screen1, text="Already have an account?Login", fg="red", font=("times new roman", 15),command=login, cursor="hand2")
    btn7.place(x=500, y=620, width=205, height=40)
def booking_user():

        lbl12 = entry11.get()
        lbl13 = entry12.get()
        lbl14 = entry13.get()


        if (lbl12 == "" or lbl13 == "" or lbl14 == ""):
            messagebox.showerror("Error", "All Fields are Required", parent=screen3)
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Ankit@77",database="booking")
            mycursor = mydb.cursor()
            #mycursor.execute("create database booking")
            #mycursor.execute("show databases")
            #for db in mycursor:
                #print(db)
            mycursor.execute("create table Em(name varchar(45),busid varchar(45),age varchar(45))")
            mycursor.execute("insert into Em values('"+ lbl12 +"','"+ lbl13 +"','"+ lbl14 +"')")
            mydb.commit()
            messagebox.showinfo("Success", "Booked Successful", parent=screen3)
            mydb.close()

            entry11.delete(0, END)
            entry12.delete(0, END)
            entry13.delete(0, END)



def booking():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("Booking")
    screen3.geometry("1500x769")
    screen3.resizable(False, False)

    global lbl12
    global lbl13
    global lbl14
    global entry11
    global entry12
    global entry13
    global name
    global busID
    global age
    name=StringVar()
    busid=StringVar()
    age=StringVar()

    # ---------------Image connection---------------
    screen3.bg = ImageTk.PhotoImage(file="/Users/sonusingh/Downloads/busGUI.jpg")
    screen3.bg_image = Label(screen3,image=screen.bg).place(x=0,y=0)
    # --------------add frame-------------
    frm7 = Frame(screen3, bg="light blue")
    frm7.place(x=0, y=0, height=150, width=1500)
    title10 = Label(frm7, text="BUS RESERVATION SYSTEM", font=("impact", 60, "bold"), fg="red", bg="light blue", bd=10,relief=GROOVE).place(x=50, y=40)
    frm8 = Frame(screen3, bg="light blue")
    frm8.place(x=100, y=240, height=420, width=500)
    title11 = Label(frm8, text="BUS RESERVATION SYSTEM", font=("impact", 35, "bold"), fg="#d25d17",bg="light blue").place(x=70, y=50)
    title12 = Label(frm8, text="Booking Area", font=("impact", 40, "bold"), fg="#d25d17", bg="light blue").pack()
    lbl12 = Label(frm8, text="Name", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60,y=130)
    entry11 = Entry(frm8, font=("times of roman", 18), bg="light gray")
    entry11.place(x=60, y=155, width=350, height=35)
    lbl13 = Label(frm8, text="BusID", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60,y=195)
    entry12 = Entry(frm8, font=("times of roman", 18), bg="light gray")
    entry12.place(x=60, y=220, width=350, height=35)
    lbl14 = Label(frm8, text="Age", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60,y=260)
    entry13 = Entry(frm8, font=("times new roman", 18), bg="light gray")
    entry13.place(x=60, y=285, width=200, height=35)
    # --------button----------
    btn10 = Button(screen3, text="Book", fg="#d25d17", font=("times new roman", 25, "bold"), command=booking_user,cursor="hand2")
    btn10.place(x=400, y=570, width=180, height=40)
def login_user():

    lbl10=entry9.get()
    lbl11=entry10.get()


    if (lbl10=="" or lbl11=="" ):
        messagebox.showerror("Error", "All Fields are Required",parent=screen2)
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Ankit@77", database="Ankit2")
        mycursor = mydb.cursor()
        mycursor.execute(" select * from AA where email=%s and password=%s ",lbl10,lbl11)
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=screen2)
        else:
            messagebox.showinfo("Success","Welcome",Parent=screen2)



def login():
    global screen2
    screen2= Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("1024x790")
    screen2.resizable(False, False)

    global entry9
    global entry10
    global lbl10
    global lbl11
    global usernamelogin
    global passwordlogin
    usernamelogin=StringVar()
    passwordlogin=StringVar()

    #---------image_connection for login----------
    screen2.bg=ImageTk.PhotoImage(file="/Users/sonusingh/Downloads/BusLog.jpeg")
    screen2.bg_image=Label(screen2,image=screen2.bg).place(x=0, y=100, width=1024, height=700)
    #-----------frame for bouder--------------
    frm5=Frame(screen2,bg="light blue")
    frm5.place(x=0,y=0,height=150,width=1024)
    title7=Label(frm5,text="BUS RESERVATION SYSTEM",font=("impact",60,"bold"),fg="red",bg="light blue",bd=10,relief=GROOVE).place(x=50,y=40)
    frm6= Frame(screen2, bg="light blue")
    frm6.place(x=400,y=280,height=340,width=500)
    title8=Label(frm6,text="BUS RESERVATION SYSTEM", font=("impact", 35, "bold"), fg="#d25d17",bg="light blue").pack()
    title9=Label(frm6,text="LOGIN HERE",font=("impact",40,"bold"),fg="#d25d17",bg="light blue").pack()
    lbl10= Label(frm6,text="Username",font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60,y=130)
    entry9=Entry(frm6,font=("times of roman",18),bg="light gray")
    entry9.place(x=60,y=155,width=350,height=35)
    lbl11=Label(frm6,text="Password",font=("Goudy old style",18,"bold"),fg="black",bg="light blue").place(x=60, y=195)
    entry10=Entry(frm6,font=("times of roman",18),bg="light gray")
    entry10.place(x=60,y=220,width=350,height=35)
    #----------------button-------------
    btn8=Button(screen2, text="Login",fg="#d25d17", font=("times new roman", 25, "bold"),command=login_user, cursor="hand2")
    btn8.place(x=570,y=600,width=180,height=40)
    btn9=Button(screen2, text="New to this?Create account",bd=0, fg="red", font=("times new roman",15),command=register, cursor="hand2")
    btn9.place(x=460,y=550,width=180,height=40)
def main_screen():
    global screen
    screen=Tk()
    screen.title("BUS")
    screen.geometry("1500x769")
    screen.resizable(False,False)

    global From
    global To
    global Date
    global lbl1
    global lbl2
    global lbl3
    global entry
    global entry1
    global entry2
    global student_table
    From=StringVar()
    To=StringVar()
    Date=StringVar()

    #---------------Image connection---------------
    screen.bg=ImageTk.PhotoImage(file="/Users/sonusingh/Downloads/busGUI.jpg")
    screen.bg_image=Label(screen,image=screen.bg).place(x=0,y=0)
    #--------------add frame-------------
    frm1=Frame(screen,bg="light blue")
    frm1.place(x=0,y=0,height=150,width=1500)
    title1=Label(frm1,text="BUS RESERVATION SYSTEM",font=("impact",60,"bold"), fg="red",bg="light blue",bd=10,relief=GROOVE).place(x=50, y=40)
    frm2=Frame(screen,bg="light blue")
    frm2.place(x=100,y=240,height=420,width=500)
    title2=Label(frm2,text="BUS RESERVATION SYSTEM",font=("impact",35,"bold"),fg="#d25d17",bg="light blue").place(x=70,y=50)
    title3=Label(frm2, text="MY WAY", font=("impact", 40, "bold"), fg="#d25d17",bg="light blue").pack()
    lbl1=Label(frm2,text="From", font=("Goudy old style",18, "bold"), fg="black", bg="light blue").place(x=60,y=130)
    entry=Entry(frm2,font=("times of roman",18),bg="light gray")
    entry.place(x=60,y=155,width=350,height=35)
    lbl2=Label(frm2,text="To",font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60, y=195)
    entry1=Entry(frm2,font=("times of roman", 18), bg="light gray")
    entry1.place(x=60, y=220, width=350, height=35)
    lbl3=Label(frm2, text="Date", font=("Goudy old style", 18, "bold"), fg="black", bg="light blue").place(x=60,y=260)
    entry2=Entry(frm2, font=("times new roman", 18), bg="light gray")
    entry2.place(x=60, y=285, width=200, height=35)
    #--------button----------
    btn1=Button(screen,text="Search",fg="#d25d17",font=("times new roman",25,"bold"),command=search_data,cursor="hand2")
    btn1.place(x=400,y=570,width=180,height=40)
    btn3=Button(screen,text="login",fg="red",width=10,height=2,font=("times new roman",18,"bold"),command=login,cursor="hand2").place(x=1200,y=100)
    btn4=Button(screen,text="register",fg="red",width=10,height=2,font=("times new roman",18,"bold"),command=register,cursor="hand2").place(x=1300,y=100)
    btn5=Button(screen,text="Book",fg="#d25d17",width=10,height=2,font=("time new roman",25,"bold"),command=booking,cursor="hand2").place(x=1250,y=570,width=130,height=40)
    #----------Table_Frame-------
    Table_frame=Frame(screen,bd=4,relief=RIDGE,bg="crimson")
    Table_frame.place(x=700,y=230,width=550,height=450)

    scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
    student_table=ttk.Treeview(Table_frame,columns=("bus","from","to","date","time","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)
    student_table.heading("bus",text="BusID")
    student_table.heading("from",text="From")
    student_table.heading("to",text="To")
    student_table.heading("date",text="Date")
    student_table.heading("time",text="Time")
    student_table.heading("price",text="Price")
    student_table['show']='headings'
    student_table.column("bus",width=40)
    student_table.column("from",width=120)
    student_table.column("to",width=120)
    student_table.column("date",width=100)
    student_table.column("time",width=80)
    student_table.column("price",width=80)
    student_table.pack(fill=BOTH,expand=1)

    screen.mainloop()

main_screen()
