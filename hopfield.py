import numpy as np
import imageio
import random
import os
import re
from PIL import Image
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from core_functions import *


class hopfield():
    node = 0
    weight = 0
    
    def init(self, train_files, size = 3600, current_path = None):
#we initialise the weight
        print('***start the initialisation***')
        self.node = np.zeros(3600)
        self.weight = np.zeros((3600,3600))
        for ii in range(size):
            for jj in range(ii, size):
                s = 0
                for pp in train_files:
                    s = s + pp[ii]*pp[jj]
                   
                self.weight[ii][jj] = float(s / len(train_files))
                self.weight[jj][ii] = self.weight[ii][jj]
                if (ii == jj):
                    self.weight[ii][jj] = 0
                        
       # self.update_weight(train_files)
        
           
            
    def update_weight(self,vector):
        w = self.weight
        temp = np.zeros(self.weight.shape)
        for i in range(self.weight.shape[0]):
            for j in range(self.weight.shape[1]):
                if (i == 0):
                    self.weight[i][j] = 0
                else :
                    c = vector[i]*vector[j]
                    print(c)
                    self.weight[i][j] = self.weight[i][j] 

    
    
    def check(self, patterns):
        print('** check function **')
        for pat in patterns:
            self.node = pat  
            stored  = False   
            while not stored:         
                new_state = check_one(self.node, self.weight)
                if(np.array_equal(self.node,new_state)):
                    print('pattern stored')
                    stored = True
                else:
                    print('Not stored yet !')
                self.node = new_state
     

    
    def test(self, pattern, data):
        checked = False
        self.node = pattern
        for i in range(20):       
            new_state = check_one(self.node, self.weight)
            for dat in data:
                if(np.array_equal(dat,new_state)):
                    print('pattern recovered')
                    print(new_state)
                    checked = True
                    return new_state
                else:
                    c = 0
                    print('waiting _\|/_')
                    for i in range(len(dat)):
                        if(new_state[i] == dat[i]):
                            c = c + 1
                    print(float(c/len(pattern)),' per cent')

                    print(new_state)
                    print(self.node)
            self.node = new_state







        

