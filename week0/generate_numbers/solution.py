import sys
from random import randint

def generate_numbers(filename, numbers):
    file = open(filename, "w")
    for i in range(numbers):
        file.write(str(randint(1,1000)))
        file.write(' ')
    file.close()

def main():
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        generate_numbers(filename, int(sys.argv[2]))
    else:
        "Not enough arguments given"

if __name__ == '__main__':
    main()