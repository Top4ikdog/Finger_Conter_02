
import cv2
import mediapipe  as mp
cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(
    model_complexity = 0,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5,
    max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4,2)


while cap.isOpened():
    success ,image = cap.read()
    if not success:
        print('Не удалось получть изображение  камере ')
        continue

    
    image = cv2.flip(image,1)
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result  =hands.process(RGB_image)
    if result.multi_hand_landmarks:
        
        miltiLandMarks =result.multi_hand_landmarks
        for idx, landLms in enumerate(miltiLandMarks):
            lbl = result.multi_handedness[idx].classification[0].label
            print(lbl)
        upCount = 0
        for handLms in miltiLandMarks:
            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            handlist = []
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy  = int(lm.x * w), int(lm.y * h)
                handlist.append((cx, cy))
            for coordinate in finger_Coord:
                if handlist[coordinate[0]][1] < handlist[coordinate[1]][1]:
                    upCount += 1
            if handlist[thumb_Coord[0]][0] > handlist[thumb_Coord[1]][0]:
                    upCount += 1

            print(upCount)
                






    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()

