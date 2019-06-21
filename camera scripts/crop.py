import os
import cv2

#Read all images from one directory, crop them and save them to another directory

readFolder = 'E:' + os.sep + os.path.join('rawimages')
writeFolder = 'E:' + os.sep + os.path.join('croppedimages')

allImages = [f for f in os.listdir(readFolder) if os.path.isfile(os.path.join(readFolder, f))]

for img in allImages:
    readImg = cv2.imread(os.path.join(readFolder, img))
    crop_img = readImg[120:955, 540:1355]
    cv2.imwrite(os.path.join(writeFolder, img), crop_img)
