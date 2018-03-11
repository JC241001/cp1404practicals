"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?    Enter a non integer in either input
2. When will a ZeroDivisionError occur?     Enter a zero in the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?       done
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Zero is not valid, try again")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")