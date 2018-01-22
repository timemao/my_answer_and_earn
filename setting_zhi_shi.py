#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:16:45 2018

@author: timemao
"""

class Zhi_shi():
    def __init__(self):
        self.time_money={'pm12_30':'100','pm19_30':'100','pm20_30':'100'\
                         ,'pm21_30':'300for youth','pm22_30':'200'}
        self.box_question=[161, 258,477, 355]

        self.box_number=3
        self.box_1=[110, 396,509, 438]
        self.box_2=[self.box_1[0], 489,self.box_1[2], 529]
        self.box_3=[self.box_1[0], 580,self.box_1[2], 621]
        self.box_selection=[117, 400,277, 617]
        self.box_all=[self.box_selection[0],self.box_question[1],\
                      self.box_question[2],self.box_selection[3]]
        self.number_start=0