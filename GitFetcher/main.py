import os

def find_dirs():
	# dir_path = os.path.dirname(os.path.realpath(__file__))
	dir_path = os.path.dirname("C:\\")

	for root, dirs, files, in os.walk(dir_path):
		for file in files:
			if file.endswith('dirs.txt'):
				print (root + '\\' + str(file))

def main():
	find_dirs()

if __name__ == "__main__":
	main()