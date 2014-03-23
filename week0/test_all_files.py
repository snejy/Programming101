from subprocess import call
import glob
import os

def main():
    directory = os.path.dirname(os.path.realpath('test_all_files.py'))
    for folder in glob.glob('*'):
        if folder != 'test_all_files.py':
            os.chdir(directory + "/" + folder)
            print("Testing " + folder + ":")
            call("python3.3 tests.py", shell = True)


if __name__ == '__main__':
    main()
