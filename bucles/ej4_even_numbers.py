"""
Author: Manuel Brito
Program that show the even numbers between two numbers introduced by the user.
# A even number is a number that the division with two is equal zero.
"""

print("---EVEN NUMBERS---")


try:
    
    # The user introduce two numbers for calculate the even number between n1 and n2
    n1 = int(input("\nIntroduce a number: "))
    n2 = int(input("Introduce another number: "))
    
    if n1 > n2:
        n1, n2 = n2, n1 

    # 'for' loop to go through the numbers and show the even numbers
    print("\nThe even numbers are:")
    
    n2 += 1 # to go through ALL numbers

    for num in range(n1, n2):
        if num % 2 == 0:
            print(num)

except:
    print("ERROR")













