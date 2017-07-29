import numpy as np
import scipy.misc
import random

def angle_udacity(val):
    norm = -4*np.arcsin(val)*180/np.pi
    if np.isnan(norm):
        diff = np.ceil(val) if val < 0 else np.floor(val)
        start = -4*np.arcsin(val-diff)*180./np.pi
        start += diff * -360.
        return start
    return norm

xs = []
ys = []

#points to the end of the last batch
train_batch_pointer = 0
val_batch_pointer = 0

#read data.txt
with open("datasets/udacity-NEW/data.txt") as f:
    for line in f:
        xs.append("datasets/udacity-NEW/" + line.split()[0])
        ys.append(float(line.split()[1]))

#get number of images
num_images = len(xs)

#shuffle list of images
c = list(zip(xs, ys))
random.shuffle(c)
xs, ys = zip(*c)

train_xs = xs[:int(len(xs) * 0.8)]
train_ys = ys[:int(len(xs) * 0.8)]

val_xs = xs[-int(len(xs) * 0.2):]
val_ys = ys[-int(len(xs) * 0.2):]

num_train_images = len(train_xs)
num_val_images = len(val_xs)

def crop_udacity(img,cropx,cropy, y_off, x_off):
    y,x,z = img.shape
    startx = x//2-(cropx//2)+x_off
    starty = y//2-(cropy//2)+y_off
    return img[starty:starty+cropy,startx:startx+cropx]

def LoadTrainBatch(batch_size):
    global train_batch_pointer
    x_out = []
    y_out = []
    for i in range(0, batch_size):
        full_image = scipy.misc.imread(train_xs[(train_batch_pointer + i) % num_train_images])
        full_image = crop_udacity(full_image, 455, 256, -20, -70)
        x_out.append(scipy.misc.imresize(full_image[-150:], [66, 200]) / 255.0)
        y_out.append([train_ys[(train_batch_pointer + i) % num_train_images]])
    train_batch_pointer += batch_size
    return x_out, y_out

def LoadValBatch(batch_size):
    global val_batch_pointer
    x_out = []
    y_out = []
    for i in range(0, batch_size):
        full_image = scipy.misc.imread(val_xs[(val_batch_pointer + i) % num_val_images])
        full_image = crop_udacity(full_image, 455, 256, -20, -70)
        x_out.append(scipy.misc.imresize(full_image[-150:], [66, 200]) / 255.0)
        y_out.append([val_ys[(val_batch_pointer + i) % num_val_images]])
    val_batch_pointer += batch_size
    return x_out, y_out
