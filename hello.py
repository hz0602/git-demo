import sys

def default():
    if len(sys.argv) != 2:
        print("wrong usage")
        return
    print("hello world")

def main():
    default()

if __name__ == "__main__":
    main()
