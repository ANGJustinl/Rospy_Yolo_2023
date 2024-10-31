# ANGJustinl 2023.2.21
# coding=utf8
from ..yolov3_mobilenet import yolo_frame,yolo_detect
import logging


#解析yolo输出的list,分离图片中各个目标的坐标与标签,以准确率由大到小排序
def sort(input_):
    results = yolo_detect(input_)
    if results == None:
        logging.error("no input")
    data_raw = results[0]
    data_list = data_raw.get('data')
    label_dict = dict()

    #top bottom left right
    top_dict = dict()
    bottom_dict = dict()
    left_dict = dict()
    right_dict = dict()

    for i in range(len(data_list)):
        label_dict[i] = data_list[i]['label']
        top_dict[i] = data_list[i]['top']
        bottom_dict[i] = data_list[i]['bottom']
        left_dict[i] = data_list[i]['left']
        right_dict[i] = data_list[i]['right']
        
    logging.info('yolo_output---\n label/top/bottom/left/right')
    return label_dict,top_dict,bottom_dict,left_dict,right_dict

def sort_frame(input_):
    results = yolo_frame(input_)
    if results == None:
        logging.error("no input")
    data_raw = results[0]
    data_list = data_raw.get('data')
    label_dict = dict()

    #top bottom left right
    top_dict = dict()
    bottom_dict = dict()
    left_dict = dict()
    right_dict = dict()

    for i in range(len(data_list)):
        label_dict[i] = data_list[i]['label']
        top_dict[i] = data_list[i]['top']
        bottom_dict[i] = data_list[i]['bottom']
        left_dict[i] = data_list[i]['left']
        right_dict[i] = data_list[i]['right']
        
    logging.info('yolo_output---\n label/top/bottom/left/right')
    return label_dict,top_dict,bottom_dict,left_dict,right_dict