# Modified version of keithweavers script taken from GitHub
# https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57

# Reads all video files in a given directory. Breaks them into separate frames and saves the frames in another
# directory with a dynamic name. Then moves video files to another directory indicating they have been processed.

import cv2
import os

rootFolder = 'C:' + os.sep + os.path.join('Users', 'Sam', 'Documents', 'Masters Folder', 'Dissertation')
readFolder = rootFolder + os.sep + 'rawvideo'
pathToWrite = rootFolder + os.sep + 'rawimages'
processedFiles = rootFolder + os.sep + 'processedvideo'

# List all files in directory
allVids = [f for f in os.listdir(readFolder) if os.path.isfile(os.path.join(readFolder, f))]

try:
    if not os.path.exists(pathToWrite):
        os.makedirs(pathToWrite)
except OSError:
    print('Error: Creating directory of data')

try:
    if not os.path.exists(processedFiles):
        os.makedirs(processedFiles)
except OSError:
    print('Error: Creating directory of processed data')

# name = os.path.join(pathToWrite, str(currentFrame) + '.jpg')
#
# # Starts writing file names successively after highest existing one
# while os.path.isfile(name):
#     # The following line simply prints the names of existing files. It is expensive. Only uncomment if needed
#     #print('File with name ' + name + ' already exists. Renaming...')
#     currentFrame += 1
#     name = os.path.join(pathToWrite, str(currentFrame) + '.jpg')

for video in allVids:
    # Playing video from file:
    cap = cv2.VideoCapture(readFolder + os.sep + video)

    # take the timestamp from the video and use this to start naming each frame
    fields = video.split('.')
    print(fields[0])
    # Turn the timestamp from seconds to milliseconds
    currentFrame = int(fields[0]) * 1000

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Saves image of the current frame in jpg file
        name = os.path.join(pathToWrite, str(currentFrame) + '.jpg')

        # The following line simply prints the name of the file being saved. It is expensive so only uncomment if needed.
        #print('Working with video ' + video)
        #print('Creating...' + name)

        cv2.imwrite(name, frame)

        # 30fps so each frame has 33(.3) milli seconds added to it
        currentFrame += 33

        if not ret:
            break

    # Place file in new directory once processed
    cap.release()
    os.rename(os.path.join(readFolder, video), os.path.join(processedFiles, video))

# When everything done, release the capture
cv2.destroyAllWindows()