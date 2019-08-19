import os
import cv2
import csv
import ast

#crop individual bees from raw images according to region data in csv file,
#resize and save into folder according to pollen label

readFolder = "/home/alme2/bees/images/pollen"
pollenFolder = "/home/alme2/bees/subsetcrop/pollen"
yellowPollenFolder = "/home/alme2/bees/subsetcrop/yellowpollen"
orangePollenFolder = "/home/alme2/bees/subsetcrop/orangepollen"
whitePollenFolder = "/home/alme2/bees/subsetcrop/whitepollen"
greenPollenFolder = "/home/alme2/bees/subsetcrop/greenpollen"
nopollenFolder = "/home/alme2/bees/subsetcrop/nopollen"

with open('region_data.csv', 'r') as csvFile:
        labelData = csv.DictReader(csvFile)

        for row in labelData:
                if int(row["region_count"]) > 0:
                        filename = row["#filename"]
                        img = cv2.imread(os.path.join(readFolder, filename))
                        regionData = ast.literal_eval(row["region_shape_attributes"])
                        pollenTag = ast.literal_eval(row["region_attributes"])
                        x = regionData["x"]
                        y = regionData["y"]
                        h = regionData["height"]
                        w = regionData["width"]
                        crop_img = img[y:y+h, x:x+w]
                        crop_img = cv2.resize(crop_img,(150,200))
                        if pollenTag["pollen"] == "p":
                                cv2.imwrite(os.path.join(pollenFolder, filename), crop_img)
                                if "colour" in pollenTag:
                                        if pollenTag["colour"] == "y":
                                                cv2.imwrite(os.path.join(yellowPollenFolder, filename), crop_img)
                                        elif pollenTag["colour"] == "o":
                                                cv2.imwrite(os.path.join(orangePollenFolder, filename), crop_img)
                                        elif pollenTag["colour"] == "w":
                                                cv2.imwrite(os.path.join(whitePollenFolder, filename), crop_img)
                                        elif pollenTag["colour"] == "g":
                                                cv2.imwrite(os.path.join(greenPollenFolder, filename), crop_img) 
                        else:
                                cv2.imwrite(os.path.join(nopollenFolder, filename), crop_img)
                   
                        
 
