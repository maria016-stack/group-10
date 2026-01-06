number=4
guess=0
while guess != number:
    guess=int(input("enter your guess between 1 and 9: "))
    if guess != number:
        print("wrong guess please try again")
    if guess == number:
        print("you guessed correctly")
        break


