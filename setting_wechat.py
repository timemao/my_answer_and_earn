#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:33:45 2018

@author: timemao
"""
class Brain_king():
    def __init__(self):
        self.time_money={'anytime'}
        self.box_questiion=[120, 398,498, 500]
        self.box_number=4
        self.box_1=[206, 558,434, 633]
        self.box_2=[self.box_1[0], 652,self.box_1[2], 726]
        self.box_3=[self.box_1[0], self.box_2[1]+(self.box_2[1]-self.box_1[1]),self.box_1[2], self.box_2[3]+(self.box_2[3]-self.box_1[3])]
        self.box_4=[self.box_1[0], self.box_3[1]+(self.box_2[1]-self.box_1[1]),self.box_1[2], self.box_3[3]+(self.box_2[3]-self.box_1[3])]
        self.box_selection=[self.box_1,self.box_2,self.box_3,self.box_4]
        self.answer_color=[208,212]

        self.box_start=[198, 429,311, 461]
        self.box_continue=[263, 750,388, 786]
        self.box_chuxian=[212, 441,412, 499]
        self.box_10=[298, 245,338, 277]
        #self.box_10=[290, 265,335, 305]
        
        self.time_turn=0.8
        self.wait_time_1=0.05
        self.wait_time_2=0.30