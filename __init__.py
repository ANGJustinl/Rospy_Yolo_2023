# ANGJustinl 2023.2.21
# coding=utf8
from  yolov3 import *

import json
import os
import rospy
from std_msgs.msg import String
import time
import cv2
import logging

def Yolo_Publisher():
    video_capture = cv2.VideoCapture(0)

    result_path = './results'
    if not os.path.exists(result_path):
        os.mkdir(result_path)

    raw_path = "./results/1_yolo_raw.avi"
    width = 640
    height = 480
    fps = 1
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    writer = cv2.VideoWriter(raw_path, fourcc, fps, (width, height))

    pub = rospy.Publisher('YoloDetect', String, queue_size=1)

    rospy.init_node('PaddleYolo', anonymous=True)

    rospy.sleep(0.2)
    index = 0
    data = []

    yolo_init()

    while not rospy.is_shutdown():
        if not video_capture.isOpened():
            logging.error('Yolo cant open camra')
            time.sleep(4)
            pass
        yoloIndex = 0
        index+=1
        # 读视频帧
        frameData = {}
        ret, frame = video_capture.read()
        if ret == False:
            break
        if index%2==0:
            continue
        frame_copy = frame.copy()
        
        results = sort_frame(frame)
        json_results = json.dumps(results)
        pub.publish(json_results) #     publish

        for i in results[0]:
            label = results[0][i]
            top = int(results[1][i])
            bottom = int(results[2][i])
            left = int(results[3][i])
            right = int(results[4][i])
            color = (0, 255, 0)
            cv2.rectangle(frame_copy, (left, top), (right, bottom), color, 3)
            cv2.putText(frame_copy, label, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
        yoloIndex += 1

        cv2.imshow('yoloDetection', frame_copy)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # with open("./result/2-mask_detection.json", "w") as f:
    #     json.dump(data, f)

    writer.release()
    # 关闭摄像头设备
    video_capture.release()

    # 关闭所有窗口
    cv2.destroyAllWindows()
