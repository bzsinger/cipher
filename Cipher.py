import sys
from FileIO import read_file, write_file
from Encrypt import encrypt
from Decrypt import decrypt

if __name__ == '__main__':
    input_file = None
    output_file = None

    if len(sys.argv) < 4:
        raise IOError('\nProper usage: \npython Cipher.py [-e/-d] <shift> <input_file_path> <OPTIONAL_output_file_path>')

    try:
        int(sys.argv[2])
    except Exception as e:
        raise IOError('\nProper usage: \npython Cipher.py [-e/-d] <shift> <input_file_path> <OPTIONAL_output_file_path>')

    shift = int(sys.argv[2])

    input_file = sys.argv[3]
    if len(sys.argv) == 5:
        output_file = sys.argv[4]

    input_text = read_file(input_file)
    output_text = ''

    if sys.argv[1] == '-e':
        output_text = encrypt(input_text, shift)
    elif sys.argv[1] == '-d':
        output_text = decrypt(input_text, shift)
    else:
        raise IOError('Proper usage: \'python Cipher.py [-e/-d] <shift> <input_file_path> <OPTIONAL_output_file_path>\'')

    if output_file is not None:
        write_file(output_file, output_text)
    else:
        print(output_text)
