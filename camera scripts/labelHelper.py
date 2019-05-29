# Successivly loads images from a given directory. Allows user to label it and then saves the image name and label data
# to a txt file. Moves images to another directory once labelled indicating they have been processed.

import os
import cv2

rootFolder = 'C:' + os.sep + os.path.join('Users', 'Sam', 'Documents', 'MastersFolder', 'Dissertation')
readFolder = os.path.join(rootFolder, 'unlabelledimages')
writeFolder = os.path.join(rootFolder, 'refinedlabelledimages')

# List all images in directory
allImages = [f for f in os.listdir(readFolder) if os.path.isfile(os.path.join(readFolder, f))]

def main():
    try:
        if not os.path.exists(readFolder):
            os.makedirs(readFolder)
    except OSError:
        print('Error: Creating directory of data')

    for pic in allImages:
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty("image", cv2.CV_WINDOW_AUTOSIZE)
        img = cv2.imread(os.path.join(readFolder, pic))
        cv2.imshow('image', img)
        key = cv2.waitKey(0)
        keychoice(key, pic)
        cv2.destroyAllWindows()

def keychoice(key, pic):
    if '0' == chr(key & 255):
        labelFile = open(os.path.join(writeFolder, 'labels.txt'), 'a')
        labelFile.write(pic + ' ' + '0 ' + '0 ' + '0\n')
        labelFile.close()
        os.rename(os.path.join(readFolder, pic), os.path.join(writeFolder, pic))
    elif '1' == chr(key & 255):
        labelFile = open(os.path.join(writeFolder, 'labels.txt'), 'a')
        labelFile.write(pic + ' ' + '1 ' + '0 ' + '0\n')
        labelFile.close()
        os.rename(os.path.join(readFolder, pic), os.path.join(writeFolder, pic))
    elif '2' == chr(key & 255):
        labelFile = open(os.path.join(writeFolder, 'labels.txt'), 'a')
        labelFile.write(pic + ' ' + '1 ' + '1 ' + '0\n')
        labelFile.close()
        os.rename(os.path.join(readFolder, pic), os.path.join(writeFolder, pic))
    elif 'm' == chr(key & 255):
        labelFile = open(os.path.join(writeFolder, 'labels.txt'), 'a')
        labelFile.write(pic + ' ' + '1 ' + '0' + '1\n')
        labelFile.close()
        os.rename(os.path.join(readFolder, pic), os.path.join(writeFolder, pic))
    elif 'p' == chr(key & 255):
        labelFile = open(os.path.join(writeFolder, 'labels.txt'), 'a')
        labelFile.write(pic + ' ' + '1 ' + '1 ' + '1\n')
        labelFile.close()
        os.rename(os.path.join(readFolder, pic), os.path.join(writeFolder, pic))
    elif key == 0: # for some reason my machine is registering the DEL key as 0 instead of 127
        cv2.destroyAllWindows()
        os.rename(os.path.join(readFolder, pic), os.path.join(rootFolder,'unusedimages', '19.08.18', pic))
    elif key == 27:
        cv2.destroyAllWindows()
        quit(0)
    else:
        key = cv2.waitKey(0)
        keychoice(key, pic)

if __name__ == "__main__":
    main()