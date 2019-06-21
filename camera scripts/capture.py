#adapted from picamera documentation
#Takes continuous captures with Pi camera and saves to USB drive
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    #camera.framerate = 120
    #set shutter speed according to light/motion conditions
    camera.shutter_speed = 2000
    # Wait for the automatic gain control to settle
    time.sleep(3)
    # Now fix the values
    #camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    print(camera.shutter_speed)
    # Finally, take several photos with the fixed settings
    #print(camera.exposure_speed)
    for i, filename in enumerate(camera.capture_continuous('/media/pi/USB/rawimages/image{timestamp:%d-%m-%Y-%H-%M-%S-%f}.jpg')):
        #seconds between each capture
        time.sleep(1)
        #counter, use i == 3600 with 1 second sleep for 1 hour of capture
        if i == 3600:
            break

