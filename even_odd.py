## Problem Statement: Check if the number inputted by the user is even or odd.

# To solve this problem, we can use the modulus operator (%) to determine if a number is even or odd. If a number is divisible by 2 (i.e., the remainder is 0), it is even; otherwise, it is odd.


a = int(input("Dear User, Please enter a number of your choice: "))

if a%2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

