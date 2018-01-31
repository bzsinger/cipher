import sys

def read_file(file_name):
    file = open(file_name,"r")
    return file.read()

def cipher(text):
    return text

if __name__ == '__main__':
    contents = read_file(sys.argv[1])
    print(cipher(contents))
