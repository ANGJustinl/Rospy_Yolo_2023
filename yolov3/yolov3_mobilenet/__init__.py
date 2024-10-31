# ANGJustinl 2023.2.21
# coding=utf8
import paddlehub as hub
import cv2
import os
import logging
'''
def object_detection(paths=None,
                     images=None,
                     batch_size=1,
                     use_gpu=False,
                     output_dir='detection_result',
                     score_thresh=0.5,
                     visualization=True)
'''

def yolo_init():
    global object_detector
    object_detector = hub.Module(name="yolov3_mobilenet_v1_coco2017") # paddle 
    
def yolo_detect(input_):
    if os.path.exists(input_): # check input type
        input_path = input_
        try: 
            result = object_detector.object_detection(images=[cv2.imread(input_path)],visualization=True) # use path
            return result
        except Exception as e:
            logging.error(e)
            pass
    else:
        if type(input_) != str :
            try:
                result = object_detector.object_detection(images=input_,visualization=True) # use image
                logging.info('ang_yolo finished')
                return result
            except Exception as e:
                logging.error(e)
            pass
        else:
            logging.error('no image')
            pass

def yolo_detect_path(input_):
    if os.path.exists(input_):
        try:
            result = object_detector.object_detection(images=[cv2.imread(input_)])
            logging.info(result)
        except Exception as e:
            logging.error(e)
        return result 
    else:
            logging.error('no input')
            pass

def yolo_frame(inputs):
    try:
        result = object_detector.object_detection(images=[inputs],visualization=True) # use image
        logging.info('ang_yolo finished')
        return result
    except Exception as e:
        logging.error(e)