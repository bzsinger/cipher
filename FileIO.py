def read_file(file_name):
    file = open(file_name,'r')
    return file.read()

def write_file(file_name, text):
    file = open(file_name,'w')
    file.write(text)
