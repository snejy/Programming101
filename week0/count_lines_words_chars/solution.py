import sys
    
def count_chars(filename):
    file = open(filename,'r')
    contents = file.read()
    file.close()
    return len(contents)

def count_lines(filename):
    file = open(filename,'r')
    contents = file.read().split("\n")
    file.close()
    return len(contents)-1

def count_words(filename):
    file = open(filename, 'r')
    contents = file.read().split(" ")
    file.close()
    return len(contents)

def main():
    if len(sys.argv)>2:
        filename = sys.argv[2]
        if sys.argv[1]=='chars':
            print(count_chars(filename))
        elif sys.argv[1]=='lines':
            print(count_lines(filename))
        elif sys.argv[1]=='words':
            print(count_words(filename))
    else:
        print("Not enough arguments given")

if __name__ == '__main__':
    main()