import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.read()

def write_file(file_name, text):
    file = open(file_name,'w')
    file.write(text)

def cipher(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) - 1)
    return encrypted_text

if __name__ == '__main__':
    input_file = None
    output_file = None

    if len(sys.argv) == 1:
        raise IOError('Please add input file arg')
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
    if len(sys.argv) == 3:
        output_file = sys.argv[2]

    contents = read_file(input_file)

    if output_file is not None:
        write_file(output_file, cipher(contents))
    else:
        print(cipher(contents))
