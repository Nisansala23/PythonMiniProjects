name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road,it has come to an end and you can go leftt or right to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river,you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("you swam accross and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles,ran out of water,and you lost the game.")
    else:
        print('Not a valid option.You lose.')


elif answer == "right":
    answer = input(
        "You come to a bridge,it looks wobbly,do you want to cross it or head back (cross/back)?")

    if answer == "back":
        print("you go nback and lose.")

    elif answer == "cross":
        answer = input(
            "you cross the bridge and meet a stranger.Do you talk to them? (yes/no)?")
        if answer == "yes":
            print("you talk to the stranger and they give you Gold.You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid information you lose')
    else:
        print('Not a valid option.You lose.')


else:
    print("Not a valid option.you lose.")

print("Thankyou for trying", name)
