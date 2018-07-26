import numpy as np
import imageio
import random
import os
import re

def activation(n_output):
    if (n_output > 0):
        return 1
    else:
        return 0

def check_one(node, weight, iteration):
    new_node = np.zeros(len(node))
    for i in range(iteration):
        s = 0
        for j in range(iteration):
            s = s + weight[i][j]*node[j]
            
        new_node[i] = s 
    
    return new_node
            
        

class hopfield():
    node = 0
    weight = 0
    
    def init(self, train_file, size = (100,100), ):
        shape = patterns.shape
        self.node = np.zeros((shape[1]))
        self.weight = np.zeros((shape[1],shape[1]))
        s = 0
        for i in range(shape[1]):
            for j in range(shape[1]):
                for elt in patterns:
                    s = s + elt[i]*elt[j]
                if (i == j):
                    self.weight[i][j] = 0
                else :
                    self.weight[i][j] = float(s/shape[0])
                s = 0

    
    
    def check(self, patterns):
        print('** check function **')
        stored = False
        for pat in patterns:
            i = 0
            print(i,'th Pattern :',pat)
            stored = False     
            self.node = pat     
            while not stored:    
                print('iteration ',i,' ', self.node)       
                new_state = check_one(self.node, self.weight, self.node.shape[0])
                if(np.array_equal(self.node,new_state)):

                    print('pattern stored')
                    stored = True
                else:
                    print('Not stored yet !')
                self.node = new_state
                i = i + 1        

    
    def test(self, pattern, data):
        checked = False
        self.node = pattern
        for i in range(5):       
            new_state = check_one(self.node, self.weight, self.node.shape[0])
            print('old state',self.node)
            print('new state',new_state)
            for dat in data:
                if(np.array_equal(dat,new_state)):
                    print('pattern recovered')
                    print(new_state)
                    checked = True
                    return new_state
                else:
                    print('waiting _\|/_')
                    print(new_state)
                    print(self.node)
            self.node = new_state







        

