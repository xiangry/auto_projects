# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *



auto_setup(__file__)

using("common.air")

from common import *

ST.FIND_TIMEOUT=0.1  #设置隐式等待时长
ST.THRESHOLD = 0.9



task_entrance_pos = [0.5, 0.078]
main_task_pos = [0.5, 0.35]
sub_task_pos = [0.5, 0.5]


un_complete_img = Template(r"tpl1708778601282.png", record_pos=(-0.343, 0.231), resolution=(540, 1200))


goto_img = Template(r"tpl1708779741282.png", record_pos=(0.002, 0.315), resolution=(540, 1200))


complete_btn_img = Template(r"tpl1708778943714.png", record_pos=(0.0, 0.32), resolution=(540, 1200))

task_panel_img = Template(r"tpl1708779859699.png", record_pos=(0.37, -0.287), resolution=(540, 1200))

sub_task_normal_img = Template(r"tpl1708780473178.png", record_pos=(-0.344, -0.248), resolution=(540, 1200))

task_sign_img = Template(r"tpl1708780725901.png", record_pos=(-0.326, -0.296), resolution=(540, 1200))



# 查找分支任务图标
un_complete_results = find_all(un_complete_img)

# if(un_complete_results == None):
#     print("找不到分支任务")
    
# sleep(1)
# first = un_complete_results[0]['result']

# 获取设备的高度和宽度
screen_width, screen_height = device().get_current_resolution()

sub_task_index = 0

def auto_accept_sub_task():
    
    open_tab("fight")
    # 打开任务菜单
    touch(task_entrance_pos)
    sleep(2)
    
    for i in range(3):
        touch([0.5, 0.72])
        sleep(1)


        task_results = find_all(sub_task_normal_img)

        for tryIndex in range(5):
            if task_results == None:
                swipe([0.5, 0.6], [0.5, 0.5])
                task_results = find_all(sub_task_normal_img)
                continue
            else:
                break
                
        if task_results == None:
            return False
                       
        

        first_pos = task_results[sub_task_index]['result']
        sleep(1)

        print("find task pos", task_results)
        touch([screen_width * 0.5, first_pos[1]])
        sleep(1)

        if exists(task_sign_img):
            touch([0.5, 0.64])
            sleep(1)  
            
    return True
    
    

# auto_accept_sub_task()


    


def auto_handle_sub_tasks():
    open_tab("fight")
    # 打开任务菜单
    touch(task_entrance_pos)
    sleep(2)
    touch(sub_task_pos)
    sleep(1)
    if exists(task_panel_img):
        if exists(goto_img):
            touch([0.64, 0.64])
            sleep(1)
        elif exists(complete_btn_img):
            touch([0.5, 0.64])
            sleep(1)
    else:
        auto_accept_sub_task()
        pass
    open_tab("fight")
    
    
    
def auto_handle_main_task():
    open_tab("fight")
    use_skill()
    # 打开任务菜单
    touch(task_entrance_pos)
    sleep(2)
    touch(main_task_pos)
    sleep(1)
    if exists(task_panel_img):
        if exists(goto_img):
            touch([0.64, 0.64])
            sleep(1)
        elif exists(complete_btn_img):
            touch([0.5, 0.64])
            sleep(1)
            if exists(Template(r"tpl1708860427128.png", record_pos=(-0.28, 0.194), resolution=(540, 1200))):
                touch([0.5, 0.75])
                sleep(1)

    else:
        pass
    open_tab("fight")
    
    
# while True:
#     auto_handle_main_task()
#     sleep(5)

    
index_cnt = 0
while True:
    auto_handle_sub_tasks()
    sleep(2)
    index_cnt = index_cnt + 1
    
    
    if index_cnt % 21 == 0:
        sell_quips()
        auto_handle_main_task()
    
















