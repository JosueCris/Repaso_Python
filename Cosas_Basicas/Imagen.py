## Programa basico para mostrar una imagen
import cv2

m = cv2.imread("/home/josue/Descargas/fondo.png", 1)
cv2.imshow("fondo", m)
cv2.waitKey()
cv2.destroyAllWindows()