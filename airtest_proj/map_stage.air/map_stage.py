# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
auto_setup(__file__)

using("common.air")

from common import *


ST.FIND_TIMEOUT=0.5  #设置隐式等待时长
ST.THRESHOLD = 0.9

activeImg = Template(r"tpl1708483834845.png", record_pos=(-0.424, -0.897), resolution=(1080, 2400))

ticket = Template(r"tpl1708493932287.png", record_pos=(-0.043, 0.556), resolution=(1080, 2400))

stage_detail = Template(r"tpl1708493982680.png", record_pos=(-0.277, 0.265), resolution=(1080, 2400))

mapEntrance = [0.074, 0.162]
mapEntrance1 = [0.222, 0.244]

map_stage = [
    [0.70, 0.65],
    [0.30, 0.65],
    [0.70, 0.55],
    [0.30, 0.55],
    [0.70, 0.45],
    [0.30, 0.45],
    [0.70, 0.35],
    [0.30, 0.35],
    [0.70, 0.25],
    [0.30, 0.25],
]


map_pos = [[0.12, 0.75], [0.26, 0.75], [0.4, 0.75], [0.56, 0.75], [0.72, 0.86]]
def open_stage_list(mapIndex, isTop):
    
    while True:
        if exists(activeImg):
            break;
        else:
            sleep(2.0)
    
    touch(mapEntrance)
    
    sleep(0.1)
    
    touch(mapEntrance1)
    
    sleep(2)
    
    if exists(Template(r"tpl1708493519159.png", record_pos=(0.085, -0.612), resolution=(1080, 2400))):
        touch(map_pos[mapIndex])
        sleep(1)
        if isTop:
            swipe([0.5, 0.3], [0.5, 0.6])
        else:
            swipe([0.5, 0.6], [0.5, 0.3])
        sleep(1)
    else:
        open_stage_list(mapIndex, isTop)
        
        
def challenge_map_stage(mapIndex, stageIds, isTop):
    
    sell_quips()
    
    open_stage_list(mapIndex, isTop)
    
    sleep(0.2)
    
    for i in stageIds:
        pos = map_stage[i-1]
        
        touch(pos)
        
        sleep(0.5)
        
        tryCnt = 0
        while True:
            if exists(stage_detail):
                break
            else:
                sleep(1)
                tryCnt = tryCnt + 1
                if(tryCnt > 5):
                    break
        
        if exists(ticket):
            touch([0.5, 0.95])
            continue
        else:
            touch([0.5, 0.75])
            

        while True:
            if exists(activeImg):
                open_stage_list(mapIndex, isTop)
                break
            else:
                use_skill()
                
    
    # 回到首页
    touch([0.5,0.95])
    sleep(0.1)
    touch([0.5,0.95])
    sleep(0.1)
        

    
    
hero_challenge = [
    [0, 4], #战士
    [1, 4], #法师
    [2, 2], #盗贼
    [3, 4], #猎人
    [4, 4], #圣骑士
    [5, 4], #术士
    [6, 2], #德鲁伊
    [7, 2], #萨满祭司
    [8, 2], #牧师
    [9, 4], #死亡骑士
]


map_times1 = [
    [1,2,3,4],
    [1,2,3,4,5,6,7],
    [2,3,4,5],
    [2,3,4,5,8],
    [2,3,4,5],
    [1,2,3,4],
    [1,2,3,4],
]

map_times2 = [
    [],
    [8],
    [10],
    [10],
    [],
    [],
]

hero_pos = [
    [0.15, 0.6], [0.32, 0.6], [0.5, 0.6], [0.68, 0.6], [0.84, 0.6], 
    [0.15, 0.7], [0.32, 0.7], [0.5, 0.7], [0.68, 0.7], [0.84, 0.7], 
]


def switch_hero(index):
    # 回到首页
    touch([0.5,0.95])
    sleep(0.5)
    touch([0.5,0.95])
    sleep(0.5)
        
    touch([0.95,0.09])
    sleep(2)
    touch([0.5, 0.73])
    
    sleep(3)
    touch(hero_pos[index])
    sleep(2)
    touch([0.5, 0.51])
    
    while True:
        if exists(activeImg):
            break
        else:
            sleep(2)
        
    

for i in range(len(hero_challenge)):
    info = hero_challenge[i]

    switch_hero(info[0])
    
    mapCnt = info[1]
    
    index = 0
    challenge_map_stage(index, map_times1[index], False)
    challenge_map_stage(index, map_times2[index], True)
    if(mapCnt == index + 1 ):
        continue
        
    index = index + 1
    challenge_map_stage(index, map_times1[index], False)
    challenge_map_stage(index, map_times2[index], True)
    if(mapCnt == index + 1 ):
        continue
        
    index = index + 1
    challenge_map_stage(index, map_times1[index], False)
    challenge_map_stage(index, map_times2[index], True)
    if(mapCnt == index + 1 ):
        continue
        
    index = index + 1
    challenge_map_stage(index, map_times1[index], False)
    challenge_map_stage(index, map_times2[index], True)
    if(mapCnt == index + 1 ):
        continue
        
    index = index + 1
    challenge_map_stage(index, map_times1[index], False)
    challenge_map_stage(index, map_times2[index], True)
    if(mapCnt == index + 1 ):
        continue


