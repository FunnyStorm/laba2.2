from math import *

def inanout(x, y, R):
    if x**2 + y**2 <= R**2 and x * y >= 0:
        if x >= 0 and y >= 0 and y >= x:
           print('Входит')
        elif x <= 0 and y <= 0 and y <= x:
            print('Входит')
        else:
            print('Не входит')
    else:
        print('Не входит')

def main():
    x = float(input('x = '))
    y = float(input('y = '))
    R = float(input('R = '))

    inanout(x, y, R)


if __name__ == "__main__":
    main()
    
