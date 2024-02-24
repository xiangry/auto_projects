# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

using("common.air")

from common import use_skill
from common import sell_quips


auto_setup(__file__)




ST.FIND_TIMEOUT=0.1  #设置隐式等待时长
ST.THRESHOLD = 0.9


no_task_done = Template(r"tpl1708580549576.png", record_pos=(-0.181, -0.87), resolution=(1080, 2400))


go_stage_img = Template(r"tpl1708583142954.png", record_pos=(-0.065, 0.557), resolution=(1080, 2400))



done_imgs = [
   # Template(r"tpl1708513790302.png", record_pos=(-0.337, -0.289), resolution=(540, 1200)),
    Template(r"tpl1708513790302.png", record_pos=(-0.337, 0.024), resolution=(540, 1200)),
   # Template(r"tpl1708513790302.png", record_pos=(-0.337, 0.239), resolution=(540, 1200)),
   # Template(r"tpl1708513790302.png", record_pos=(-0.337, 0.461), resolution=(540, 1200)),
]

no_task_img = Template(r"tpl1708520450127.png", record_pos=(-0.001, 0.02), resolution=(1080, 2400))

normal_task_img = Template(r"tpl1708520592612.png", record_pos=(-0.353, -0.423), resolution=(1080, 2400))


task_not_complete = Template(r"tpl1708521801836.png", record_pos=(-0.368, -0.031), resolution=(1080, 2400))


# 获取设备的高度和宽度
width, height = device().get_current_resolution()


task_title_pos = [[0.5, 0.37], [0.5, 0.5], [0.5, 0.6], [0.5, 0.7], ]


def accept_task():
    sleep(0.5)
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    sleep(2)
    
    # 点击任务
    touch([0.5, 0.11])
    
    sleep(1)
    
    if exists(task_not_complete):
        jump_map()
        return
    
    # 领取任务
    touch([0.5, 0.5])
    sleep(3)
    
    if exists(normal_task_img):
        touch([0.5, 0.3])
    else:
        touch([0.5, 0.37])
        
    sleep(1)
    touch([0.5, 0.63])
    sleep(2)
    
    jump_map()
    
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    sleep(2)


def jump_map():
    sleep(1)
    touch([0.5, 0.5])
    sleep(2)
    touch([0.63, 0.64])
    sleep(2)
    if exists(go_stage_img):
        touch([0.5, 0.75])
        sleep(2)
    touch([0.33, 0.95])
    sleep(1)
    



loop_cnt = 0
while True:
    loop_cnt += 1
    
    #出售
    if loop_cnt % 20 == 0:
        sell_quips()
        
    accept_task()
    
    use_skill()
    
    # 打开任务面板
    sleep(1)
    touch([0.3, 0.1])
    sleep(2)

    for i in range(len(done_imgs)):
        result = exists(done_imgs[i])
        print("try find done", i, "result = ", result)
        if result :
            result2 = [width * 0.5,  result[1]]
            print("result2 = ", result2)
            touch(result2)
            sleep(2)

            touch([0.5, 0.64])
            sleep(2)
        else:
            if exists(task_not_complete):
                sleep(1)
                jump_map()
                sleep(1)
            break

    touch([0.33, 0.95])
    sleep(0.5)

