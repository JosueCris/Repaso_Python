import cv2
import numpy as np
from numpy.core.defchararray import array

def ordenar_puntos(puntos):
    n_puntos = np.concatenate(puntos[0], puntos[1], puntos[2], puntos[3]).tolist()
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
    contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_EXTRENAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key=cv2.contourArea, reverse=True)[0:1]
    for i in contorno:
        epsilon = 0.01*cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, epsilon, True)
        if(len(approx) == 4):
            puntos = ordenar_puntos(approx)
            puntoS1 = np.float32(puntos)
            puntoS2 = np.float32([[0, 0], [ancho, 0], [0, alto], [ancho, alto]])
            M = cv2.getPerspectiveTransform(puntoS1, puntoS2)
            imagen_alineada = cv2.warpPerspective(imagen, M, (ancho, alto))
    return imagen_alineada

capturarVideo = cv2.VideoCapture(0)
while(True):
    tipocamara, camara = cv2.capturarVideo.read()
    if(tipocamara == False):
        break
    imagenA6 = 