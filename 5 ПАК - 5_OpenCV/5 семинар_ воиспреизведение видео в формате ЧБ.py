import cv2
import numpy as np

path = r'E:/УЧЕБА/УЧЕБА НГУ/2 КУРС/1 СЕМЕСТР/ПИТОН/СЕМИНАРЫ/Задание_5 семинар/Видео для задание с ЧБ (оригинал).mp4'
cap = cv2.VideoCapture(path) #Захват видео из файла

#Чтение каждого кадра из видео
while True:
    ret, frame = cap.read() #прочитан ли кадр
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # перевод в серый
    cv2.imshow('Gray Video', gray) #отбражение изображения в окошке

    if cv2.waitKey(28) & 0xFF == 27: #выход по кнопки esc
        break

#освободить ресурсов
cap.release()
cv2.destroyAllWindows()

