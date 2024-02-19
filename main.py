import cv2
import mediapipe as mp
import pyautogui
hand_detector = mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
cap=cv2.VideoCapture(0)
index_y=0
midf_y=0

while True:
    success, frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_=frame.shape
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output= hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                if id==8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_x=(screen_width/frame_width)*x
                    index_y=(screen_height/frame_height)*y
                    pyautogui.moveTo(index_x+50,index_y+50)
                if id==12:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    midf_x=(screen_width/frame_width)*x
                    midf_y=(screen_height/frame_height)*y
                    print(abs(index_y-midf_y))
                    if abs(index_y-midf_y)<100:
                        print("click")
                        pyautogui.click()
                        pyautogui.sleep(2)
    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1)