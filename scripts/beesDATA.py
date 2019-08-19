#this script was adapted from https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/

import numpy as np
import os
import cv2
from tqdm import tqdm
import random

DATADIR = "/home/alme2/bees/cropimages"
ROOT = "/home/alme2/bees"

CATEGORIES = ["nopollen", "pollen"]

training_data = []

def create_training_data():
    for category in CATEGORIES:  

        path = os.path.join(DATADIR,category)  
        class_num = CATEGORIES.index(category)  

        for img in tqdm(os.listdir(path)):  
            try:
                img_array = cv2.imread(os.path.join(path,img))  
                new_array = cv2.resize(img_array, (200, 300))  
                training_data.append([img_array, class_num])  
            except Exception as e:  
                pass       

create_training_data()

print(len(training_data))

for sample in training_data[:10]:
    print(sample[1])
	
random.shuffle(training_data)

for sample in training_data[:10]:
    print(sample[1])
	
features = []
label = []

for f,l in training_data:
    features.append(f)
    label.append(l)
    
for i in range(10):
    print(features[0].shape)
    
features = np.array(features).reshape(-1, 200, 300, 3)	
	
np.save(os.path.join(ROOT,'featurescrop.npy'),features)
np.save(os.path.join(ROOT,'labelcrop.npy'),label)	
