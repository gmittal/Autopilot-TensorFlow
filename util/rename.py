import os

direction = "center"

def rename(directory):
    i = 0
    for file_name in os.listdir(directory):
        new_file_name = "/Users/NitaGanapathi/Desktop/udacity-40G-output/" + direction + "/" + str(i) + '.jpg'
        old_file_name = "/Users/NitaGanapathi/Desktop/udacity-40G-output/" + direction + "/" + file_name
        os.rename(old_file_name, new_file_name)
        i += 1

PATH = os.path.abspath('/Users/NitaGanapathi/Desktop/udacity-40G-output/' + direction)
rename(PATH)
