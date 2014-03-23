import sys
import os

def concat_files(filenames):
	filename = open("MEGATRON.txt", "a")
	for file in filenames:
		file_handler = open(file, "r")
		content = file_handler.read()
		filename.write(content)
		filename.write('\n')
		file_handler.close()
	filename.close()
	filename = open('MEGATRON.txt', 'r')
	content = filename.read()
	return content

def main():
	if len(sys.argv)>2:
		files = []
		for file in sys.argv[1:]:
			files.append(file)
		print(concat_files(files))
	
	else:
		print("Not enough arguments given.")

if __name__ == '__main__':
	main()