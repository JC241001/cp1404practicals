import math

ABS_TOL = 0.0001

def display_menu():
    print(); print()
    print('(1) Show the even numbers from x to y')
    print('(2) Show the odd numbers from x to y')
    print('(3) Show the squares from x to y')
    print('(4) Exit the Program')
    print()

def main():
    display_menu()
    response = input()

    while response != '4':
        x = int(input('x value: '))
        y = int(input('y value: '))

        if response == '1':
            print('Even {} to {}:'.format(x,y))
            for i in range(x,y+1):
                if i%2 == 0:
                    print(i, end=' ')
        elif response == '2':
            print('Odd {} to {}:'.format(x,y))
            for i in range(x,y+1):
                if i%2 == 1:
                    print(i, end=' ')
        elif response == '3':
            print('squares within {} to {}'.format(x,y))
            for i in range(x,y+1):
                sqrt_i = math.sqrt(i)
                if (sqrt_i - math.floor(sqrt_i)) < ABS_TOL:
                    print(i, end=' ')
        elif response == '4':
            break
        else:
            print('bad input. Try again')

        display_menu()
        response = input()

    print('Goodbye')

if __name__ == '__main__': main()
