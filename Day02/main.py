print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_amount_tipped = tip_percent * bill
tipped_amount_per_person = total_amount_tipped / people

amount_per_person = (bill / people ) + tipped_amount_per_person
final_bill_per_person = round(amount_per_person, 2)

print(f"Each person should pay: ${final_bill_per_person}")


