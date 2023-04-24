#import the imporant libs
import cv2 as cv
import numpy as np
import random
import math

#init the pargram 
image = np.zeros((100,200),dtype=np.uint8)
chang = random.randint(50,150)
kuan = random.randint(30,70)
jiaodu = random.randint(50,90)
#mean the chang rate should be a 30 
angle0 = math.radians(30)

angle = math.radians(jiaodu)

#get the draw line point
#use the int 
chang1 =(int)(chang+(15/math.tan(angle0))*math.cos(1.57-angle)) 
kuan1 = (int)(kuan-(15/math.tan(angle0))*math.sin(1.57-angle))

chang2 = (int)(chang-(15/math.tan(angle0))*math.cos(1.57-angle))
kuan2 = (int)(kuan+(15/math.tan(angle0))*math.sin(1.57-angle))

chang3 = (int)(chang+15*math.cos(angle))
kuan3 = (int)(kuan+15*math.sin(angle))

chang4 = (int)(chang-15*math.cos(angle))
kuan4 = (int)(kuan-15*math.sin(angle))

#draw the pic
cv.circle(image,(chang1,kuan1),3,(255),-1)
cv.circle(image,(chang2,kuan2),3,(255),-1)
cv.circle(image,(chang3,kuan3),3,(255),-1)
cv.circle(image,(chang4,kuan4),3,(255),-1)
#show the line
#cv2.line(image, (rx1, ry1), (rx2, ry2), (255), 2)
cv.line(image,(chang1,kuan1),(chang3,kuan3),(255),2)
cv.line(image,(chang2,kuan2),(chang4,kuan4),(255),2)
cv.line(image,(chang3,kuan3),(chang2,kuan2),(255),2)
cv.line(image,(chang4,kuan4),(chang1,kuan1),(255),2)
#show the pic
cv.imshow("black image",image)
cv.waitKey(0)
cv.destroyAllWindows()
