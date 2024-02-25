# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

skill_pos = [
    [0.15, 0.55], [0.32, 0.55], [0.5, 0.55], [0.68, 0.55], [0.84, 0.55], 
    [0.15, 0.62], [0.32, 0.62], [0.5, 0.62], [0.68, 0.62], [0.84, 0.62], 
    [0.15, 0.7],  [0.32, 0.7],  [0.5, 0.7],  [0.68, 0.7],  [0.84, 0.7], 
]

def use_skill():
    touch([0.5,0.95])
    sleep(0.1)
    touch([0.5,0.95])
    sleep(0.1)
    touch([0.5,0.95])
    sleep(0.1)
    touch([0.5,0.95])
    sleep(0.1)
    touch([0.5,0.95])
    sleep(0.1)
    touch([0.5,0.95])
    sleep(0.1)
    for i in range(len(skill_pos)):
        touch(skill_pos[i])
        sleep(0.1)


def sell_quips():
    sleep(0.5)
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    touch([0.33, 0.95])
    sleep(2)
    
    #批量出售
    touch([0.65, 0.88])
    sleep(2)
    
    #出售
    touch([0.75, 0.72])
    sleep(1)
    
    #选择全部
    touch([0.5, 0.72])
    sleep(1)
    
    #出售
    touch([0.75, 0.72])
    sleep(1)
    
    #确认
    touch([0.5, 0.57])
    sleep(1)
    
    touch([0.33, 0.95])
    sleep(0.5)
    
    
    
   

tab_pos = [[0.1, 0.95], [0.3,0.95], [0.5, 0.95], [0.7, 0.95], [0.7, 0.95]]
def open_tab(tabName):
    pos = tab_pos[0]
    if tabName == "fight":
        pos = tab_pos[2]
    elif tabName == "equip":
        pos = tab_pos[1]
    else:
        pos = tab_pos[tabName]
        
    
    sleep(0.5)
    touch(pos)
    touch(pos)
    touch(pos)
    sleep(0.5)

    

