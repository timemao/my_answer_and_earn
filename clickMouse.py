#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:48:59 2018

@author: timemao
"""

#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')
#TODO: Get and print the mouse coordinates.

try:
    while True:
        x,y=pyautogui.position()
        positionStr='X: '+str(x).rjust(4)+'Y: '+str(y).rjust(4)
        print(positionStr,end='')
        print('\b'*len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\nDone.')
        