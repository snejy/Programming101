import sys

def cat(filename):
    file=open(filename, "r")
    content=file.read()
    file.close()
    return content


def main():
	if len(sys.argv) > 1:
		filename=sys.argv[1]
		cat(filename)
	else:
		print("No arguments given.")

if __name__ == '__main__':
	main()