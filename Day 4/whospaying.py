import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
fin = len(names)
re = random.randint(0, fin)
print(f"{names[re]} has to pay the bill!")

# Alternative:
# person_who_will_pay = random.choice(names)
