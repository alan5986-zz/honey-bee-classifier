#this script was adapted from https://pythonprogramming.net/convolutional-neural-network-deep-learning-python-tensorflow-keras/

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
import numpy as np
from timeit import default_timer as timer

start = timer()

ROOT = "/home/alme2/bees"

#load data features and labels
X = np.load("/home/alme2/bees/cropfeatures.npy")
y = np.load("/home/alme2/bees/croplabels.npy")

print(X.shape)
print(y.shape)

X = X/255.0

model = Sequential()
#layersize = 128
epochnum = 100
k = 3
p = 2

model.add(Conv2D(32, (k, k), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(p, p), padding='same'))

model.add(Conv2D(32, (k, k)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(p, p), padding='same'))

model.add(Conv2D(64, (k, k)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(p, p), padding='same'))

model.add(Conv2D(64, (k, k)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(p, p), padding='same'))

model.add(Flatten())

model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

callbacks = [EarlyStopping(monitor='val_loss', patience=20),
             ModelCheckpoint(filepath='best.model', monitor='val_loss', save_best_only=True)]

model.fit(X, y, batch_size=32, epochs=epochnum, callbacks=callbacks, validation_split=0.1)

model.save('cropBeeCNN.model')

finish = timer() - start
print("Operation took %f seconds" % finish)

