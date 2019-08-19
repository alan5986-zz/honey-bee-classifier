import os
import cv2

#Read all images from one directory, flip them along vertical and horizontal axis and save a copy int the same directory

readFolder = "/home/alme2/bees/subsetcrop/pollen"

allImages = [f for f in os.listdir(readFolder) if os.path.isfile(os.path.join(readFolder, f))]

for img in allImages:
	readImg = cv2.imread(os.path.join(readFolder, img))
	flip_img = cv2.flip(readImg,-1)
	cv2.imwrite(os.path.join(readFolder, "flip" + img), flip_img)
