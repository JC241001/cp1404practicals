import random

for i in range(30):
    print(random.randint(5, 20), end=", ")
print()

for i in range(10):
    print(random.randrange(3, 10, 2), end=", ")
print()

for i in range(10):
    print(random.uniform(2.5, 5.5), end=", ")
print()
