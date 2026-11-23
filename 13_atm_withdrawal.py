# Demo ATM: example PIN and transaction rules
correct_pin = "1234"
pin = input("Enter PIN: ")
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if pin != correct_pin:
    print("Incorrect PIN")
elif amount <= 0:
    print("Enter a valid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
