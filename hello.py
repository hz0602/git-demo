import sys

def default():
    if len(sys.argv) != 2:
        print("wrong usage")
        return
    if sys.argv[1] == "cat":
        print("meow")
    elif sys.argv[1] == "dog":
        print("wow")
    else:
        print("hello world")

def isOdd(num):
    if num % 2 == 0:
        print("It's a even")
    else:
        print("It's a odd")

def calculateSum(num):
    sum = 0
    for i in range(num):
        sum += i
    print(sum)


def main():
    calculateSum()

if __name__ == "__main__":
    main()
