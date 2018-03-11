LOWER = 33
UPPER = 127

users_char = input("Enter a character: ")
print("Tha ASCII code for {} is {}".format(users_char, ord(users_char)))

users_num = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while not LOWER <= users_num <= UPPER:
    print("Invalid number!")
    users_num = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

print("The character for {} is {}".format(users_num, chr(users_num)))


for i in range(LOWER,UPPER+1):
    print("{:3} {:>5}".format(i, chr(i)))


num_col = int(input("how many columns: "))
for i in range(num_col):
    print("{:5}".format(i+1), end="")
print()

for i in range(LOWER, UPPER):
    for j in range(num_col):
        print("{:5}".format(i), end="")
    print()
