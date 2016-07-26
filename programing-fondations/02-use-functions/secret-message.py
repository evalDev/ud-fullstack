import os
def rename_files():
    #1. Get the name of each file in folder
    file_list = os.listdir("/home/mute/repos/udacity/programing-fondations//02-use-functions/prank")
    print file_list
#2. remove numbers from each file name

rename_files()
