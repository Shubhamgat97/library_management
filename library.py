
import datetime
from select import select
import tkinter
from cProfile import label
from msilib import Table
from msilib.schema import ComboBox, ListBox
from struct import pack
from tarfile import PAX_FIELDS
from tkinter import *
from tkinter import font, messagebox, ttk
from tokenize import Name, String

import mysql.connector
from matplotlib.pyplot import connect, text
from numpy import place
from typing_extensions import Self

from setuptools import Command


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry('1400x1200+0+0')


    #  ======================================================VARIABLES=============================================================================


        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.databorrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdate_var=StringVar()
        self.actualprice_var=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="white",fg="black", bd=12,relief=RIDGE,font=("times new roman",38,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="violet")
        frame.place(x=0,y=120,width=1530,height=675)

    #    ==============================================DATA  FRAME  LEFT========================================================================================
                                                
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="lightblue",fg="black",bd=10,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=750,height=350)

        lblMember=Label(DataFrameLeft,bg="light blue",text="Member Type:",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,state="readonly",textvariable=self.member_var,font=("arial",12,"bold"),width=12)
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.place(x=130,y=10)

        lblPRN_No=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="PRN No:",padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.prn_var,width=20)
        txtPRN_No.grid(row=1,column=1)


        lblId_No=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="ID No:",padx=2,pady=6)
        lblId_No.grid(row=2,column=0,sticky=W)
        txtId_No=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.id_var,width=20)
        txtId_No.grid(row=2,column=1)


        lblFirstName=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="First Name:",padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.firstname_var,width=20)
        txtFirstName.grid(row=3,column=1)


        lblLastName=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Last Name:",padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=20)
        txtLastName.grid(row=4,column=1)


        lblAddress1=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Address 1:",padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address1_var,width=20)
        txtAddress1.grid(row=5,column=1)


        lblAddress2=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Address 2:",padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address2_var,width=20)
        txtAddress2.grid(row=6,column=1)


        lblPostCode=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Post Code:",padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.postcode_var,width=20)
        txtPostCode.grid(row=7,column=1)


        lblMobile=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Mobile No:",padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.mobile_var,width=20)
        txtMobile.grid(row=8,column=1)


        lblBookId=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Book Id:",padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=20)
        txtBookId.grid(row=0,column=3)


        lblBookTitle=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Book Title:",padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=20)
        txtBookTitle.grid(row=1,column=3)


        lblAuthor=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Author:",padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=20)
        txtAuthor.grid(row=2,column=3)


        lblDateOfBorrowed=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Date Of Borrowed:",padx=2,pady=6)
        lblDateOfBorrowed.grid(row=3,column=2,sticky=W)
        txtDateOfBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.databorrowed_var,width=20)
        txtDateOfBorrowed.grid(row=3,column=3)


        lblDateOfDue=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Date Of Due:",padx=2,pady=6)
        lblDateOfDue.grid(row=4,column=2,sticky=W)
        txtDateOfDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=20)
        txtDateOfDue.grid(row=4,column=3)


        lblDaysOnBooks=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Days On Books:",padx=2,pady=6)
        lblDaysOnBooks.grid(row=5,column=2,sticky=W)
        txtDaysOnBooks=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=20)
        txtDaysOnBooks.grid(row=5,column=3)


        lblLateReturnFine=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Late Return Fine:",padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=20)
        txtLateReturnFine.grid(row=6,column=3)


        lblDateOverDate=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Date Over Date:",padx=2,pady=6)
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdate_var,width=20)
        txtDateOverDate.grid(row=7,column=3)


        lblActualPrice=Label(DataFrameLeft,font=("arial",10,"bold"),bg="lightblue",text="Actual Price:",padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.actualprice_var,width=20)
        txtActualPrice.grid(row=8,column=3)

     # ==============================================DATA  FRAME  RIGHT=============================================================================
        

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="lightblue",fg="black",bd=10,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=755,y=5,width=710,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",13,"bold"),width=52,height=14,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head Firt Book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python CookBook',
                                                               'Machine Techno','My Python','Joss Ellif Guru','Inton Python'
                                                               'Elite Jungel Python','Machine Python','Advance Python',
                                                               'RedChilli Python','Ishq Python','Jungli Python','Intro to Machine Learning']
        
        
        def SelectBook(event):
            valuee=str(listBox.get(listBox.curselection()))
            x=valuee
            if (x=="Head Firt Book"):
                self.bookid_var.set("BKID5050")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("C.A Chetan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.788")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID5151")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Roy P.K")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.45")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.748")

            elif (x=="Python Programming"):
                self.bookid_var.set("BKID5252")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("N.S Narayan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.799")

            elif (x=="Secrete Rahshy"):
                self.bookid_var.set("BKID5353")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("A.G Amol")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.399")

            elif (x=="Python CookBook"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("R.G Rahul")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.45")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.499")

            elif (x=="Machine Techno"):
                self.bookid_var.set("BKID5555")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("S.P Saurabh")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.599")

            elif (x=="My Python"):
                self.bookid_var.set("BKID5656")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("O.N Onkar")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.359")

            elif (x=="Joss Ellif Guru"):
                self.bookid_var.set("BKID5757")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("L.Lalit")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.450")

            elif (x=="Inton Python"):
                self.bookid_var.set("BKID5858")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("S.G ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.1200")

            elif (x=="Elite Jungel Python"):
                self.bookid_var.set("BKID5959")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Tilakh Siri")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.320")

            elif (x=="Machine Python"):
                self.bookid_var.set("BKID6060")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Pandu ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.549")

            elif (x=="Advance Python"):
                self.bookid_var.set("BKID6161")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("D.Keshav")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.629")

            elif (x=="RedChilli Python"):
                self.bookid_var.set("BKID6262")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Nitin Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.712")

            elif (x=="Ishq Python"):
                self.bookid_var.set("BKID6363")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("S.G Shubham")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.333")

            elif (x=="Jungli Python"):
                self.bookid_var.set("BKID6464")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("M.P pawan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.249")

            elif (x=="Intro to Machine Learning"):
                self.bookid_var.set("BKID6565")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Pawan.P")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.databorrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.actualprice_var.set("Rs.199")


        listBox=Listbox(DataFrameRight,font=("arial",13,"bold"),width=20,height=14)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=2)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


    # # # ===============================================BUTTON  FRAME================================================================================================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=30,bg="light green")
        Framebutton.place(x=27,y=490,width=1470,height=50)

        
        ButtonAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",10,"bold"),width=28,bg="blue",fg="white")
        ButtonAddData.grid(row=0,column=0)

        ButtonAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",10,"bold"),width=28,bg="blue",fg="white")
        ButtonAddData.grid(row=0,column=1)

        ButtonAddData=Button(Framebutton,command=self.update,text="Update Data",font=("arial",10,"bold"),width=28,bg="blue",fg="white")
        ButtonAddData.grid(row=0,column=2)

        ButtonAddData=Button(Framebutton,command=self.delete,text="Delete Data",font=("arial",10,"bold"),width=28,bg="blue",fg="white")
        ButtonAddData.grid(row=0,column=3)

        ButtonAddData=Button(Framebutton,command=self.reset,text="Reset Data",font=("arial",10,"bold"),width=28,bg="blue",fg="white")
        ButtonAddData.grid(row=0,column=4)

        ButtonAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",10,"bold"),width=28,bg="blue",fg="white")
        ButtonAddData.grid(row=0,column=5)


    # ==================================================INFORMATION  FRAME===========================================================================================================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=30,bg="light green")
        FrameDetails.place(x=30,y=542,width=1470,height=230)


        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="light yellow")
        Table_frame.place(x=0,y=2,width=1380,height=195)

        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prn no","id no","first name","last name","address 1",
                                                              "address 2","post code","mobile no","book id","book title","author",
                                                              "date of borrowed","date of due","days on books","late return fine",
                                                              "date over date","actual price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prn no",text="PRN No")
        self.library_table.heading("id no",text="ID No")
        self.library_table.heading("first name",text="First Name")
        self.library_table.heading("last name",text="Last Name")
        self.library_table.heading("address 1",text="Address 1")
        self.library_table.heading("address 2",text="Address 2")
        self.library_table.heading("post code",text="Post Code")
        self.library_table.heading("mobile no",text="Mobile No")
        self.library_table.heading("book id",text="Book Id")
        self.library_table.heading("book title",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("date of borrowed",text="Date Of Borrowed")
        self.library_table.heading("date of due",text="Date Of Due")
        self.library_table.heading("days on books",text="Days On Books")
        self.library_table.heading("late return fine",text="Late Return Fine")
        self.library_table.heading("date over date",text="Date Over Date")
        self.library_table.heading("actual price",text="Actual Price")
 
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=120)
        self.library_table.column("prn no",width=120)
        self.library_table.column("id no",width=120)
        self.library_table.column("first name",width=120)
        self.library_table.column("last name",width=120)
        self.library_table.column("address 1",width=120)
        self.library_table.column("address 2",width=120)
        self.library_table.column("post code",width=120)
        self.library_table.column("mobile no",width=120)
        self.library_table.column("book id",width=120)
        self.library_table.column("book title",width=120)
        self.library_table.column("author",width=120)
        self.library_table.column("date of borrowed",width=120)
        self.library_table.column("date of due",width=120)
        self.library_table.column("days on books",width=120)
        self.library_table.column("late return fine",width=120)
        self.library_table.column("date over date",width=120)
        self.library_table.column("actual price",width=120)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.databorrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdate_var.get(),
                                                                                                                self.actualprice_var.get()
        ))
        conn.commit()
        self.fatch_data()
        conn.close()                       

        messagebox.showinfo("Success","Member Has Been Inserted Successfully")                                                                           

        
 
    
    def update(self): 
        conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,Firstname=%s,Lastname=%s,Address1=%s,Address2=%s,Postcode=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Author=%s,Dateofborrowed=%s,Dateofdue=%s,DaysonBook=%s,Latereturnfine=%s,Dateoverdate=%s,Actualprice=%s where PRN_NO=%s",(

                                                                                                                    self.member_var.get(),
                                                                                                                    self.id_var.get(),
                                                                                                                    self.firstname_var.get(),
                                                                                                                    self.lastname_var.get(),
                                                                                                                    self.address1_var.get(),
                                                                                                                    self.address2_var.get(),
                                                                                                                    self.postcode_var.get(),
                                                                                                                    self.mobile_var.get(),
                                                                                                                    self.bookid_var.get(),
                                                                                                                    self.booktitle_var.get(),
                                                                                                                    self.author_var.get(),
                                                                                                                    self.databorrowed_var.get(),
                                                                                                                    self.datedue_var.get(),
                                                                                                                    self.daysonbook_var.get(),
                                                                                                                    self.latereturnfine_var.get(),
                                                                                                                    self.dateoverdate_var.get(),
                                                                                                                    self.actualprice_var.get(),
                                                                                                                    self.prn_var.get()
                                                                                                                ))   
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()  

        messagebox.showinfo("Success","Member has been Updated")                                                                                                  

    def fatch_data(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select  * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()        


    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

            
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.databorrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdate_var.set(row[16]),
        self.actualprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")    
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address 1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address 2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book Id:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date Of Borrowed:\t\t"+ self.databorrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date Of Due:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Days On Books:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Late Return Fine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"Date Over Date:\t\t"+ self.dateoverdate_var.get() + "\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+ self.actualprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.databorrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdate_var.set(""),
        self.actualprice_var.set("")
        self.txtBox.delete("1.0",END)
       
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":   
            messagebox.showerror("Error","First Select the Member")
        else: 
            conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="mydata")
        my_cursor=conn.cursor()
        query="delete from library where PRN_NO=%s"
        value=(self.prn_var.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()        



if __name__=="__main__":
    root=Tk()
obj=LibraryManagementSystem(root)
root.mainloop()

