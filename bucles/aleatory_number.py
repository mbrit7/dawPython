"""
Author: Manuel Brito

Program that generate an aleatory number between 1 and 100.
The user has to input the correct one and the program can tell him if the 
number is greater or smaller that the input.
Also he has ten tries and the program finish when the number is correct, 
telling the number of tries.
If the user didn't guess the number in the ten tries, the program show the number.
"""

from random import randint

print("---Guess the number---")

# Initialize the variables
secret_number = randint(0,100)
tries = 0

# 'while' loop for controling the number of tries
# if tries = 10 the program finish
# in every loop the user introduce the number
# if is the secret number, congrats
# if not, the number is smaller or greater with the tries left
while tries < 10: 
    tries += 1
    user_number = int(input("\nTell me a number between 1 and 100: "))
    
    if user_number == secret_number:
        print("\n>>Congrats is the correct number")
        print(f">>Number of tries: {tries}")
        break 
    else:
        if secret_number < user_number:
            print("The secret number is smaller") 
            print(f"You have {abs(tries - 10)} tries left")
        else:
            print("The secret number is greater") 
            print(f"You have {abs(tries - 10)} tries left")
            

else:
    print(f"The secret number is: {secret_number}")





