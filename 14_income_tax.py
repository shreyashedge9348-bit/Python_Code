# Simplified illustrative tax slabs (not current tax advice)
income = float(input("Enter annual income (Rs.): "))
tax = 0

if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10
elif income <= 1200000:
    tax = 45000 + (income - 900000) * 0.15
else:
    tax = 90000 + (income - 1200000) * 0.20

print("Illustrative tax payable:", tax)
