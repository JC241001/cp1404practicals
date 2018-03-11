
open_file = open('numbers.txt', 'r')

sum = 0
for each_number in open_file:
    sum += int(each_number)
print(sum)

open_file.close()
