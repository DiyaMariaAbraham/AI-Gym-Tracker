import mediapipe as mp
import streamlit as st
import cv2 as cv2
import tempfile
import numpy as np

def calcAngle(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle>180.0:
        angle = 360-angle
    return angle

bicep_count = 0
squat_count = 0
lat_count = 0
push_count = 0
sequence = []
message1 = ""
message2 = ""

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

option = st.selectbox(
        'Choose your exercise:',
        ('Push Ups', 'Squats', 'Lat Raises','Bicep Curls'))

f = st.file_uploader("Upload file")

if f is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(f.read())
    


    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()
    with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret,frame = cap.read()
            if frame is not None:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = pose.process(image)
            
                try:
                    landmarks = results.pose_landmarks.landmark
                    
                    if (option == "Squats"):
                        left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                        left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                        left_heel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]
                        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        
                        angle = calcAngle(left_hip,left_knee,left_heel)
                        angle_back = calcAngle(left_shoulder,left_hip,[left_hip[0],0])
                        
                        
                        if 160 < angle < 180:
                            state = "s1"
                            if len(sequence) == 0:
                                sequence.append(state)
                        
                        if 110 < angle< 155 :
                            state = "s2"
                            if (sequence[-1] != "s2"):
                                sequence.append(state)

                        
                        if 85 < angle < 109:
                            state = "s3"
                            if (sequence[-1] != "s3"):
                                sequence.append(state)
                        

                        if(sequence == ['s1','s2','s3','s2']):
                            squat_count+= 1
                            sequence = []      
                    
                    if (option == "Push Ups"):
                        shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                        wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                        shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                        elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                        wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                        left_heel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]
                        left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                        
                        angle_left = calcAngle(shoulder_left,elbow_left,wrist_left)
                        angle_right = calcAngle(shoulder_right,elbow_right,wrist_right)

                        angle_push = (angle_left + angle_right)/2
                        #print(sequence)
                        #print(angle_push)
                        angle_back = calcAngle(left_shoulder,left_hip,left_heel)

                        if 150 < angle_push < 180:
                            state = "s1"
                            print("entered if")
                            if len(sequence) == 0:
                                sequence.append(state)
                        
                        if 110 < angle_push < 1 :
                            state = "s2"
                            print("entered if2")
                            if (sequence[-1] != "s2"):
                                sequence.append(state)

                        
                        if 90 < angle_push < 105:
                            state = "s3"
                            if (sequence[-1] != "s3"):
                                sequence.append(state)

                            if   angle_back < 110:
                                message = "lower hips"
                            elif angle_back > 130:
                                message = "raise hips"
                            else:
                                message = "perfect"

                        #print(sequence) 
                        if(sequence == ['s1','s2','s3','s2']):
                            push_count += 1
                            sequence = []
                        #print(push_count)
                    
                    if (option == "Lat Raises"):
                        right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                        shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                        elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]

                        left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                        shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                        angle_right = calcAngle(right_hip,shoulder_right,elbow_right)
                        angle_left = calcAngle(left_hip,shoulder_left,elbow_left)

                        angle = (angle_left + angle_right)/2
                        print(angle)

                        if 0 < angle < 20:
                            state = "s1"
                            if len(sequence) == 0:
                                sequence.append(state)
                        
                        if 21 < angle < 70 :
                            state = "s2"
                            if (sequence[-1] != "s2"):
                                sequence.append(state)

                        if 71 < angle < 110:
                            state = "s3"
                            if (sequence[-1] != "s3"):
                                sequence.append(state)

                            if   angle > 90:
                                message1 = "lower arms"
                            elif 71 < angle < 79:
                                message1 = "raise arms"
                            else:
                                message1 = "perfect"

                        print(sequence) 
                        if(sequence == ['s1','s2','s3','s2']):
                            lat_count += 1
                            sequence = []
                        #print(push_count)

                    if (option == "Bicep Curls"):
                        shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                        elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                        wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
                        angle = calcAngle(shoulder,elbow,wrist)
                        print(angle)
                        if 170 < angle < 180:
                            state = "s1"
                            if len(sequence) == 0:
                                sequence.append(state)
                        
                        if  30 < angle < 169:
                            state = "s2"
                            if (sequence[-1] != "s2"):
                                sequence.append(state)

                        if 0 < angle < 29:
                            state = "s3"
                            if (sequence[-1] != "s3"):
                                sequence.append(state)

                            # if   angle > 90:
                            #     message = "lower arms"
                            # elif 71 < angle < 79:
                            #     message = "raise arms"
                            # else:
                            #     message = "perfect"

                        #print(sequence) 
                        if(sequence == ['s1','s2','s3','s2']):
                            bicep_count += 1
                            sequence = []
                        



                except:
                    pass

                finally:
                    cv2.rectangle(image,(90,50),(400,310),(0,0,0),-1)

                    cv2.putText(image,f'Bicep Curl Count: {bicep_count}',(100,100),cv2.FONT_HERSHEY_COMPLEX,0.5,
                                    (0,0,250),2,cv2.LINE_4)
                    cv2.putText(image,f'Squat Count: {squat_count}',(100,140),cv2.FONT_HERSHEY_COMPLEX,0.5,
                                    (0,0,250),2,cv2.LINE_4)
                    cv2.putText(image,f'Lat Raises Count: {lat_count}',(100,180),cv2.FONT_HERSHEY_COMPLEX,0.5,
                                    (0,0,250),2,cv2.LINE_4)
                    cv2.putText(image,f'PushUp Count: {push_count}',(100,220),cv2.FONT_HERSHEY_COMPLEX,0.5,
                                    (0,0,250),2,cv2.LINE_4)
                    
                    #cv2.rectangle(image,(90,50),(300,120),(0,0,0),-1)
                    cv2.putText(image,message1,(100,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2,cv2.LINE_4)
                    cv2.putText(image,message2,(100,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2,cv2.LINE_4)
                    message1 = " "
                    message2 = " "
                
                mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
                image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
                stframe.image(image)
                #cv2.imshow('Feed',image)