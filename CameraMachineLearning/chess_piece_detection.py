"""
Author: John Nesnidal
File: chess_piece_detection.py
Notes:
    Packages need to be installed for this to run
"""

MODEL_PATH = "chess_model_1.pt"

# set up ultralytics

import ultralytics

from ultralytics import YOLO
import matplotlib.pyplot as plt
# import os
# from PIL import Image
# import cv2
# from IPython.display import Video
# import glob

import warnings
warnings.filterwarnings('ignore')

ultralytics.checks()

# configure local model

local_model = YOLO(MODEL_PATH)

# test model

def test_local_model(image_path):
    pass

    results = local_model.predict(source=image_path, imgsz=640)
    test_image = results[0].plot(line_width=2)
    plt.imshow(test_image)
    input()



