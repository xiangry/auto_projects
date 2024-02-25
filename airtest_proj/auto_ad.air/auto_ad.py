# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)


# 领额外挂机奖励
receive_cnt = 2

for i in range(receive_cnt):
    sleep(1)
    touch([0.5, 0.87])
    sleep(3)
#     touch([0.68, 0.68])
#     sleep(1)
    touch([0.34, 0.68])
    sleep(1)
    touch([0.5, 0.55])
    sleep(1)
    sleep(40)
    
    touch([0.0877, 0.095])
    sleep(3)
    sleep(1)
    touch([0.5, 0.96])
    sleep(1)
    touch([0.5, 0.96])
    sleep(1)
    touch([0.5, 0.96])