total_bill = float(input("Enter the total bill amount: $"))

tip_percentage = float(input("Enter the tip percentage you want to leave (e.g., 15 for 15%): "))

tip_amount = (tip_percentage / 100) * total_bill

final_amount = total_bill + tip_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to pay: ${final_amount:.2f}")
