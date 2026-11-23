# Salary calculation (rates are example assumptions)
basic = float(input("Enter basic salary: "))
da = basic * 0.10       # 10% DA
hra = basic * 0.20      # 20% HRA
gross = basic + da + hra
tax = gross * 0.05      # 5% tax deduction
net = gross - tax

print("DA:", da)
print("HRA:", hra)
print("Gross Salary:", gross)
print("Tax Deduction:", tax)
print("Net Salary:", net)
