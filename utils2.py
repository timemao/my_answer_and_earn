#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:57:30 2018

@author: timemao
"""
from selenium import webdriver
import numpy as np
from fuzzywuzzy import fuzz
import time
from re import sub
#suff_url="哪位帝王在即位之初设置了我国历史上第一个年号 汉武帚汉景帝"
#suff_url="老佛爷是来自于哪个家著名百货公司"
#suff_url="哪幅名画不是宋朝年间所作"
#suff_url="羊脂球被哪位作家称为可以流传于世杰作"
#suff_url="以下哪个选项的描述不属于五岳"
#answer=["意大利","法国","英国"]
#answer=["千里江山图","清明上河图","富春山居图"]
#answer=["福楼拜","莫泊桑","贾平凹"]
#answer=["一览众山小","方广寺深翠竹林","横看成岭侧成峰"]


    
def test_browser():
    driverlist=[driver,driver2,driver3]
    for wd in range(3):
        t=0
        driverper=driverlist[wd]
        for i in range(20):
            t1=time.time()
            driver3.get(url)
            t2=(time.time()-t1)
            t=t2+t
        print(t/20)
        print(driver.find_element_by_id("3").text)

def cluster_exclude(array):
    index_sort=sorted(range(len(array)), key=lambda k: array[k])
    dist01=array[index_sort[1]]-array[index_sort[0]]
    dist12=array[index_sort[2]]-array[index_sort[1]]
    if dist01>=dist12:
        return index_sort[0]
    else:
        return index_sort[2]



#count_disappear(suff_url,answer,driver)