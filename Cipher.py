import sys
from FileIO import read_file, write_file
from Encrypt import encrypt
from Decrypt import decrypt

if __name__ == '__main__':
    input_file = None
    output_file = None

    if len(sys.argv) <= 2:
        raise IOError('Please add input/output file and encrypt/decrypt flag args')
    if len(sys.argv) == 3:
        input_file = sys.argv[2]
    if len(sys.argv) == 4:
        output_file = sys.argv[3]

    input_text = read_file(input_file)
    output_text = ''

    if sys.argv[1] == '-e':
        output_text = encrypt(input_text)
    elif sys.argv[1] == '-d':
        output_text = decrypt(input_text)
    else:
        raise IOError('Please add input/output file and encrypt/decrypt flag args')

    if output_file is not None:
        write_file(output_file, output_text)
    else:
        print(output_text)
