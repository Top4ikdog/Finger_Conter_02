from asyncio import Transport
from re import X
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)  # подключаемся к web-камере
mp_Hands = mp.solutions.hands  # хотим распознавать руки (hands)
# характеристики для распознавания
hands = mp_Hands.Hands(
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=4)
mpDraw = mp.solutions.drawing_utils  # утилита для рисования
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]  # координаты интересующих точек у пальцев (кроме большого)
thumb_Coord = (4, 3)  # координаты интересующих точек большого пальца

while cap.isOpened():  # пока камера "работает"
    success, image = cap.read()  # полчаем кадр с web-камеры (True/False, image)
    prevTime = time.time()
    if not success:  # если не удалось получить кадр
        print("Не удалось получить изображение с web-камеры")
        continue  # переход к ближайшему циклу (while)
    
    image = cv2.flip(image, 1)  # зеркальное отражение картинки

    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR -> RGB
    result = hands.process(RGB_image)  # ищем руки
    if result.multi_hand_landmarks:  # если найдены руки
        multiLandMarks = result.multi_hand_landmarks  # извлекаем список найденных рук
        upCount = 0 # кол-во "поднятых" пальцев
        for idx, handLms in enumerate(multiLandMarks):
            lbl = result.multi_handedness[idx].classification[0].label
            print(lbl)

            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)  # рисуем "маску" руки
            handList = [] # Список координат пальцев в пикселях
            for lm in handLms.landmark:
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handList.append((cx, cy))
            side = 'left'
            if  handList[5][0]  > handList[17][0]:
                side = 'right'

            for coordinate in finger_Coord:
                if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                    upCount += 1
            

            if side == 'left':

                if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                    upCount += 1
            else:
                if handList[thumb_Coord[0]][0]< handList[thumb_Coord[1]][0]:
                    upCount += 1

        print(upCount)
        cv2.putText(image, str(upCount), (50, 100), cv2.FONT_HERSHEY_PLAIN, 8, (255, 225, 255), 8)
        cv2.putText(image, str(lbl), (200, 100), cv2.FONT_HERSHEY_PLAIN, 8, (255, 225, 255), 8)



    currentTime = time.time()
    fps = 1 / (currentTime - prevTime)
    cv2.putText(image, f'FPS: {fps}', (350, 475), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
    cv2.imshow('image', image)
    if cv2.waitKey(1) &  0xFF == 27:  # esc
        break

cap.release()