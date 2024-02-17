# Input item code, unit price, and quantity
'''item_code = input("Enter item code: ")
unit_price = float(input("Enter unit price in Rs: "))
quantity = int(input("Enter quantity taken: "))
# Calculate total amount
total_amount = unit_price * quantity
# Calculate discount amount (20% discount)
discount = 0.20 * total_amount
discounted_total = total_amount - discount
# Print the bill in the specified format
print("\nBILL")
print("Item Code:", item_code)
print("Unit Price (Rs):", unit_price)
print("Quantity Taken:", quantity)
print("Total Amount (Rs):", total_amount)
print("Discount Amount (20%):", discount)
print("Net Payable Amount (Rs):", discounted_total)'''
def calculate_total_price(unit_price, quantity):
    return unit_price * quantity
def calculate_discount(total_amount):
    return 0.2 * total_amount 
def calculate_net_payable(total_amount, discount_amount):
    return total_amount - discount_amount
item_code = input("Enter item code: ")
unit_price = float(input("Enter unit price in Rs: "))
quantity = int(input("Enter quantity taken: "))
total_amount = calculate_total_price(unit_price, quantity)
discount_amount = calculate_discount(total_amount)
net_payable_amount = calculate_net_payable(total_amount, discount_amount)
print("\nBILL")
print("Item Code:", item_code)
print("Unit Price (Rs):", unit_price)
print("Quantity Taken:", quantity)
print("Total Amount (Rs):", total_amount)
print("Discount Amount (20%):", discount_amount)
print("Net Payable Amount (Rs):", net_payable_amount)

