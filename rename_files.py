import os

def rename_files():
    file_list = os.listdir(r'G:\Projects\Python\prank')
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir(r'G:\Projects\Python\prank')
    for file_name in file_list:
        print('Old name - ' + file_name)
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        os.rename(file_name, file_name.translate(translation_table))
        print('New name - ' + file_name.translate(translation_table))
    os.chdir(saved_path)
rename_files()
