# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)


first_task_img_not_complete = Template(r"tpl1708666786391.png", threshold=0.9, record_pos=(-0.328, 0.015), resolution=(540, 1200))

first_task_img_completed = Template(r"tpl1708668170825.png", threshold=0.9, record_pos=(-0.33, 0.024), resolution=(540, 1200))


using("common.air")
using("auto_task.air")

from common import *



def clear_sub_tasks():

    #打开主面板
    open_tab("fight")
    
    #打开任务
    touch([0.5, 0.07])
    sleep(1)
    
    touch([0.5, 0.5])
    sleep(1)
    touch([0.5, 0.5])
    sleep(1)

    
    if exists(first_task_img_not_complete):
        #跳转任务
        touch([0.62, 0.65])
        sleep(2)
        clear_sub_tasks()
    elif exists(first_task_img_completed):
        #领取奖励
        touch([0.5, 0.65])
        sleep(1)
        clear_sub_tasks()

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    