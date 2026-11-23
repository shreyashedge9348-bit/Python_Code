# Example data-plan slabs
usage = float(input("Enter monthly data usage (GB): "))
if usage <= 5:
    bill = 100
elif usage <= 10:
    bill = 100 + (usage - 5) * 20
elif usage <= 20:
    bill = 200 + (usage - 10) * 15
else:
    bill = 350 + (usage - 20) * 10
print("Monthly data bill: Rs.", bill)
