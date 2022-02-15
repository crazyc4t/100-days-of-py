print("Welcome to the adventure game!\nYou are in a deserted island, you are lost and you need to get home")


step1 = input("You will wait for a boat or swim to get out of the island?\n(Write 'boat' for the Boat or 'Swim' for swimming) ")

if step1 == 'Boat' or 'boat':
    print("You are lucky, the boat arrived and you landend on a strange place with a house and a motorcycle")
    print("What are you going to do? ask for help in that house or steal the motorcycle?")
    step1_2 = input("(Write 'Motorcycle' for the steal or 'Help' for asking) ")
    if step1_2 == 'Motorcycle' or 'motorcycle':
        print("You stealed the bike but survived!")
    else:
        print("You asked for help, those people werent nice for you and thought you would steal from them, the police arrived\n to tell you that you need to leave property, but the police helped you escape!")
else:
    print("A rare animal ate you, you didnt survived...")