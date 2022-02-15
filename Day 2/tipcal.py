print("Welcome to our Tip Calculator!")
value = float(input("How much did the meal costs? "))
person = float(input("How many people will pay the bill? "))
percentage = float(input("For what type of percentage will you tip? (0.15, 0.12, 0.10) (if you have another percentage type it by starting with '0.') "))
tax = value * percentage
total = tax + value
print("Total cost: ",total)
print("Each cost: ",total / person)