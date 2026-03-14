#MAIN FUNCTION
import datetime
from prettytable import PrettyTable
import mysql.connector
conn=mysql.connector.connect(host="localhost", user="root", password="root")
cur=conn.cursor() 
cur.execute("create database if not exists shadow") 
cur.execute("use shadow")
cur.execute("create table if not exists loan(name varchar(30),loan_amt int, rate int, time int, simple_interest float, amount float )")
cur.execute("create table if not exists signup(username varchar(30),password varchar(30))")
cur.execute("insert into signup values('ashish',12345)")
conn.commit()

#OPEN BANK ACCOUNT
def openacc():
    print("\t-----—**** Please Enter Your Account No. & Branch Code ****—-----")
    bcode=input("Enter Branch CODE (SHA00) of ShadowBank:")
    acc_no=int(input("Enter your Account Number: "))
    print()
    print("\t-----—**** Please Enter Your Personal Details ****—-----")
    name=input("Please Enter FULL NAME of Account Holder: ")
    dob=input("Please Enter Date of Birth (YYYY-MM-DD) of Account Holder:")
    age=int(input("Please Enter AGE  of Account Holder:"))
    gender=input("Please Enter Gender (M/F) of Account Holder:")
    occup=input("Please Enter Occupation Type of the Account Holder:")
    income= int(input("Please Enter Monthly Income of Account Holder:"))
    print()
    print("\t-----—**** Please Enter Your Address/Contact Details ****—-----")
    address=input("Please Enter Your Permanent Address:")
    contact_no=int(input("Please Enter Your Contact Number: "))
    email=input("Please Enter Your Email Address:")
    print()
    print("\t-----—**** Proof of Identity & Verification ****—-----")
    pan_no=input("Enter PAN Card Number of Costomer:")
    print()
    print("\t-----—**** Nomination & Account Nominee's ****—-----")
    nominee=input("Enter Account Nominee of Account Holder:")
    total_balance=int(input("Enter how much BALANCE you want to Deposite: "))
    print()
    print("\t-----—**** Account Succesfully Created Date/Time****—-----")
    t_date=datetime.datetime.now()
    print("Account Succesfully Created on -", t_date)
    
    data1=(acc_no, name, dob, age, gender, occup, income, address, contact_no, email, pan_no, nominee, total_balance)
    data2=(acc_no, name, total_balance)
    
    cur.execute("create table if not exists acc (acc_no int (30) primary key, name varchar(30), dob varchar(30), \
age int(3), gender char(4), occup varchar(30), income int(30), address varchar(50), contact_no int(10),\
email varchar(30), pan_no varchar(15), nominee varchar(30),total_balance int(30))")
    cur.execute("create table if not exists amount (acc_no int(15) primary key, name varchar(30), total_balance int(30))")
    
    sql1="insert into acc values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql2="insert into amount values(%s,%s,%s)" 
    c=conn.cursor()
    cur.execute(sql1,data1)
    cur.execute(sql2,data2)
    conn.commit()
    print()
    print("\t-----—**** Data entered Successfully & Account Open ****—-----")
    print("\t___________________________________________________________________________________________________\t")


#FOR DEPOSITE AMOUNT FUNCTION
def dep():
    name=input("Please Enter your Account Holder Name: ")
    acc_no=input("Please Enter your Account Number: ")
    dep_amt=input("Please Enter how much Amount you Deposite: ")
    c=conn.cursor()
    cur.execute("update acc set total_balance=total_balance+"+dep_amt+ ' where acc_no='+acc_no+';')
    cur.execute("select total_balance from acc where acc_no="+str(acc_no))
    myresult=cur.fetchall()
    conn.commit()
    t=PrettyTable(['acc_no','name','total_balance'])
    for total_balance in myresult:
        t.add_row([acc_no, name, total_balance])
    t_date=datetime.datetime.now()
    print("Cash Deposite Succesfully on -", t_date)
    print()
    print("\t-----—**** Available Balance After Deposite ****—-----")
    print(t) 
    print("\t___________________________________________________________________________________________________\t")


# FOR WITHDRAW AMOUNT
def withdraw():
    name=input("Please Enter your Account Holder Name: ")
    acc_no=input("Please Enter your Account Number: ")
    dep_amt=input("Please Enter how much Amount you Withdraw: ")
    c=conn.cursor()
    cur.execute("update acc set total_balance=total_balance-"+dep_amt+ ' where acc_no='+acc_no+';')
    cur.execute("select total_balance from acc where acc_no="+str(acc_no))
    myresult=cur.fetchall()
    conn.commit()
    t=PrettyTable(['acc_no','name','total_balance'])
    for total_balance in myresult:
        t.add_row([acc_no, name, total_balance])
    t_date=datetime.datetime.now()
    print("Cash Withdraw Succesfully on -", t_date)
    print()
    print("\t-----—**** Available Balance After Withdraw ****—-----")
    print(t) 
    print("\t___________________________________________________________________________________________________\t")
    

# FOR BALANCE ENQUIRY
def bal_enq():
    name=input("Please Enter Account Holder Name: ")
    acc_no=int(input("Please Enter your Account Number: "))
    c=conn.cursor()
    cur.execute("select total_balance from acc where acc_no="+str(acc_no))
    myresult=cur.fetchall()
    t=PrettyTable(['acc_no','name','total_balance'])
    for total_balance in myresult:
        t.add_row([acc_no,name,total_balance])
    t_date=datetime.datetime.now()
    print("Balance Enquiry Succesfully Printed on -", t_date)
    print()
    print("\t-----—**** Balance Enquiry Successfully Printed ****—-----")
    print(t)
    print("\t___________________________________________________________________________________________________\t")


#TO KNOW CUSTOMER DETAILDS
def cust_det():
    name=input("Please Enter Account Holder Name: ")
    acc_no=int(input("Please Enter your Account Number:"))
    c=conn.cursor()
    cur.execute("select * from acc where acc_no="+str(acc_no))
    myresult=cur.fetchall()
    t=PrettyTable(['acc_no','name','dob', 'age', 'gender','occup', 'income', 'address','contact_no', 'email', 'pan_no', 'nominee', 'total_balance'])
    for acc_no, name, dob, age, gender, occup, income, address, contact_no, email, pan_no, nominee, total_balance in myresult:
        t.add_row([acc_no, name, dob, age, gender, occup, income, address, contact_no, email, pan_no, nominee, total_balance])
    t_date=datetime.datetime.now()
    print("View Customer Details on -", t_date)
    print()
    print("\t-----—**** Customers Details ****—-----")
    print(t)
    print("\t___________________________________________________________________________________________________\t")


#FOR INFORMATION UPDATE
def update():
    acc_no=input("Please Enter your Account Number: ")
    new_cont=input("Please Enter your NEW Contact no.: ")
    c=conn.cursor()
    cur.execute("update acc set contact_no="+new_cont+ ' where acc_no='+acc_no+';')
    conn.commit()
    cur.execute("select * from acc where acc_no="+str(acc_no))
    myresult=cur.fetchall()
    t=PrettyTable(['acc_no','name','dob', 'age', 'gender','occup', 'income', 'address','contact_no', 'email', 'pan_no', 'nominee', 'total_balance'])
    for acc_no, name, dob, age, gender, occup, income, address, contact_no, email, pan_no, nominee, total_balance in myresult:
        t.add_row([acc_no, name, dob, age, gender, occup, income, address, contact_no, email, pan_no, nominee, total_balance])
    t_date=datetime.datetime.now()
    print("Information Updated Succesfully on -", t_date)
    print()
    print("\t-----—**** Information Updated Successfully ****—-----")
    print(t)
    print("\t___________________________________________________________________________________________________\t")


#TO CLOSE ACCOUNT
def close():
    name=input("Please Enter Account Holder Name: ")
    acc_no=int(input("Please Enter your Account Number: "))
    contact_no=int(input("Please Enter your Contact Number: "))
    c=conn.cursor()
    cur.execute("delete from acc where acc_no="+str(acc_no))
    conn.commit()
    t_date=datetime.datetime.now()
    print("Account Deleted Succesfully on -", t_date)
    print()
    print("\t-----—**** Account Deleted/Closed Succcesfully ****—-----")
    print("\t___________________________________________________________________________________________________\t")


#TO DISPLAY ALL INFORMATION
def show():
    cur=conn.cursor()
    cur.execute("select * from acc")
    myresult=cur.fetchall()
    t=PrettyTable(['acc_no','name','dob', 'age', 'gender','occup', 'income', 'address','contact_no', 'email', 'pan_no', 'nominee', 'total_balance'])
    for acc_no, name, dob, age, gender, occup, income, address, contact_no, email, pan_no, nominee, total_balance in myresult:
        t.add_row([acc_no, name, dob, age, gender, occup, income, address, contact_no, email, pan_no, nominee, total_balance])
    t_date=datetime.datetime.now()
    print("All Information Printed Succesfully on -", t_date)
    print()
    print("\t-----—**** All Information ****—-----")
    print(t)
    print("\t___________________________________________________________________________________________________\t")


#TO TAKE A LOAN
def loan():
    print(" Press 1 for Apply Gold Loan")
    print(" Press 2 for Appy Home Loan")
    print(" Press 3 for Apply Business Loan")
    print(" Press 4 for Apply Education Loan")
    print(" Press 5 for Apply Car Loan")
    print(" Press 6 for Show All Loans")
    print(" Press Any key for EXIT ")
    ch=int(input("Select from Above All Loans : "))
    print("\t________________________________________________\t")
    if (ch==1):
        print("\t-----—**** Apply for GOLD LOAN ****—-----")
        name=input("Please Enter Your Name : ---")
        loan_amt=int(input("Please Enter Amount for Gold LOAN : "))
        rate=8
        time=int(input("Select Time for Payment--- /Year ONLY  --- "))
        simple_interest=loan_amt*rate*time/100
        amount=loan_amt + simple_interest
        cur=conn.cursor()
        
        data3=(name,loan_amt,rate,time,simple_interest,amount)
        cur.execute("create table if not exists loan (name varchar(30),loan_amt int, rate int, time int, simple_interest float, amount float )")
        sql3="insert into loan values(%s,%s,%s,%s,%s,%s)"
        
        cur.execute(sql3,data3)
        conn.commit()
        cur.execute("select*from loan")
        myresult=cur.fetchall()
        t=PrettyTable(['name','loan_amt','rate','time','simple_interest','amount'])
        for name,loan_amt,rate,time,simple_interest,amount in myresult:
            t.add_row([name,loan_amt,rate,time,simple_interest,amount])
        t_date=datetime.datetime.now()
        print("Apply for GOLD LOAN Succesfully on -", t_date)
        print()
        print("\t-----—**** Apply for GOLD LOANs ****—-----")
        print(t)
        print("\t___________________________________________________________________________________________________\t")

    elif (ch==2):
        print("\t-----—**** Apply for HOME LOAN ****—-----")
        name=input("Please Enter Your Name : ---")
        loan_amt=int(input("Please Enter Amount for Home LOAN : "))
        rate=12
        time=int(input("Select Time for Payment--- /Year ONLY  --- "))
        simple_interest=loan_amt*rate*time/100
        amount=loan_amt + simple_interest
        cur=conn.cursor()
        
        data3=(name,loan_amt,rate,time,simple_interest,amount)
        cur.execute("create table if not exists loan(name varchar(30),loan_amt int, rate int, time int, simple_interest float, amount float )")
        sql3="insert into loan values(%s,%s,%s,%s,%s,%s)"
        
        cur.execute(sql3,data3)
        conn.commit()
        cur.execute("select*from loan")
        myresult=cur.fetchall()
        t=PrettyTable(['name','loan_amt','rate','time','simple_interest','amount'])
        for name,loan_amt,rate,time,simple_interest,amount in myresult:
            t.add_row([name,loan_amt,rate,time,simple_interest,amount])
        t_date=datetime.datetime.now()
        print("Apply for HOME LOAN Succesfully on -", t_date)
        print()
        print("\t-----—**** Apply for HOME LOANs ****—-----")
        print(t)
        print("\t___________________________________________________________________________________________________\t")
            
    elif (ch==3):
        print("\t-----—**** Apply for BUSINESS LOAN ****—-----")
        name=input("Please Enter Your Name : ---")
        loan_amt=int(input("Please Enter Amount for Business LOAN : "))
        rate=15
        time=int(input("Select Time for Payment--- /Year ONLY  --- "))
        simple_interest=loan_amt*rate*time/100
        amount=loan_amt + simple_interest
        cur=conn.cursor()
        
        data3=(name,loan_amt,rate,time,simple_interest,amount)
        cur.execute("create table if not exists loan(name varchar(30),loan_amt int, rate int, time int, simple_interest float, amount float )")
        sql3="insert into loan values(%s,%s,%s,%s,%s,%s)"
        
        cur.execute(sql3,data3)
        conn.commit()
        cur.execute("select*from loan")
        myresult=cur.fetchall()
        t=PrettyTable(['name','loan_amt','rate','time','simple_interest','amount'])
        for name,loan_amt,rate,time,simple_interest,amount in myresult:
            t.add_row([name,loan_amt,rate,time,simple_interest,amount])
        t_date=datetime.datetime.now()
        print("Apply for BUSINESS LOAN Succesfully on -", t_date)
        print()
        print("\t-----—**** Apply for BUSINESS LOANs ****—-----")
        print(t)
        print("\t___________________________________________________________________________________________________\t")

    elif (ch==4):
        print("\t-----—**** Apply for EDUCATION LOAN ****—-----")
        name=input("Please Enter Your Name : ---")
        loan_amt=int(input("Please Enter Amount for Education LOAN : "))
        rate=3
        time=int(input("Select Time for Payment--- /Year ONLY  --- "))
        simple_interest=loan_amt*rate*time/100
        amount=loan_amt + simple_interest
        cur=conn.cursor()
        
        data3=(name,loan_amt,rate,time,simple_interest,amount)
        cur.execute("create table if not exists loan(name varchar(30),loan_amt int, rate int, time int, simple_interest float, amount float )")
        sql3="insert into loan values(%s,%s,%s,%s,%s,%s)"
        
        cur.execute(sql3,data3)
        conn.commit()
        cur.execute("select*from loan")
        myresult=cur.fetchall()
        t=PrettyTable(['name','loan_amt','rate','time','simple_interest','amount'])
        for name,loan_amt,rate,time,simple_interest,amount in myresult:
            t.add_row([name,loan_amt,rate,time,simple_interest,amount])
        t_date=datetime.datetime.now()
        print("Apply for EDUCATION LOAN Succesfully on -", t_date)
        print()
        print("\t-----—**** Apply for EDUCATION LOANs ****—-----")
        print(t)
        print("\t___________________________________________________________________________________________________\t")
        
    elif (ch==5):
        print("\t-----—**** Apply for CAR LOAN ****—-----")
        name=input("Please Enter Your Name : ---")
        loan_amt=int(input("Please Enter Amount for Car LOAN : "))
        rate=10
        time=int(input("Select Time for Payment--- /Year ONLY  --- "))
        simple_interest=loan_amt*rate*time/100
        amount=loan_amt + simple_interest
        cur=conn.cursor()
        
        data3=(name,loan_amt,rate,time,simple_interest,amount)
        cur.execute("create table if not exists loan(name varchar(30),loan_amt int, rate int, time int, simple_interest float, amount float )")
        sql3="insert into loan values(%s,%s,%s,%s,%s,%s)"
        
        cur.execute(sql3,data3)
        conn.commit()
        cur.execute("select*from loan")
        myresult=cur.fetchall()
        t=PrettyTable(['name','loan_amt','rate','time','simple_interest','amount'])
        for name,loan_amt,rate,time,simple_interest,amount in myresult:
            t.add_row([name,loan_amt,rate,time,simple_interest,amount])
        t_date=datetime.datetime.now()
        print("Apply for CAR LOAN Succesfully on -", t_date)
        print()
        print("\t-----—**** Apply for CAR LOANs ****—-----")
        print(t)
        print("\t___________________________________________________________________________________________________\t")
        
    elif (ch==6):
        cur=conn.cursor()
        cur.execute("select * from loan")
        myresult=cur.fetchall()
        t=PrettyTable(['name','loan_amt','rate','time','simple_interest','amount'])
        for name,loan_amt,rate,time,simple_interest,amount in myresult:
            t.add_row([name,loan_amt,rate,time,simple_interest,amount])
        t_date=datetime.datetime.now()
        print("All Information Printed Succesfully on -", t_date)
        print()
        print("\t-----—**** All Information ****—-----")
        print(t)
        print("\t___________________________________________________________________________________________________\t")
        
    elif (ch==7):
        d_rate=int(input("Please Enter yourRATE  NAME/Loan: "))
        cur=conn.cursor() 
        cur.execute("delete from loan where rate="+str(d_rate))
        conn.commit()
        t_date=datetime.datetime.now()
        print("LOAN Deleted Succesfully on -", t_date)
        print()
        print("\t-----—**** LOAN Details Deleted/Closed Succcesfully ****—-----")
        print("\t___________________________________________________________________________________________________\t")
  
    else:
        print()
        print("\t\t\t                         _____-----_____THANK YOU!_____-----_____ ")
        print("\t\t\t                                 -----_____-----HAVE A GOOD DAY !-----_____-----")
        print("\t___________________________________________________________________________________________________\t")

    
#SIGNUP/LOGIN FUNCTION
def signup(username,password):
    if username=="ashish"or username=="shadow" and password=="12345":
        print("\t\t\t*****************+++SIGNUP/LOGIN SUCCESSFULLY+++********************")
        print("\t___________________________________________________________________________________________________\t")
        while True:
            print()
            print(" Press 1 for Open NEW Account")
            print(" Press 2 for Deposite Amount ")
            print(" Press 3 for Withdraw Amount ")
            print(" Press 4 for Balance Enquiry ")
            print(" Press 5 for Customer Details ")
            print(" Press 6 for Information Updation ")
            print(" Press 7 for Close Account ")
            print(" Press 8 for to SHOW data/information ")
            print(" Press 9 for to Take a LOAN ")
            print(" Press Any key for EXIT ")
            a=int(input(" Enter Your Choice To Continue : "))
            print("\t________________________________________________\t")
            print()
            if (a==1):
                openacc()
            elif (a==2):
                dep()
            elif (a==3):
                withdraw()
            elif (a==4):
                bal_enq()
            elif (a==5):
                cust_det()
            elif (a==6):
                update()
            elif (a==7):
                close()
            elif (a==8):
                show()
            elif (a==9):
                loan()
            else:
                print("\t\t\t                         _____-----_____THANK YOU!_____-----_____ ")
                print("\t\t\t                                 -----_____-----HAVE A GOOD DAY !-----_____-----")
                break
    else:
        print("\t\t\t**************+++WRONG PASSWORD OR USERNAME !!!+++*****************")
        print("\t___________________________________________________________________________________________________\t")


#SHADOW BANK LIMITED. - BANK MAGEMENT SYSTEM
print("\t\t\t __________________________________________________________________________________________________\t")
print("\t\t\t|__________________________________________________________________________________________________|\t")
print("\t\t\t|------------------------------>>>>>TOPIC OF PROJECT : BANK MAGEMENT SYSTEM<<<<<-------------------|\t")
print("\t\t\t|--------------------------->>>>>KENDRIYA VIDYALAYA ORDNANCE FACTORY BHANDARA<<<<<-----------------|\t")
print("\t\t\t|__________________________________________________________________________________________________|\t")
print("\t\t\t|---------------------------------->>>>>MADE BY: ASHISH & BHAVESH <<<<<----------------------------|\t")
print("\t\t\t|------------------------------------->>>>>> CLASS : XII 'A' CS <<<<<------------------------------|\t")
print("\t\t\t|------------------------------>>>>>SUBMITTED TO : SWATI VISHWAKARMA<<<<<--------------------------|\t")
print("\t\t\t|__________________________________________________________________________________________________|\t")
print("\t\t\t|__________________________________________________________________________________________________|\t")
print()

username=input("@ Enter Username : ")
password=int(input("@ Enter Password : "))
signup(username,password)

#MADE BY ASHISH MESHRAM STUDENT OF (KENDRIYA VIDYALAYA ORDNANCE FACTORY BHANDARA) !!!
#2022-2023 ALL RIGHTS RESERVED. 
