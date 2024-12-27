from tkinter import *
import tkinter as tk
from tkinter import messagebox


def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def create_login_page():
    #login page 
    global pin_entry
    clear_frame()

    #title label
    title=tk.Label(root,text="ATM Machine",font=('arial',24),bg="blue",fg="white")
    title.pack(pady=20)


    #pin label and entry
    pin_label=tk.Label(root,text="Enter your PIN:",font=("times",16),bg="blue",fg="white")
    pin_label.pack(pady=10)
    pin_entry=tk.Entry (root,show="*",font=('times',16))
    pin_entry.pack(pady=10)

    #login btn
    login_button=tk.Button(root,text="Login",font =("times",16),command=verify_pin,relief="groove",bd=8,activebackground="yellow")
    login_button.pack(pady=20,side=RIGHT)

def verify_pin():#pin verification
    entered_pin=pin_entry.get()
    if entered_pin==pin:
        create_dashboard()
    else:
        messagebox.showerror("Error","invalid PIN!Please try again.")


def create_dashboard():
    #main dashboard
    clear_frame()

    
    welcome_label=tk.Label(root,text="welcome to the ATM ",font=("arial",20),bg="blue",fg="white")
    welcome_label.pack(pady=20)

    labelframe=LabelFrame(root,bd=0)
    labelframe.pack(side=RIGHT)

    frame=Frame(labelframe,bg="blue")
    frame.pack(side=RIGHT)
    #balance check btn
    balance_button=tk.Button(frame,text="check balance",font=("times",16),command=check_balance,width=25,height=2,relief="groove",bd=12,activebackground="yellow")
    balance_button.grid(row=0,column=0,pady=15)
    

    #deposit btn
    deposit_button=tk.Button(frame,text="Deposit",font=("times",16),command=deposit_money,width=25,height=2,relief="groove",bd=12,activebackground="yellow")
    deposit_button.grid(row=1,column=0,pady=15)

    #withdraw btn
    withdraw_button=tk.Button(frame,text="withdraw ",font=("times",16),command=withdraw_money,width=25,height=2,relief="groove",bd=12,activebackground="yellow")
    withdraw_button.grid(row=2,column=0,pady=15)

    #Exit btn
    exit_button=tk.Button(frame,text="Exit",font=("times",16),command=exit_atm,width=25,height=2,relief="groove",bd=12,activebackground="yellow")
    exit_button.grid(row=3,column=0,pady=15)

    
def check_balance():
    #balance checking process
    messagebox.showinfo("balance","your current balance is :{:.2f}".format(balance))

def deposit_money():
    #deposit page
    global deposit_entry
    clear_frame()

    #deposit label
    deposit_label=tk.Label(root,text="Enter deposit amount:",font=('times',16),bg="blue",fg="white")
    deposit_label.pack(pady=20)

    #deposit entry
    deposit_entry=tk.Entry(root,font=("times",16))
    deposit_entry.pack(pady=10)

    #deposit btn
    deposit_button=tk.Button(root,text="Deposit",font=("times",16),command=process_deposit,width=10,relief="groove",bd=5,activebackground="yellow")
    deposit_button.pack(pady=20,side=RIGHT)

    #back btn
    back_button=tk.Button(root,text="Back",font=("times",16),command=create_dashboard,width=10,relief="groove",bd=5,activebackground="yellow")
    back_button.pack(pady=10,side=LEFT)


def process_deposit():
    #deposit processing
    global balance
    try:
        amount=float(deposit_entry.get())
        if amount > 0:
            balance=balance+amount
            messagebox.showinfo("success","{:.2f}has been deposited".format(amount))
            create_dashboard()
        else:
            messagebox.showerror("error","enter  valid amount")

    except ValueError:
        messagebox.showerror("error","please enter a valid amount")

def withdraw_money():
    #displaying wthdw and amt
    global withdraw_entry
    clear_frame()

    #withdrae label
    withdraw_label=tk.Label(root,text="Enter withdrawal amout:",font=("times",16),bg="blue",fg="white")
    withdraw_label.pack(pady=20)

    #withdraw entry
    withdraw_entry=tk.Entry(root,font=("times",16))
    withdraw_entry.pack(pady=10)

    #withdraw btn
    withdraw_button=tk.Button(root,text="withdraw",font=("times",16),command=process_withdraw,width=10,relief="groove",bd=5,activebackground="yellow")
    withdraw_button.pack(pady=20,side=RIGHT)

    #back btn
    back_button=tk.Button(root,text="Back",font=("times",16),command=create_dashboard,width=10,relief="groove",bd=5,activebackground="yellow")
    back_button.pack(pady=10,side=LEFT)
def process_withdraw():
    #withdraw processing
    global balance
    try:
        amount=float(withdraw_entry.get())
        if amount>0 and amount<=balance:
            balance-=amount
            messagebox.showinfo("success","{:.2f} has been withdraw".format(amount))
            create_dashboard()
        elif amount>balance:
            messagebox.showerror("error","insufficient balance")
        else:
            messagebox,showerror("error","enter a valid amount")
    except:
        messagebox.showerror("error","please enter a valid number")
    

def exit_atm():
    root.destroy()


#main 
root=tk.Tk()
root.title("ATM Machine")
root.geometry("500x600")
root.config(bg="blue")


pin="1234"
balance=1000.0
pin_entry=None
deposit_entry=None
withdraw_entry=None


create_login_page()


root.mainloop()                  
