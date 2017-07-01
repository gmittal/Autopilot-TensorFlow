# Make Udacity datasets NVIDIA friendly
import os, pandas, sys

PATH = sys.argv[1]
IMAGE_VIEW = "center"

angle = IMAGE_VIEW + "_camera"
direction = IMAGE_VIEW

def rename(directory):
    i = 0
    for file_name in os.listdir(directory):
        new_file_name = PATH + "/" + direction + "/" + str(i) + '.jpg'
        old_file_name = PATH + "/" + direction + "/" + file_name
        os.rename(old_file_name, new_file_name)
        i += 1
rename(os.path.abspath(PATH + "/" + direction))

c_angle = []
s_angle = []

filename = PATH + "/data.txt"
text_file = open(filename, "w")

# Read a CSV file
data = pandas.read_csv(PATH+'/interpolated.csv')

for i in range(0, len(data["frame_id"])):
    c_angle.append(data["frame_id"][i])
    s_angle.append(data["angle"][i])


i = 0
j = 0
for camera_angle in c_angle:
    if camera_angle == angle:
        text_file.write(str(i) + ".jpg" + ' ' + str(s_angle[j]) + '\n')
        i += 1
    j += 1

text_file.close()
