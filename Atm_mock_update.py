import random
from datetime import datetime
import time
now = datetime.today()
date = now.strftime("%A %B %d, %Y")
time = now.strftime("%I:%m %p")
import sys

database = {}

def welcome_page():
  print(f"\n\t****** WELCOME TO BANK PY ******\n\n{date}\t\t{time}\n")
  while True:
    try:
      options = int(input("""\t*Please Select an Option*\n
1. Exiting User(sign-in)\n
2. New User(sign-up)\n"""))
      if options == 1:
        login()
        break
      elif options ==2:
        signup()
        break
      else:
        print("Invalid option.\nPlease try again\n")
        continue
    except ValueError:
      print("invalid input\nPlease try again\n")


def login():
  print("\n******** LOGIN ********")
  account_nou = input("Account no : ")
  
  if ((account_nou in database)):
    password = (input("Password : "))
    if (password == database[account_nou][5]):
      
      print("Please wait...")
      banking_op(account_nou)
    else:
      print("user not found")
      login()
  else:
    print("invalid account number")
    login()

def signup():
  print("\t****** CREATE ACCOUNT ******")
  last_name = input("\nLast Name : ")
  first_name = input("\nFirst Name : ")
  while True:
    email = input("\nEmail : ")
    if (".com" and "@" not in email):
      print("Invalid Email address\nPlease enter a vaild Email address")
      continue
    else:
      break
  account_balance = 450
  while True:
    try:
      pin = int(input("\nCreate Pin : "))
      if pin in range(0000,9999):
        break
      else:
        print("Please select a four digit pin")
        continue
    except ValueError:
      print("invalid input")

  while True:
    password = input("\nCreate Password : ")
    confirm_password = input("\nConfirm Password : ")

    if (password == confirm_password):
      account_no = str(generate_account())
      database[account_no]=[last_name, first_name, email, account_balance, pin, password]

      
      print("\t\nYour registration was successful")
      print(f"Your Account number: {account_no}")
      print("Please wait....\n")
   
      print("Please Login")
      login()

      break
    else:
      print("Password do not match")
      continue
  
def generate_account():
  return random.randrange(00000000,99999999)

def banking_op(user):
  last_name = database[user][0]
  first_name = database[user][1]
  
  print(f"\t\nWelcome, {last_name} {first_name}\n\t{date} {time}")
  print("""
  \tPlease Select an Option\n
  1. Account Balance
  2. Withdraw
  3. Deposit
  4. Statement Request
  5. Exit""")
  options = int(input("\nSelect Option : "))
  if options == 1:
    account_balance(user)
  if options == 2:
    withdraw(user)
  if options == 3:
    deposit(user)
  if options == 4:
    Statement(user)
  if options == 5:
    exit()

def account_balance(user):
  while True:
    try:
      print("\n*****Account Balance****** ")
      print("$",database[user][3])
      print("Press 1 to return to previous menu")
      print("Press 2 to exit")
      select = int(input("\n"))
      if select==1:
        banking_op(user)
        break

      elif select==2:
        welcome_page()
        break
      else:
        print("""
        invalid selecton
        Try again""")
        continue
    except ValueError:
      print("\nInvalid input, Try again")



def withdraw(user):
  print("\n******Cash Withdrawal******\n")
  amount = int(input("Amount : $"))
  if amount <= database[user][3]:
    while True:
      userpin = int(input("Transaction Pin : "))
      if userpin == database[user][4]:
        break
        print("\nTransaction was Successful")
        database[user][3] = database[user][3]-amount
        print("....")
        print(f"Your Balance : ${database[user][3]}")
        print("""
        Press
        1. Perform another Transaction
        2. Exit""")
        bal=int(input("Select an option : "))
        if bal==1:
          banking_op(user)
        elif bal==2:
          welcome_page()
        else:
          print("invalid selection")
          login()

      else:
        print("Invalid pin")
        continue
  else:
    print("Insufficiet Funds")
    banking_op(user)


def deposit(user):
  print("\n******Deposit******")
  amount=int(input("Amount : $"))
  acc_no = input("Account Number : ")
  if (acc_no in database):
    print("Successful...")
    database[user][3] += amount
    print(f"\nYou deposited ${amount}\nYour Balance is ${database[user][3]}")
    print("""
        Press
        1. Perform another Transaction
        2. Exit""")
    bal=int(input("Select an option : "))
    if bal==1:
      banking_op(user)
    elif bal==2:
      welcome_page()
    else:
      print("invalid selection")
      login()
  else:
    print("incorrect account number")
    deposit(user)

def Statement(user):
  print("\n\tStatement Request ")
  request = input("\nPlease enter Account Number: ")
  print(f"\nYour Account Statement will be sent to {database[user][2]}")
  select = int(input("Press 1 to confirm, 2 to return to previous menu : "))
  if select==1:
    print("\n\tThank you for Banking with us...")
    sys.exit()
  elif select==2:
    banking_op(user)
  else:
    print("Invalid option")
    Statement(user)

def exit():
  print("Have a Good Day")
  sys.exit    

welcome_page()