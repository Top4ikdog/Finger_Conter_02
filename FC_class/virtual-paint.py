from turtle import width
import fingertrackingmodule as ftm
import cv2
import mediapipe
import math
import os
import numpy as np

cap = cv2.VideoCapture(0)
width = 1920
height = 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
print()