import numpy as np
import tensorflow as tf
import tensorflow.compat.v1 as tf
import binascii
import pandas as pd
import matplotlib as mlab
from PIL import Image
from numpy import asarray
tf.disable_v2_behavior()
import csv
from array import *
import os

filename = 'img.png'
filename1 = 'Test.jpg'
filename2 = 'aruba.png'
filename3 = 'paypal.jpg'
filename4 = 'n26.png'


#with open(filename, 'rb') as f:
#    content = f.read()
#c=(binascii.hexlify(content))

image = Image.open(filename)

image1 = Image.open(filename1)

image2 = Image.open(filename2)

image3 = Image.open(filename3)

image4 = Image.open(filename4)


data1 = asarray(image1)

data = asarray(image)

data2 = asarray(image2)

data3 = asarray(image3)

data4 = asarray(image4)

#t = data[tuple[map(slice, data2.shape))]

p = data4[tuple(map(slice, data2.shape))]

q = data[tuple(map(slice, data2.shape))]

#r = data4[tuple(map(slice, data2.shape))]

f = data1[tuple(map(slice, data2.shape))]

q1 = np.copy(q)
new_array = [tuple(row) for row in q1]
uniques = np.unique(new_array)
print(uniques)

#f = open('numbers2.csv', 'w')

#with f:

#    writer = csv.writer(f)

#    for row in uniques:
#        writer.writerows(row)

p1 =  np.copy(p)
new_array1 = [tuple(row) for row in p1]
uniques1 = np.unique(new_array1)
print(uniques1)

f1 = np.copy(f)
new_array2 = [tuple(row) for row in f1]
uniques2 = np.unique(new_array2)
print(uniques2)


#p1[0,0,0] = int('1')
#p1[0,0,1] = int('2')
#p1[0,0,2] = int('3')
#p1[0,0,3] = int('4')


#f = open('numbers3.csv', 'w')

#with f:

#    writer = csv.writer(f)

#    for row in p1:
#        writer.writerows(row)


TRAIN_DATA_URL = "https://drive.google.com/file/d/1M4EqlE8RtPCJi3ip5jz_2IXraINWr_9S/view?usp=sharing"

TEST_DATA_URL = "https://drive.google.com/file/d/10CzEo66Wkl9m3G0d_c19dyUI__0jT4Fl/view?usp=sharing"

train_file_path = tf.keras.utils.get_file("numbers2.csv", TRAIN_DATA_URL)
test_file_path = tf.keras.utils.get_file("number3.csv", TEST_DATA_URL)


LABEL_COLUMN = 'survived'
LABELS = [0, 4]




