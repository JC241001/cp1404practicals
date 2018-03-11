
#PART 1
name_1 = input("Enter your name: ") + ".txt"
open_file = open(name_1, 'w')
open_file.write(name_1)
open_file.close()

#PART 2
open_file = open(name_1, 'r')
name_2 = open_file.readline()[:-4]
print("Your name is {}".format(name_2))
open_file.close()





