import cv2
import numpy as np
def ordenar_puntos(puntos):
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    y_order = sorted(n_puntos, key=lambda n_puntos:n_puntos[1])
    x1_order = y_order[0:2]
    x1_order = sorted(x1_order, key=lambda x1_order:x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order:x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]
def alineamiento(imagen, ancho, alto):
    imagen_alineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tipoumbral, umbral = cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("Umbral", umbral)
    contorno = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key=cv2.contourArea, reverse=True)[0:1]
    for i in contorno:
        epsilon = 0.01*cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, epsilon, True)
        if len(approx) == 4:
            puntos = ordenar_puntos(approx)
            puntoS1 = np.float32(puntos)
            puntoS2 = np.float32([[0, 0], [ancho, 0], [0, alto], [ancho, alto]])
            M = cv2.getPerspectiveTransform(puntoS1, puntoS2)
            imagen_alineada = cv2.warpPerspective(imagen, M, (ancho, alto))
    return imagen_alineada
capturarVideo = cv2.VideoCapture(0)

while True:
    tipocamara, camara = capturarVideo.read()
    if tipocamara == False:
        break
    imagenA6 = alineamiento(camara, ancho=1080, alto=720)
    if imagenA6 is not None:
        puntos = []
        grises2 = cv2.cvtColor(imagenA6, cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(grises2, (5, 5), 1)
        tipoumbral2, umbral2 = cv2.threshold(gauss, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("Umbral 2", umbral2)
        contorno2 = cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagenA6, contorno2, -1, (255, 0, 0), 2)
        suma1 = 0.0
        suma2 = 0.0
        suma5 = 0.0
        suma10 = 0.0
        for j in contorno2:
            area = cv2.contourArea(j)
            momentos = cv2.moments(j)
            if momentos["m00"] == 0:
                momentos["m00"] = 1.0
            x = int(momentos["m10"] / momentos["m00"])
            y = int(momentos["m01"] / momentos["m00"])

            if area<9000 and area>7000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagenA6, "$10 MXN", (x, y), font, 0.75, (0, 255, 0), 2)
                suma10 = suma10+10

            if area<6999 and area>6000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagenA6, "$5 MXN", (x, y), font, 0.75, (0, 255, 0), 2)
                suma5 = suma5 + 5

            if area<5999 and area>5000:
                 font = cv2.FONT_HERSHEY_SIMPLEX
                 cv2.putText(imagenA6, "$2 MXN", (x, y), font, 0.75, (0, 255, 0), 2)
                 suma2 = suma2 + 2

            if area<4999 and area>4000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagenA6, "$2 MXN", (x, y), font, 0.75, (0, 255, 0), 2)
                suma1 = suma1 + 1

        total = suma10+suma5+suma2+suma1
        print(f"Cantidad: ${round(total, 2)} MXN")
        cv2.imshow("Imagen A6", imagenA6)
        cv2.imshow("Camara", camara)
    if cv2.waitKey(1) == ord("s"):
        break

capturarVideo.release()
cv2.destroyAllWindows()