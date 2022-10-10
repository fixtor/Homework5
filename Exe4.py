# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`
from uFile_IO import *


def archive(string):
    encoding = ""
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + string[i]
        i += 1
    return encoding



if __name__ == '__main__':
    Input_data_file("file_exe4_extract.txt", archive(Output_data_string_file('file_exe4_archive.txt', 'r')), 'w')
    print(Output_data_string_file('file_exe4_extract.txt', 'r'))

def decoding_text(text2):
    count = ''
    str_decode = ''
    for char in text2:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_text(Output_data_string_file("file_exe4_extract.txt", 'r'))
print(str_decode)
