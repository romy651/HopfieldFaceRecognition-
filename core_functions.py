import numpy as np 
from PIL import Image


def mat_to_vect(matrix):
    vect = matrix.flatten() 

    return vect

def image_to_array(treshold, path):
    file = Image.open(path)
    file.thumbnail((200,200))
    file = file.convert('L') 
    imgArray = np.array(file, dtype = np.uint8)
    x = np.zeros(imgArray.shape,np.float)
    x[imgArray > treshold] = 1
    x[ x == 0] = -1
    return x

def array_to_image(data):
    y = np.zeros(data.shape,dtype = np.uint8)
    y[data == 1] = 255
    y[data == 0] = 0
    img = Image.fromarray(y,mode="L")
    img.save('file.jpg')
    #img.show()
    return img
    

def activation(n_output):
    if (n_output > 0):
        return 1
    else:
        return -1

def check_one(node, weight):
    print(len(node))
    new_node = np.zeros(len(node))
    new_node = np.dot(weight,node)
    for i in range(len(new_node)):
        new_node[i] = activation(new_node[i])
    
    return new_node
            
def show_image(image):
    image.save('result/result.jpg')

def vect_to_array(vect, row = 60, col = 60):
    new_array = np.reshape(vect, (row, col))
    return new_array


        
