age = int(input("Enter age: "))
income = float(input("Enter monthly income (Rs.): "))
credit_score = int(input("Enter credit score: "))

# Example eligibility conditions
if age >= 21 and income >= 25000 and credit_score >= 700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
