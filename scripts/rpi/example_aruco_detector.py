import cv2 as cv
from picamera2 import Picamera2
import numpy as np

# SETUP
cam = Picamera2()
config = cam.create_still_configuration()
cam.configure(config)
cam.start()
aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_50)  # aruco dictionary
aruco_params = cv.aruco.DetectorParameters_create()

# LOOP
while True:
    if cv.waitKey(1) == ord('q'):
        break
    im = cam.capture_array()
    im_rgb = cv.cvtColor(im, cv.COLOR_BGR2RGB)
    im_resize = cv.resize(im_rgb, (400, 300))
    corners, ids, reject_candidates = cv.aruco.detectMarkers(
        im_resize,
        aruco_dict,
        parameters=aruco_params,
    )
    top_left_coords = corners[0][0][0].astype(int)
    bot_right_coords = corners[0][0][2].astype(int)
    print(corners, ids)
    image = cv.rectangle(im_resize, top_left_coords, bot_right_coords, (0, 255, 0), 2)
    cv.imshow("Camera", image)

