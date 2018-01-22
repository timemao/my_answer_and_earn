#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:16:08 2018

@author: timemao
"""

class Chong_ding():
    def __init__(self,float_down=2):
        self.time_money={'pm13_00':'','pm17_00':'','pm19_00':'','pm21_00':''}
        left_q,right_q=93,543
        left_s,right_s=125,381
        if float_down==1:
            self.box_question=[left_q, 266,right_q, 308]

            self.box_1=[left_s, 371,right_s, 405]
            self.box_2=[left_s, 450,right_s, 481]

        elif float_down==2:
            self.box_question=[left_q, 266,right_q, 351]

            self.box_1=[left_s, 414,right_s, 447]
            self.box_2=[left_s, 493,right_s, 525]

        elif float_down==3:
            self.box_question=[left_q, 266,right_q, 395]

            self.box_1=[left_s, 456,right_s, 493]
            self.box_2=[left_s, 536,right_s, 569]
       
        self.box_3=[left_s,2*self.box_2[1]-self.box_1[1], right_s,2*self.box_2[3]-self.box_1[3]]
        self.box_selection=[left_s,self.box_1[1],right_s, self.box_3[3]]

        self.number_start=1
        self.box_number=3