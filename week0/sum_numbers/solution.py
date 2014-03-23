import sys

def sum_numbers(filename):
	file = open(filename,"r")
	content=file.read().split(" ")
	content= list(map(lambda x: int(x), content))
	file.close()
	return sum(content)

def main():
	if len(sys.argv)>1:
		filename = sys.argv[1]
		print(sum_numbers(filename))
	else:
		print("Not enough arguments given")

if __name__ == '__main__':
	main()