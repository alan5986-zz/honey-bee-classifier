#extracts individual bee images from large images by comparing colours
import os
import cv2
import numpy as np
from skimage import measure
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

readFolder = "/home/alme2/bees/images/pollen"
writeFolder = "/home/alme2/bees/unlabelled2"

#setup default colour ranges and parameters
edgeSize = 30
imgWidth = 200
imgHeight = 300
defaultEdgeColour = sRGBColor(50.2,109.1,157.6)
defaultCentreColour = sRGBColor(85.1,75.1,76.4)

#function to compare two colours with colormath
def compareColours(color1,color2):
    color1_lab = convert_color(color1, LabColor)
    color2_lab = convert_color(color2, LabColor)
    difference = delta_e_cie2000(color1_lab, color2_lab)
    return difference
    
#function to compare colour range of image samples with the default colour ranges
#returns true if match
def compareImage(sample):
 
    match = True

    #crop sample areas from the full image 
    topEdge = sample[0:0+edgeSize, 0:0+200]
    rightEdge = sample[0:0+300, 200-edgeSize:200-edgeSize+edgeSize]
    bottomEdge = sample[300-edgeSize:300-edgeSize+edgeSize, 0:0+200]
    leftEdge = sample[0:0+300, 0:0+edgeSize]
    centre = sample[edgeSize:300- edgeSize, edgeSize:200-edgeSize]
    
    #take average colour of sample area and convert to sRGB
    topColour = topEdge.mean(axis=0).mean(axis=0)
    topColour = sRGBColor(topColour[0],topColour[1],topColour[2])
    rightColour = rightEdge.mean(axis=0).mean(axis=0)
    rightColour = sRGBColor(rightColour[0],rightColour[1],rightColour[2])
    bottomColour = bottomEdge.mean(axis=0).mean(axis=0)
    bottomColour = sRGBColor(bottomColour[0],bottomColour[1],bottomColour[2])
    leftColour = leftEdge.mean(axis=0).mean(axis=0)
    leftColour = sRGBColor(leftColour[0],leftColour[1],leftColour[2])
    edges = [topColour, rightColour,bottomColour,leftColour]           
    sampleCentreColour = centre.mean(axis=0).mean(axis=0)
    sampleCentreColour = sRGBColor(sampleCentreColour[0], sampleCentreColour[1], sampleCentreColour[2])   

    #compare the colours of the edges and the centre. Set mactch to false if any area outside acceptable range
    for edge in edges:
        edgeDifference = compareColours(defaultEdgeColour, edge)
        if edgeDifference > 20:
            match = False
    
    centreDifference = compareColours(defaultCentreColour, sampleCentreColour)
    if centreDifference > 45:
        match = False
            
    return match                        

#loop through all images in folder, sample them and extract all images that pass the the compare function
allImages = [f for f in os.listdir(readFolder) if os.path.isfile(os.path.join(readFolder, f))]

print("extracting...")
for img in allImages:
    readImg = cv2.imread(os.path.join(readFolder, img))
    imgWidth, imgHeight = readImg.shape[1], readImg.shape[0]
    h, w = 300, 200 #bounding box dimensions
    stepsize = 30

    #move the bounding box across the image in steps generating an image at each step   
    for i in range(0, imgHeight-h, stepsize):
                for j in range(0,imgWidth-w, stepsize):
                        crop_img = readImg[i:i+h, j:j+w]
                        bgrImg = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
                        if compareImage(bgrImg):
                            print(img)
                            #crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
                            cv2.imwrite(os.path.join(writeFolder, str(i) + str(j) + img), crop_img)
               

    
