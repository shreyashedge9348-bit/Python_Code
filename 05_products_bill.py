# Three products; discount and GST rates are example assumptions
subtotal = 0
for i in range(1, 4):
    price = float(input(f"Enter price of product {i}: "))
    quantity = int(input(f"Enter quantity of product {i}: "))
    subtotal += price * quantity

discount = subtotal * 0.10  # 10%
taxable_amount = subtotal - discount
gst = taxable_amount * 0.18  # 18%
final_amount = taxable_amount + gst

print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST:", gst)
print("Final payable amount:", final_amount)
