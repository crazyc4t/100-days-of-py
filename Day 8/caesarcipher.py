alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def init():
    print("Caesar Cipher")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text=text, shift=shift, direction=direction)

def caeser(text, shift, direction):
    output = ""
    if shift <= 26:
        if direction == "decode":
            shift *= -1
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                output += alphabet[new_position]
            else:
                output += letter
        print(f"The {direction}d text is {output}")
    else:
        print(f"There isn't a {shift} character in the alphabet... try again")

init()
decision = input("Do you want to go again?(y/n) ")

if decision == "y":
    init()
elif decision == "n":
    "Thank you ma boi"
    exit()
else:
    print("Not the correct option, exiting...")
    exit()
