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

def main():
    default()

if __name__ == "__main__":
    main()
