import numpy as np 
from PIL import Image
from hopfield import *
from time import sleep



img1 = image_to_array(90, 'images/pic1.jpg')
img2 = image_to_array(90, 'images/pic2.jpg')
img3 = image_to_array(90, 'images/pic3.jpg')
test = image_to_array(90, 'images/pic4.jpg')

img1 = mat_to_vect(img1)
img2 = mat_to_vect(img2) 
img3 = mat_to_vect(img3) 
test = mat_to_vect(test)

train_file = np.array([img1,img2, img3])
hop = hopfield()
hop.init(train_file)
hop.check(train_file)


result = hop.test(test, train_file)

i = 0
for pat in train_file:
    if(np.array_equal(result,pat)):
        print('it is the pattern ', i)
        break
    else:
        print('It is not the pattern ', i)

a_test = vect_to_array(result)
a_test = array_to_image(a_test)
show_image(a_test)

sleep(100)