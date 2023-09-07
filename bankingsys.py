import random

class Account:
    def __init__(self, acc_no, branch, balance):
        self.acc_no = acc_no
        self.branch = branch
        self.balance = balance
      

    def transaction(self, amount, from_, to_):
        if(self.balance >= amount):
            if(amount >= 1):
                self.balance = self.balance - amount
                print(f"Rs.{amount}/- sent to Acc No. {to_.acc_no}")

                to_.balance += amount
                print(f"Rs.{amount}/- recieved from Acc No. {from_.acc_no}")
                print("Transaction Successfull!")
            else:
                print("Minimum limit for transaction is Rs. 1.00 /-")

        elif(self.balance < amount):
            print("Insufficient Funds!")

            

    def showBalance(self):
        print(f'\nAcc No : {self.acc_no}')
        print(f"Your Balance : {self.balance}\n")



accounts = {}


while(1):
    print("\n\n**** MENU ****")
    print("1) Send Money.")
    print("2) Show Balance.")
    print("3) Open Acc : ")
    print("4) Exit Application.")
    print("-"*20)

    operation = int(input("Select Operation to be performed : "))
    if(operation == 1):
        SAcc = int(input("Enter sender's acc no : "))
        RAcc = int(input("Enter recipent's acc no : "))
        amt = float(input("\nEnter amount : "))
        accounts[SAcc].transaction(amt, accounts[SAcc], accounts[RAcc])
    
    elif(operation == 2):
        acc = int(input("Enter your acc no : "))
        accounts[acc].showBalance()
    
    elif(operation == 3):
        accno = random.randint(100, 999)
        print(f"Assigned ACC NO : {accno}")
        branch = input("Enter branch of bank : ")
        blc = float(input("Enter your acc balance : "))
        accounts[accno] = Account(accno, branch, blc)
    
    else:
        print("Thank you for using Banking System!")
        break
