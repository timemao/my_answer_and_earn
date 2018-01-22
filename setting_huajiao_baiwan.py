#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:16:22 2018

@author: timemao
"""

class Huajiao_baiwan():
    def __init__(self,float_down=2):
        self.time_money={'pm13_30':'58','pm16_30':'58','pm19_30':'188','pm20_30':'188'\
                         ,'pm21_30':'388','pm22_30':'200'}
        left_q,right_q=123,515
        left_s,right_s=105,382
        if float_down==1:
            self.box_question=[left_q, 311,right_q, 356]

            self.box_1=[left_s, 419-4,right_s, 450+4]
            self.box_2=[left_s, 500-4,right_s, 531+4]

        if float_down==2:
            self.box_question=[left_q, 311,right_q, 396]

            self.box_1=[left_s, 463-4,right_s, 495+4]
            self.box_2=[left_s, 542-4,right_s, 572+4]

        if float_down==3:
            self.box_question=[left_q, 311,right_q, 436]

            self.box_1=[left_s, 505-4,right_s, 537+4]
            self.box_2=[left_s, 587-4,right_s, 613+4]

        if float_down==4:
            self.box_question=[left_q, 311,right_q, 475]

            self.box_1=[left_s, 549-4,right_s, 578+4]
            self.box_2=[left_s, 627,right_s, 658]

        elif float_down==5:
            self.box_question=[left_q, 311,right_q, 475]

            self.box_1=[left_s, 589,right_s, 620]
            self.box_2=[left_s, 669,right_s, 701]            

        self.box_3=[left_s,2*self.box_2[1]-self.box_1[1], right_s,2*self.box_2[3]-self.box_1[3]]
        self.box_selection=[left_s,self.box_1[1],right_s, self.box_3[3]]

        self.number_start=1
        self.box_number=3