import numpy as np, os
import tensorflow as tf
import scipy.misc, math
import model
import cv2
from subprocess import call

def crop_udacity(img,cropx,cropy, y_off, x_off):
    y,x,z = img.shape
    startx = x//2-(cropx//2)+x_off
    starty = y//2-(cropy//2)+y_off
    return img[starty:starty+cropy,startx:startx+cropx]

def angle_udacity(val):
    norm = -4*np.arcsin(val)*180/np.pi
    if np.isnan(norm):
        diff = np.ceil(val) if val < 0 else np.floor(val)
        start = -4*np.arcsin(val-diff)*180./np.pi
        start += diff * -360.
        return start
    return norm

sess = tf.InteractiveSession()
saver = tf.train.Saver()
saver.restore(sess, "save/model.ckpt")

img = cv2.imread('steering_wheel_image.jpg',0)
rows,cols = img.shape


data = open("datasets/udacity-TEST/data.txt").read().split('\n')[:-1]
angles = map(lambda x: float(x.split(' ')[1]), data)
images = map(lambda x: x.split(' ')[0], data)


smoothed_angle = 0

i = 0
while(cv2.waitKey(10) != ord('q')):
    full_image = scipy.misc.imread("datasets/udacity-TEST/" + images[i], mode="RGB")
    full_image = crop_udacity(full_image, 455, 256, -20, -70)
    image = scipy.misc.imresize(full_image[-150:], [66, 200]) / 255.0
    degrees = model.y.eval(feed_dict={model.x: [image], model.keep_prob: 1.0})[0][0] #* 180 / scipy.pi
    degrees = angle_udacity(degrees)
    call("clear")
    print("Predicted steering angle: " + str(degrees) + " degrees")
    print("Ground truth steering angle: " + str(angles[i] * -25) + " degrees")
    cv2.imshow("frame", cv2.cvtColor(full_image, cv2.COLOR_RGB2BGR))
    
    #make smooth angle transitions by turning the steering wheel based on the difference of the current angle
    #and the predicted angle
    diff = 0.2 * pow(abs((degrees - smoothed_angle)), 2.0 / 3.0) * (degrees - smoothed_angle) / abs(degrees - smoothed_angle)
    smoothed_angle +=diff
    M = cv2.getRotationMatrix2D((cols/2,rows/2),-smoothed_angle,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow("steering wheel", dst)
    i += 1

cv2.destroyAllWindows()
