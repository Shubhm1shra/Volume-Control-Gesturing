from cvzone.HandTrackingModule import HandDetector
import cv2
from colorama import init
from termcolor import colored
import pyautogui as gui

init()

class VolumeControl:
    def __init__(self) -> None:
        gui.press('volumedown', 50)
        self.curVolume = 0

    def setMINVolume(self):
        gui.press('volumedown', 50)

    def setMAXVolume(self):
        gui.press('volumeup', 50)

    def setVolume(self, Volume):
        if Volume == 0: 
            self.setMINVolume()
            return 0
        elif Volume == 100:
            self.setMAXVolume()
            return 100

        if self.curVolume > Volume: gui.press('volumedown', int((self.curVolume - Volume)//2))
        elif self.curVolume < Volume: gui.press('volumeup', int((Volume - self.curVolume)//2))
        else: pass

        return Volume
    
    def displayVolume(self, length):
        length = length if length != None else 0
        Volume = int(length//2) if length < 200 else 100

        self.curVolume = self.setVolume(Volume)
        
        if Volume > 70: color = "red"
        elif Volume > 50: color = "yellow"
        else: color = "green"

        print("Volume : ", colored(str(Volume)+"%", color))
    
    def run(self, show=True):
        cap = cv2.VideoCapture(0)
        detector = HandDetector(detectionCon=0.8, maxHands=1)

        while True:
            success, img = cap.read()
            hands, img = detector.findHands(img)
            length = None

            if hands:
                hand1 = hands[0]
                lmList1 = hand1["lmList"]  #--> List of 21 Landmark points
                bbox1 = hand1["bbox"]  #--> Bounding box info x,y,w,h
                centerPoint1 = hand1['center']  #--> center of the hand cx,cy
                handType1 = hand1["type"]  #--> Left or Right

                fingers1 = detector.fingersUp(hand1)

                if (fingers1[0] and fingers1[1]):
                    length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[4][0:2], img)

            self.displayVolume(length)

            if show: cv2.imshow("Image", img)
            cv2.waitKey(1)

if __name__ == '__main__':
    VolumeControl().run(show=True)
