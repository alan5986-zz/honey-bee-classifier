import os
import cv2

#Read all images from one directory, crop them and save them to another directory

readFolder = 'C:' + os.sep + os.path.join('Users', 'Sam', 'Documents', 'MastersFolder', 'Dissertation', 'labelledimages')
writeFolder = 'C:' + os.sep + os.path.join('Users', 'Sam', 'Documents', 'MastersFolder', 'Dissertation', 'croppedimages')

allImages = [f for f in os.listdir(readFolder) if os.path.isfile(os.path.join(readFolder, f))]

for img in allImages:
    readImg = cv2.imread(os.path.join(readFolder, img))
    crop_img = readImg[0:1080, 400:1050]
    cv2.imwrite(os.path.join(writeFolder, img), crop_img)