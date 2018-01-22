#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:17:18 2018

@author: timemao
"""

class Xi_gua():
    def __init__(self):
        self.time_money=self.time_money={'pm18_00':'50+20','pm20_00':'100','pm21_00':'100'\
                         ,'pm22_00':'300','pm23_00':'100'}
        self.box_question=[96, 289,537, 374]
        self.box_number=3
        self.box_1=[134, 444,298, 480]
        self.box_2=[self.box_1[0], 539,self.box_1[2], 569]
        self.box_3=[self.box_1[0], self.box_2[1]+(self.box_2[1]-self.box_1[1]),self.box_1[2], self.box_2[3]+(self.box_2[3]-self.box_1[3])]
        self.box_selection=[132, 446,333, 665]
        self.answer_color={'blue':[32,23]}
        self.number_start=1
        self.difficulty={'recogition':'middle','content':'middle','resolution':'burry'}