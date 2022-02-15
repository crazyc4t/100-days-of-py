# Write your code below this line 👇
def prime_checker(number):
    checker = number % 2
    if checker == 0:
        print("Your number isn't a prime one")
    else:
        print("Your number is a prime one")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
