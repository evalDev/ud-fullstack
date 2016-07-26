import os
def rename_files():
    files_dir = "/home/mute/repos/udacity/programing-fondations//02-use-functions/prank"
    saved_path = os.getcwd()
    os.chdir(files_dir) 
    #1. Get the name of each file in folder
    file_list = os.listdir(files_dir)
    for file_name in file_list:
        #2. remove numbers from each file name
        file_name_no_numbers = file_name.translate(None, "0123456789")
        print "Changing:", file_name, "to:", file_name_no_numbers
        os.rename(file_name, file_name_no_numbers)

    os.chdir(saved_path)
rename_files()
