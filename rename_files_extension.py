import os

def rename_files(file_path, extension):
    file_path = r'{}'.format(file_path)
    file_list = os.listdir(file_path)
    saved_path = os.getcwd()
    os.chdir(file_path)

    for file_name in file_list:
        os.rename(file_name, file_name + extension)
    os.chdir(saved_path)

file_path = input()
extension = input()
rename_files(file_path, extension)
