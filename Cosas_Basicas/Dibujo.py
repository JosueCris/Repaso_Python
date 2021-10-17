from typing import Text
import cv2
import numpy as np

img = np.zeros((300, 300, 3))

cv2.line(img, (0,0), (300,300), (255,0,0), 3)
cv2.rectangle(img, (60,30), (120,60), (0,255,0), -1)
cv2.circle(img, (150,150), 50, (0,0,255), -1)

Texto = "Josue Tellez"
fuente = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

cv2.putText(img, Texto, (30,220), fuente, 1, (255,255,0), 2)

cv2.imshow("Dibujos", img)
cv2.waitKey()