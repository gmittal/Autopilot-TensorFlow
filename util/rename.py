import os

direction = "center"
name = "/data/autopilot/datasets/udacity-183G/"

def rename(directory):
    i = 0
    for file_name in os.listdir(directory):
        new_file_name = name + direction + "/" + str(i) + '.jpg'
        old_file_name = name + direction + "/" + file_name
        os.rename(old_file_name, new_file_name)
        i += 1

PATH = os.path.abspath(name + direction)
rename(PATH)
