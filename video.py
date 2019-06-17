'''
Date :2019-05-06
Author: 林志帆
'''
import cv2
vc = cv2.VideoCapture("G:/MyStudy/Python/1.mp4")
i = 0
rate = 50 #保存频率
rval = vc.isOpened()
while rval:
      i += 1
      rval, frame = vc.read()
      if (i%rate == 0):
         cv2.imwrite("G:/MyStudy/Python/images3/"+str(i)+".jpg", frame)
vc.release()
