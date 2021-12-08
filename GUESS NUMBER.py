import random

computer_number = random.randint(0,100)
human_guess = ""

print(" WELCOME TO GUESS MY NUMBER. ")
print(" I HAVE  A NUMBER IN MIND BETWEEN O AND 100 ")


while human_guess != computer_number:
        human_guess = input(" WHAT IS YOUR GUESS? ")
        while human_guess.isnumeric() == False:
            human_guess = input(" PLEASE INPUT A VALID NUMBER: ")
        human_guess = int(human_guess)
        if human_guess > computer_number:
            print(" YOUR GUESS IS TOO HIGH ")
        elif human_guess < computer_number:
            print (" YOUR GUESS IS TOO LOW ")
        if human_guess == computer_number:
            print(" CONGRATULATIONS YOU GUESSED IT RIGHT ")
            print(" THE COMPUTER'S NUMBER WAS: ",computer_number)
           