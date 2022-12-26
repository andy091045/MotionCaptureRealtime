import cv2
import numpy as np
import os
import glob

# 選擇第一隻攝影機
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

while(True):
  # 從攝影機擷取一張影像
  ret, frame0 = cap0.read()
  ret, frame1 = cap1.read()

  # 顯示圖片
  cv2.imshow('frame0', frame0)
  cv2.imshow('frame1', frame1)

  # 若按下 c 鍵開始相機校正
  if cv2.waitKey(1)& 0xFF == ord('c'):
    print("camera calibration")

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap0.release()
cap1.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()