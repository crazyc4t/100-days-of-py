from collections import Counter
name1 = input("What is your name? ")
name2 = input("What is your lover's name? ")

name1_low = name1.lower()
name2_low = name2.lower()

countername1 = Counter(name1_low)
countername2 = Counter(name2_low)
digits1_2 = countername2['t', 'r', 'u', 'e']
digits1 = countername1['t', 'r', 'u', 'e']

digits2_2 = countername2['l', 'o', 'v', 'e']
digits2 = countername1['l', 'o', 'v', 'e']

first_digit = int(digits1 + digits1_2)
second_digit = int(digits2 + digits2_2)

complete = str(first_digit + second_digit)
total = int(complete)

if total <= 10:
    print(f"You go together like coke and mentos {total}")
elif total >= 30 and total <= 70:
    print(f"You are alright {total}")
else:
    print(f"You are made for each other {total}")  


    




