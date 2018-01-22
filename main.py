#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:16:58 2018

@author: timemao
"""
from setting_chong_ding import Chong_ding
from setting_huajiao_baiwan import Huajiao_baiwan
from setting_xi_gua import Xi_gua
from setting_zhi_shi import Zhi_shi
from setting_wechat import Brain_king
from utils import web_search,solution_once,correct_text_two
import time
import sys
from selenium import webdriver
#execu_path0='/home/timemao/Downloads/github/pythonselenium/phantomjs'
execu_path1='/home/timemao/Downloads/github/pythonselenium/geckodriver'
execu_path2='/home/timemao/Downloads/github/pythonselenium/chromedriver'
#driver=webdriver.Firefox(executable_path=execu_path)
#driver2=webdriver.Chrome(executable_path=execu_path)
def main_brain_king():
    for i in range(2):
        solution_once()
        correct_text_two()
def main_earn(now_time,driver1,driver2,float_down):
    #box=Chong_ding(float_down)
    #box=Xi_gua()
    #box=Zhi_shi()
    box=Huajiao_baiwan(float_down)
    web_search(box,now_time,driver1,driver2,is_debug=0)
    
if __name__=='__main__':
    is_brain_king=0
    if is_brain_king:
        main_brain_king()
    else:
        # 1.name
        # 2.box
        # 3.float_down
        #print(len(sys.argv))
        #float_down=int(sys.argv[1])
        #driver=webdriver.Firefox(executable_path=execu_path1)
        #driver1=webdriver.Chrome(executable_path=execu_path2)
        #driver2=webdriver.Chrome(executable_path=execu_path2)
        float_down=2
        now_time=time.time()
        main_earn(now_time,driver1,driver2,float_down)