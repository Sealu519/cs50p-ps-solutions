def main():
    x = int(input('The value of x = '))
    y = int(input('The value of y = '))
    compare(x, y)
    mod(x, y)


def compare(x, y):
    if x > y:
        print('x is greater')
    elif x < y:
        print('y is greater')
    elif x == y:
        print('x equals to y')


def mod(x, y):
    if x % y == 0:
        print('x is multiples of y')
    else:
        print('x y parity')


main()
