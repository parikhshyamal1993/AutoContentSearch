import sys , os
import cv2
import numpy as np
from pytesseract import image_to_string
import re


def panExtract(self,image):
        panColor = cv2.imread(image)
        panColor = cv2.resize(panColor,(1200,743))
        adjusted = cv2.convertScaleAbs(panColor, alpha=1.5, beta=0)
        panImage = cv2.imread(image,0)
        meanImg = panImage.mean()
        #panImage = panImage / meanImg
        print("panImage",panImage.shape)
        panImage = cv2.resize(panImage,(1200,743))
        _, mask = cv2.threshold(panImage,90,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        dst = cv2.dilate(mask,self.kernal,iterations = 1)
        dst = cv2.bitwise_not(dst) 
        kernel_ = cv2.getStructuringElement(cv2.MORPH_RECT,(31,5))
        clossing = cv2.morphologyEx((255-dst),cv2.MORPH_CLOSE,kernel_)
        contours , hierarchy = cv2.findContours(clossing,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
        allBoxes = []
        typeIDList = []
        for cnt , high in zip(contours,hierarchy[0]):
            x,y,w,h = cv2.boundingRect(cnt)
            if h > 20 and w >30 and x <550:
                cv2.rectangle(panColor,(x,y),(x+w,y+h),(0,255,100),3)
                cells = adjusted[y-5:y+h,x:x+w]
                gray = cv2.cvtColor(cells,cv2.COLOR_BGR2GRAY)
                data = image_to_string(cells,config='--psm 7')
                allBoxes.append([data,[x,y,x+w,y+h]])
        cv2.imshow("Binary",cv2.resize(panColor,(600,375)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        allBoxes.reverse()
        return allBoxes


if __name__=="__main__":
    print("Done")