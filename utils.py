#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:59:31 2018

@author: timemao
"""
import time
import pyscreenshot as ImageGrab
import pytesseract
import webbrowser
from termcolor import colored
import pyautogui
import random
from zhon.hanzi import punctuation
from re import sub
import numpy as np

from setting_wechat import Brain_king
from fuzzywuzzy import fuzz
from PIL import Image
#from utils2 import count_disappear
# if is answer, click left point
ans_click_point=450
len_same=8
mouse_return=[560, 523]

box_ti=[215, 425,423, 487]

time_wait_1=0.03
time_wait_2=0.28
time_wait_3=0.6

max_search_length=33

web_point=[1152, 623]

active=lambda x:x if x>=5 else 0
active_thres1=10
active_thres2=5
lib_question='lib-question.txt'
question_lib='question-lib.txt'
replace_file='deleteword.txt'
replace_file2='deleteword2.txt'
reverse_file='reverse.txt'

def add_lib(box_a,box_b,box_c,box_d,text_question,write_file,g_r):
    im=which_green(box_a,box_b,box_c,box_d,g_r)
    index=1
    while (not im and index<=30):
        im=which_green(box_a,box_b,box_c,box_d,g_r)
        index+=1
    if im:
        answer=box_to_text_question(im)
        print('Answer is: '+answer)
        print('Be Saved!')
        fr=open(write_file,'a')
        fr.write(text_question+'\t'+answer+'\n')
        fr.close()
    else:
        print (colored('I need master\'s help','red'))
    
def box_to_text_question(box_question,number_start=0,is_debug=0):
    stt=time.time()
    im_qu=ImageGrab.grab(box_question)
    im_qu.save('qu.jpg')
    im_question=Image.open('qu.jpg')
    if is_debug:
        im_question.show()
    text=pytesseract.image_to_string(im_question,lang='chi_sim+eng')
    print(text)
    text=sub(r"[%s]+"%punctuation,"",text)
    text=sub('[()《》″"?\'`~!,;]',"",text)
    if len(text)>38:
        text=more_38(text)
    text=''.join(text.split())
    text=sub(' ',"",text)
    print(text)
    print(colored('OCR time %f'%(time.time()-stt),'red'))
    if not number_start:
        text=replace_text(replace_file,text)
        print(text)
        return text
    text=replace_text(replace_file,sub("[01234567890]\'′","",text[0:3])+text[3:])
    print(text)
    return text

def box_to_text_selection(box_selection,is_debug=0):
    st=time.time()
    im_se=ImageGrab.grab(bbox=box_selection)
    im_se.save('se.jpg')
    im_selection=Image.open('se.jpg')
    if is_debug:
        im_selection.show()
    text_selection=pytesseract.image_to_string(im_selection,lang='chi_sim+eng')
    print(text_selection)
    text_selection=sub(r"[%s]+"%punctuation,"",text_selection)
    text_selection=sub('[()《》′′″"?\'`~!,;]',"",text_selection)
    text_selection=sub(' ',"",text_selection)
    print(text_selection)
    text_selection=text_selection.split()
    text_selection=''.join(text_selection)
    print(colored('OCR selection time %f'%(time.time()-st),'red'))
    return text_selection

def box_to_text_10(box_10,is_debug=0):
    im_box_10=ImageGrab.grab(box_10)
    text_10=pytesseract.image_to_string(im_box_10)
    if is_debug:
        im_box_10.show()
        print(text_10)
    return text_10
    
def cluster_exclude(array):
    index_sort=sorted(range(len(array)), key=lambda k: array[k])
    dist01=array[index_sort[1]]-array[index_sort[0]]
    dist12=array[index_sort[2]]-array[index_sort[1]]
    if dist01>=dist12:
        return index_sort[0]
    else:
        return index_sort[2]

def click_mouse(point,is_ans=0):
    pyautogui.moveTo(point)
    pyautogui.click(point,button='left')
    if not is_ans:
        pyautogui.moveTo(mouse_return)
def correct_text(text_from,text_to):
    # delete punctuation
    fr=open(text_from,'r')
    questions=[line.split('\n') for line in fr]
    fc=open(text_to,'w')
    for i in range(len(questions)):
        have_same=0
        item=questions[i][0]
        question,may_answer=item.split('\t')[0],item.split('\t')[-1]
        for j in range(i+1,len(questions)):
            item_2=questions[j][0]
            question_2=item_2.split('\t')[0]
            if len(question)>=6:
                question=sub(r"[%s]+"%punctuation,"",question)
                may_answer=sub(r"[%s]+"%punctuation,"",may_answer)
                if question_2[0:5]==question[0:5]:
                    have_same+=1
        if have_same==0 and may_answer!='' and may_answer!='\n':
            fc.write(question+'\t'+may_answer+'\n')
    fr.close()
    fc.close
def correct_text_two():
    correct_text(question_lib,lib_question)
    correct_text(lib_question,question_lib)
    #print(colored('correct! done!','red'))

def combine_url_answer(suff_url,per_answer):
    words=[word.rstrip() for word in open('combine_word.txt')]
    index=0
    is_have=False
    word=words[0]
    while (word not in suff_url):
        word=words[index]
        index+=1
        if index==len(words):
            break
        if word in suff_url and word!='':
            comb_sent=sub(word,per_answer,suff_url)
            is_have=True
            break
    if not is_have:
        comb_sent=suff_url+per_answer
    return comb_sent

def count_disappear(suff_url,driver,answer,max_count=1):
    if max_count:
        url="https://www.baidu.com/s?wd=%s"%(suff_url) #+' '+''.join(answer))
    else:
        url="https://www.baidu.com/s?wd=%s"%(suff_url)
    t2=time.time()
    driver.get(url)
    print('get url time: %f'%(time.time()-t2))
    text_main=driver.find_elements_by_class_name("c-abstract")
    text_title=driver.find_elements_by_class_name("t")
    all_count_title=np.array(np.zeros(len(answer)))
    all_count_main=np.array(np.zeros(len(answer)))
    count_ti=np.array(np.zeros(len(answer)))
    count_ma=np.array(np.zeros(len(answer)))
    sim_ti=np.array(np.zeros(len(answer)))
    sim_ma=np.array(np.zeros(len(answer)))
    all_sim_ti=np.array(np.zeros(len(answer)))
    all_sim_ma=np.array(np.zeros(len(answer)))
    #print(colored(comb_sent,'red'))
    for index in range(len(text_main)):
        #print(index)
        per_ti=text_title[index].text 
        #print(per_ti)
        per_ma=text_main[index].text
        #print(per_ma)
        for j in range(len(answer)):
            count_ti[j]=per_ti.count(answer[j])
            all_count_title[j]=all_count_title[j]+count_ti[j]
            count_ma[j]=per_ma.count(answer[j])
            all_count_main[j]=all_count_main[j]+count_ma[j]
            sim_ti[j]=similarity(per_ti,answer[j],1)   # no structure
            sim_ma[j]=similarity(per_ma,answer[j])
        for j in range(len(answer)):
            if sim_ti[j]==sim_ti.max() and sim_ti[j]-sim_ti.min()>active_thres1:
                all_sim_ti[j]+=1
            if sim_ma[j]==sim_ma.max() and sim_ma[j]-sim_ma.min()>active_thres2:
                all_sim_ma[j]+=1
        #print(sim_ti)
        #print(sim_ma)
        #print(all_sim_ti)
        ##print(all_sim_ma)
    all_count=all_count_main+all_count_title
    #print('count:'+str(all_count))
    #if all_count.max()!=all_count.min():
      #  all_count=(all_count-all_count.min())/(all_count.max()-all_count.min())
    all_sim=all_sim_ma +all_sim_ti
    #print('similarity'+str(all_sim))
    #if (all_sim.max()!=all_sim.min()):
     #   all_sim=(all_sim-all_sim.min())/(all_sim.max()-all_sim.min())
    #print('result'+str(all_sim+all_count))
    return all_sim +all_count
    
def find_reverse(string,reverse_file):
    for filter_word in open(reverse_file):
        fw=filter_word.rstrip()
        if fw in string:
            print(colored('there is :'+fw,'red'))
            return True            
    return False
    
def get_center(bbox):
    return bbox[2],(bbox[1]+bbox[3])/2

def get_img_color(im):
    rgb_im=im.convert('RGB')
    width,height=rgb_im.size
    # print(np.shape(rgb_im))
    r,g,b=rgb_im.getpixel((5,5))
    r1,g1,b1=rgb_im.getpixel((width-5,height-5))
    return (g+g1)/2

def get_similar(im,text_txt):
    text_answer=box_to_text_question(im)
    if text_answer[0:3]==text_txt[0:3]:
        return True
    else:
        return False

def more_38(text):
    list_text=text.split()
    text1=''.join(list_text[1:len(list_text)-1])
    text2=list_text[-1]
    #print(colored('more 38','red'))
    return text1+text2

def replace_text(word_file,string):
    for filter_word in open(word_file):
        fw=filter_word.rstrip()
        if fw in string:
            fw_len=len(fw)
            string=string.replace(fw,''*fw_len)
    return string
            
def search_question(text_question,text_file):
    fr=open(text_file,'r')
    questions=[line.split('\n') for line in fr]
    for i in range(len(questions)):
        item=questions[i][0]
        question,may_answer=item.split('\t')[0],item.split('\t')[-1]
        if text_question[0:len_same]==question[0:len_same]:
            print(colored('find: '+item,'red'))
            return may_answer
   
def select_answer(index,box_a,box_b,box_c,box_d):
    position=[get_center(box_a),get_center(box_b),get_center(box_c),get_center(box_d)]
    click_mouse([ans_click_point,position[index-1][1]],1)
    
def similarity(per_text,comb_sent,is_ti=0):
    string=sub('[！，。？……]'," ",per_text)
    #string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", " ",per_text) 
    list_text=string.split(' ')
    sim=0
    if is_ti:
        sim=fuzz.ratio(list_text[0],comb_sent)
    else:
        for idx,sti in enumerate(list_text):
            if sti!='':
                sim=sim+fuzz.ratio(sti,comb_sent)
    return sim
    
def solution_once():
    box=Brain_king()
    click_mouse(get_center(box.box_start))
    have_question=False
    index=1
    while (not have_question):
        is_question=wait_question(index,box.box_continue,box.box_10)
        if is_question:
            text_question=box_to_text_question(box.box_questiion)
            solution_one(box.box_1,box.box_2,box.box_3,box.box_4,text_question,box.answer_color)
            index+=1
        else:
            click_mouse(get_center(box.box_continue))
            return True
        
def solution_one(box_a,box_b,box_c,box_d,text_question,g_r):
    st=time.time()
    answer=search_question(text_question,question_lib)
    print('search question time: %f'%(time.time()-st))
    if answer:
        st2=time.time()
        index=which_answer(box_a,box_b,box_c,box_d,answer)
        print('search answer time :%f'%(time.time()-st2))
        select_answer(index,box_a,box_b,box_c,box_d)
        print('index: %d'%index)
        print(colored('Answer is:'+answer,'red'))
    else:
        url='http://www.baidu.com/s?wd=%s' %text_question
        webbrowser.open(url)
        #time.sleep(1)
        index=random.randint(1,4)
        print('random select %d'%index)
        select_answer(index,box_a,box_b,box_c,box_d)
        #time.sleep(1)
        add_lib(box_a,box_b,box_c,box_d,text_question,question_lib,g_r)
        
def wait_question(index,box_continue,box_10):
    question_state=None
    is_continue=''
    while (not question_state):
        is_continue=box_to_text_question(box_continue)
        if is_continue!='继续挑战':
            text_10=box_to_text_10(box_10,is_debug=1)
            if (text_10=='10'):
                if index==1:
                    time.sleep(time_wait_1)
                else:
                    time.sleep(time_wait_2)
                return True
        else:
              return False
def web_count(count,memory_index,reverse):
    maxmin_count=0
    if memory_index:
        #print('memory_index')
        #print(memory_index)
        if not reverse:
            #print('no reverse')
            maxmin_count=np.argmax(count)
            if count[maxmin_count]==count[memory_index]:
                index_prediction=memory_index
            else:
                    index_prediction=maxmin_count
        else:
            #print('reverse')
            maxmin_count=np.argmin(count)
            if count[maxmin_count]==count[memory_index]:
                index_prediction=memory_index
            else:
                index_prediction=maxmin_count
    else:
        #print('no memory index')
        if not reverse:
            #print('no reverse')
            index_prediction=np.argmax(count)
        else:
            #print('reverse')
            index_prediction=np.argmin(count)
    #print(colored('index prediction %d'%index_prediction,'red'))
    return index_prediction
    
def web_search(box,now_time,driver1,driver2,is_debug=0):
    #print(colored('before box to question time %f'%(time.time()-now_time),'red'))
    text_question=box_to_text_question(box.box_question,box.number_start,0)
    #print(colored('after box to question time %f'%(time.time()-now_time),'red'))
    #text_selection=box_to_text_selection(box.box_3,is_debug)
    reverse=find_reverse(text_question,reverse_file)
    text_question=sub("不","",text_question)
    text_question=sub("没","",text_question)
    text_question=sub("否","",text_question)
    text_question=sub("无","",text_question)
    #print(colored('reverse'+str(reverse),'red'))
    text_se1=box_to_text_selection(box.box_1,is_debug)
    #print(colored('after box1 time %f'%(time.time()-now_time),'red'))
    text_se2=box_to_text_selection(box.box_2,is_debug)
    #print(colored('after box2 time %f'%(time.time()-now_time),'red'))
    text_se3=box_to_text_selection(box.box_3,is_debug)
    #print(colored('after box3 time %f'%(time.time()-now_time),'red'))
    list_answer=[text_se1,text_se2,text_se3]
    empty_number=0
    memory_index=None
    for i in range(3):
        if list_answer[i]=='':
            empty_number+=1
            non_empty=[x for x in list_answer if x!='']
            #print(non_empty)
            if non_empty!=[]:
                if not memory_index:
                    memory_index=list_answer.index(non_empty[0])
                list_answer[i]=non_empty[0]
               #print('i empty'+str(i))
                #print(list_answer)
    #text=text_question+' '+''.join(text_selection)
    count1=count_disappear(text_question,driver1,list_answer)
    count2=np.array(np.zeros([3,3]))
    if empty_number<=2:#np.max(count)==0:
        #print('all count is 0, alone calc.')
        comb_sent=[combine_url_answer(text_question,per_answer) for per_answer in list_answer]
        #print(comb_sent)
        #for i in range(3):
            #count2[i,:]=count_disappear(comb_sent[i],driver2,list_answer,max_count=0)
    count2=np.sum(count2,axis=0)
    #print('alone sum count ')
    #print(colored('count appear time %f'%(time.time()-now_time),'red'))
    count=count1+count2/2
    #print('below is all count')
    print(count)
    index_prediction=web_count(count,memory_index,reverse)
    print('index_prediction')
    print(index_prediction)
    list_box=[box.box_1,box.box_2,box.box_3]
    this_time=time.time()  
    print('this time is below:')
    print(this_time-now_time)
    while (this_time-now_time<8):
        if 1:#(this_time-now_time>6.4):
            if empty_number!=3:
                print('click my answer!')
                click_mouse(get_center(list_box[index_prediction]),1)
                return True
        this_time=time.time()
        #print(this_time-now_time)
    x=random.randint(0,2)
    if x==0:
        click_mouse(get_center(box.box_1),is_debug)
    elif x==1:
        click_mouse(get_center(box.box_2),is_debug)
    elif x==2 :
        click_mouse(get_center(box.box_3),is_debug)
    print('this question randomly answer: '+str(x+1))
    print(time.time()-now_time)
    #driver.close()
    #pyautogui.moveTo(web_point)
    #time.sleep(1.5)
    #pyautogui.scroll(-4)
    
def which_answer(box_a,box_b,box_c,box_d,text_answer):
    im_A=ImageGrab.grab(bbox=box_a)
    index=random.randint(1,4)
    if get_similar(im_A,text_answer):
        index=1
    else:
        im_B=ImageGrab.grab(bbox=box_b)
        if get_similar(im_B,text_answer):
            index=2
        else:
            im_C=ImageGrab.grab(bbox=box_c)
            if get_similar(im_C,text_answer):
                index=3
            else:
                im_D=ImageGrab.grab(bbox=box_d)
                if get_similar(im_D,text_answer):
                    index=4
    return index
    
def which_green(box_a,box_b,box_c,box_d,g_r):
    im_A=ImageGrab.grab(bbox=box_a)
    im=None
    if g_r[0]<=get_img_color(im_A)<=g_r[1]:
        im=im_A
    else:
        im_B=ImageGrab.grab(bbox=box_b)
        if g_r[0]<=get_img_color(im_B)<=g_r[1]:
            im=im_B
        else:
            im_C=ImageGrab.grab(bbox=box_c)
            if g_r[0]<=get_img_color(im_C)<=g_r[1]:
                im=im_C
            else:
                 im_D=ImageGrab.grab(bbox=box_d)
                 if g_r[0]<=get_img_color(im_D)<=g_r[1]:
                     im=im_D
    return im