#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:00:40 2018

@author: timemao
"""
from PIL import Image
import time
import pyscreenshot as ImageGrab
from utils import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def merge_images(image1,image2):
    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result
    
def test_box(box):
    im=ImageGrab.grab(bbox=box)
    tex=img_to_text(im)
    print(tex)
    #im.show()
    
def test_searchtime(box_abcd,box_a,box_b,box_c,box_d):
    box2=[206,561,431,627]
    time1=time.time()
    im=ImageGrab.grab(bbox=box_abcd)
    text=img_to_text(im)
    print('abcd %f'%(time.time()-time1)+text)
    time1=time.time()
    im=ImageGrab.grab(bbox=box2)
    text=img_to_text(im)
    print('only one %f'%(time.time()-time1)+text)
    time1=time.time()
    ima=ImageGrab.grab(bbox=box_a)
    imb=ImageGrab.grab(bbox=box_b)
    imc=ImageGrab.grab(bbox=box_c)
    imd=ImageGrab.grab(bbox=box_d)
    pp=merge_images(ima,imb)
    pp=merge_images(pp,imc)
    pp=merge_images(pp,imd)
    text=img_to_text(pp)
    print('merge %f'%(time.time()-time1)+text)

def test_webscrapy(text):
    url='http://www.baidu.com/s?wd=%s' %text
    webbrowser.open(url)
    
if __name__=='__main__':
    text='歌曲一剪梅的原唱是 费玉清古巨基周杰伦'#.encode('utf-8')
    answer='费玉清'
    #text='my name is liming'
    #test_webscrapy(text)
    url='http://www.baidu.com/s?wd=%s' %text
    MAX_RETRIES=20
    session=requests.Session()
    s1=requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
    r=session.get(url)
    string=r.content
    nPos=string.index(answer)
    #url=u''.join('http://www.baidu.com/s?wd=%s' %text).encode('utf-8').strip()
    #bsObj=BeautifulSoup(html)
    #allText=bsObj.findAll("",{"class":"c-row c-gap-top-small"})    