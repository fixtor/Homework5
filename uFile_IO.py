def Input_data_file(file_name, any_strings, attribute):
    data = open(file_name, attribute)
    data.writelines(any_strings)
    data.close()


def Output_data_file(file_name, attribute):
    data = open(file_name, attribute)
    data_list = []
    for line in data:
        a = line.rstrip(line[-1])
        data_list.append((a))
    data.close()
    return data_list

def Output_data_string_file(file_name, attribute):
     with open(file_name, attribute) as data:
         text = data.read()
         return text
     data.close()