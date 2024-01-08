name = input("what is your name? ")
account_number = input("what is your account number? ")
bank_name = input("what is your bank name? ")
balance = 0
#send_receive = input("do you want to send or add money? ")
amount1 = input("how much are you sending? ")
amount2 = input("if you are adding money to your wallet, how much? ")
receiver_account_number = input("what is the receiver's account number? ")
receiver_bank_name = input("what is receiver's bank name? ")

amount = int(amount1)
new = int(amount2)
receiver = int(receiver_account_number)
new_balance = balance + new
new2 = new_balance - amount

def add_money():
 new_balance = balance + new
 print("you have successfully added " + str(new) + " to your wallet")

add_money()
def send_money():
 #(name, send_receive, amount, receiver_account, receiver_bank, new):
 if new >= amount:
    new2 = new_balance - amount
    print("you have successfully sent " + str(amount) + " to " + receiver_account_number + " " + receiver_bank_name + " thanks")
    print("your new balance is " + str(new2))
send_money()