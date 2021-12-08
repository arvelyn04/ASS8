import random

print(" WELCOME TO THE LOTTERY GAME! ")
print(" ENTER LOTTERY DIGITS FROM 0-9: ")
print()

play_again = "y"

while play_again == "y":
    digit1=int(input("1st Digit: "))
    digit2=int(input("2nd Digit: "))
    digit3=int(input("3rd Digit: "))
    digit_list=[digit1,digit2,digit3]
    digit_list.sort()
    print("YOUR DIGITS:",digit1,digit2,digit3)

    winning_number1=random.randint(0,9)
    winning_number2=random.randint(0,9)
    winning_number3=random.randint(0,9)
    winning_number_list=[winning_number1,winning_number2,winning_number3]
    winning_number_list.sort()
    print(" LOTTO WINNING NUMBERS FOR TODAY:",winning_number1,winning_number2,winning_number3)

    if digit1==winning_number1 and digit2==winning_number2 and digit3==winning_number3:
      print(" YOU'RE A WINNER! ")
    else:
      print(" YOU LOSE ")
    play_again=input("DO YOU WANT TO PLAY AGAIN? y or n: ")
    if play_again == "y":
        digit_list is not winning_number_list
    else:
        print (" Thanks for playing lotto. ")  