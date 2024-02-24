# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

using("common.air")
using("task_util.air")

from common import *
from task_util import *


task_img = Template(r"tpl1708665047592.png", threshold=0.9, target_pos=0, record_pos=(0.069, -0.298), resolution=(540, 1200))


accept_btn_img = Template(r"tpl1708666183740.png", record_pos=(0.002, 0.322), resolution=(540, 1200))


big_map_pos = [[0.12, 0.83], [0.26, 0.83], [0.42, 0.83], [0.58, 0.83], [0.72, 0.83], [0.86, 0.83]] 
def open_map_by_index(index):
    sleep(0.5)
    touch(big_map_pos[index])
    sleep(1)
    



def auto_do_xuanshang():
    #打开主面板
    open_tab("fight")

    #打开地图
    touch([0.5, 0.03])
    sleep(1)

    map_cnt = 6
    accept_cnt = 0;
    
    for i in range(map_cnt):
        open_map_by_index(i);

        screenshot = snapshot()

        question_marks = find_all(task_img)

        if question_marks == None:
            continue

        print("find img cnt = ", len(question_marks))


        if len(question_marks) == 0:
            continue

        isBreak = False
        for taskPos in question_marks:
            print(taskPos)
            touch(taskPos['result'])
            sleep(1)
            touch([0.87, 0.68])
            sleep(1)
            touch([0.5, 0.64])
            sleep(1)
            if exists(accept_btn_img):
                isBreak = True;
                open_tab("fight")
                break


            accept_cnt = accept_cnt + 1
            if accept_cnt >=3:
                isBreak = True
                break

        if isBreak:
            break

    
    clear_sub_tasks()
        

while True:
    sleep(1)
    auto_do_xuanshang()

        
        
        
    



