import sys

def cat2(files):
    content = []
    for filename in files:
        file = open(filename,"r")
        content.append(file.read())
        file.close()
    return content

def main():
    if len(sys.argv) > 1:
        result = []
        for i in range(1,len(sys.argv)):
            result.append(str(sys.argv[i]))
        print(cat2(result))
    else:
        "No arguments given"

if __name__ == '__main__':
    main()