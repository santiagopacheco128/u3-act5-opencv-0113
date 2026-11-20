# Santiago Pacheco NC 0113
import cv2
import numpy as np

# --- 1. MOSTRAR IMAGEN ORIGINAL ---
# Leer la imagen desde el archivo
imagen = cv2.imread('gato.png')
# Mostrar la imagen en una ventana
cv2.imshow('1. Original - Santiago Pacheco 0113', imagen)
# Esperar una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 2. ESCALA DE GRISES ---
# Cargar la imagen
imagen = cv2.imread('gato.png')
# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Mostrar la imagen en gris
cv2.imshow('2. Escala de grises - Santiago Pacheco 0113', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 3. REDIMENSIONAR ---
# Cargar la imagen
imagen = cv2.imread('gato.png')
# Cambiar tamaño a 300x200 píxeles
imagen_redimensionada = cv2.resize(imagen, (300, 200))
# Mostrar la imagen redimensionada
cv2.imshow('3. Redimensionada (300x200) - Santiago Pacheco 0113', imagen_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 4. ROTAR IMAGEN ---
# Cargar la imagen
imagen = cv2.imread('gato.png')
# Obtener alto y ancho de la imagen
(h, w) = imagen.shape[:2]
# Definir el centro de la imagen
centro = (w // 2, h // 2)
# Crear matriz de rotación (90 grados)
matriz = cv2.getRotationMatrix2D(centro, 90, 1.0)
# Aplicar la rotación
imagen_rotada = cv2.warpAffine(imagen, matriz, (w, h))
# Mostrar la imagen rotada
cv2.imshow('4. Rotada 90 grados - Santiago Pacheco 0113', imagen_rotada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 5. DESENFOQUE (BLUR) ---
# Cargar la imagen
imagen = cv2.imread('gato.png')
# Aplicar desenfoque gaussiano
imagen_desenfocada = cv2.GaussianBlur(imagen, (15, 15), 0)
# Mostrar la imagen desenfocada
cv2.imshow('5. Desenfocada - Santiago Pacheco 0113', imagen_desenfocada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 6. DETECCIÓN DE BORDES ---
# Cargar la imagen
imagen = cv2.imread('gato.png')
# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Detectar bordes con Canny
bordes = cv2.Canny(imagen_gris, 100, 200)
# Mostrar imagen de bordes
cv2.imshow('6. Deteccion de bordes - Santiago Pacheco 0113', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 7. DIBUJAR FIGURAS Y TEXTO ---
# Cargar la imagen
imagen = cv2.imread('gato.png')
# Dibujar un rectángulo azul
cv2.rectangle(imagen, (50, 50), (200, 200), (255, 0, 0), 3)
# Agregar texto verde a la imagen
cv2.putText(imagen, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# Mostrar imagen editada
cv2.imshow('7. Figuras y texto - Santiago Pacheco 0113', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 8. UMBRALIZACIÓN (BLANCO Y NEGRO PURO) ---
# Cargar la imagen directamente en grises
imagen = cv2.imread('gato.png', 0)
# Aplicar umbralización binaria
_, imagen_umbral = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)
# Mostrar imagen umbralizada
cv2.imshow('8. Umbralizacion - Santiago Pacheco 0113', imagen_umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- 9. DETECTAR Y DIBUJAR CONTORNOS ---
# Cargar la imagen
imagen = cv2.imread('gato.png')
# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Buscar bordes
bordes = cv2.Canny(imagen_gris, 100, 200)
# Encontrar los contornos
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Dibujar contornos verdes sobre la imagen original
cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)
# Mostrar imagen con contornos
cv2.imshow('9. Contornos - Santiago Pacheco 0113', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
