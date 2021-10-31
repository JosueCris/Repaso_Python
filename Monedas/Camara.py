import cv2

capturarVideo = cv2.VideoCapture(0)
if (not capturarVideo.isOpened):
    print("No se encontro ninguna camara")
    exit()
while(True):
    tipocamara, camara = capturarVideo.read()
    grises = cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY)
##    gauss = cv2.GaussianBlur(grises, (3, 3), 0)  
##    canny = cv2.Canny(gauss, 60, 100)  
    cv2.imshow("Camara", camara)
    if(cv2.waitKey(1) == ord("s")):
        break
capturarVideo.release()
cv2.destroyAllWindows