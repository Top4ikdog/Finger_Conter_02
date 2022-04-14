from asyncio import Transport
from re import S, X
import cv2
import mediapipe as mp
import time

class HandDetector():
    def __init__(self, mode=False, maxHands= 2, modelCompexity=1, detection=0.5, track=0.5 ):
        self.mp_Hands = mp.solutions.hands
        self.hands = self.mp_Hands.Hands(mode=False, maxHands= 2, modelCompexity=1, detection=0.5, track=0.5)
        self.mpDraw = self.mp.solutions.drawing_utils

    def FindHands(self, img):
        RGB_image = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(

    def FindPosition(self):
        pass

