import os
import pandas

## Array of all the file names in the path
#images = os.listdir('/Users/NitaGanapathi/Desktop/udacity-40G-output/center')


# Print the first one
#print images[0]

angle = "left_camera"

c_angle = []
s_angle = []

filename = "data_" + angle + ".txt"
text_file = open(filename, "w")

# Read a CSV file
data = pandas.read_csv('/Users/NitaGanapathi/Desktop/udacity-40G-output/interpolated.csv')
#print len(data["frame_id"])

for i in range(0, len(data["frame_id"])):
    c_angle.append(data["frame_id"][i])
    s_angle.append(data["angle"][i])


i = 0
j = 0
for camera_angle in c_angle:
    if camera_angle == angle:
        text_file.write(str(i) + ".jpg" + ' ' + str(s_angle[j]) + '\n')
        #print str(images[i]) + " " + str(s_angle[j]) + "\n"
        i += 1
    j += 1


text_file.close()








# Return the first row's timestamp and the first row's steering angle
#print data["timestamp"][0]
#print data["angle"][0]
