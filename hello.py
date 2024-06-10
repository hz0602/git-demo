import sys

def default():
    if len(sys.argv) != 2:
        print("wrong usage")
        return
    if sys.argv[1] == "dog":
        print("wow")
    else:
        print("hello world")

def main():
    default()

if __name__ == "__main__":
    main()
