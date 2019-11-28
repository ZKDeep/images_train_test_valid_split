# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:25:22 2019

@author: zubair
"""

import os
import numpy as np
import random
import shutil

def images_train_test_valid_split(target_path, test_valid_split):  
    os.mkdir("valid")
    os.mkdir("test")
    for dest in range(2):
        classes =  os.listdir(target_path)
        print(dest)
        for clas in classes:
            if dest == 0:
                dest_t = "test"
                try:    
                    os.makedirs(dest_t + '/' + clas)
                    des = dest_t + '/' + clas 
                except:
                     print("exiting...")
                     
                     des = dest_t + '/' + clas
                        #os.mkdir(dest_t + "/"  + clas)
                    #shutil.move(target, dest_t + '/' + clas)
            if dest == 1:
                dest_t = "valid"
                try:
                    os.makedirs(dest_t + '/' + clas)
                    des = dest_t + '/' + clas
                except:
                    print("exiting...")
                    des = dest_t + '/' + clas
                    
            
            files = os.listdir(target_path + '/' + clas)
            #print(files)
            images_to_copy = int(len(files)*test_valid_split[dest])
            selected_indexes = random.sample(range(0, len(files)), images_to_copy)
            #print(selected_indexes)
            for si in selected_indexes:
                target = target_path + "/" + clas + "/" + files[si]
                shutil.move(target, des)
    
    os.rename(target_path, "train")