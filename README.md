最近很火的答题Python搜索:
==
一.思路
---
1.chrome浏览器插件vysor将Android手机画面同步到电脑;
>工具:chrome's vysor\
>流程:安装插件-打开插件-打开Android开发者选项usb调试-done\
2.ocr识别特定位置矩形框里的题目及选项;\
>工具:pyautogui;pyscreenshot;pytesseract-ocr(chi_sim+eng模式);\
>流程:\
(1).pyautogui确定矩形框\
(2).pyscreenshot抓取屏幕特定框,抓屏时间与所抓屏幕大小关系不是很大\
(3).pytesseract识别文字,识别速度效率和图像中文字的多少有关\
3.在百度搜索问题(带选项);\
工具:selenium\
流程:\
(1).打开浏览器,注意这一步提前执行,因为执行速度比较慢:driver=webdriver.Chrom(path)\
(2).用driver.get(url)方法获取整个网页内容,然后用find_elements_..方法获取需要的类(class)文本和标签文本(id)\
4.根据百度搜索的结果来分析选项出现次数多少来判定答案\
工具:fuzzywuzzy包\
流程:\
利用fuzzywuzzy包的fuzz.ratio()函数分析每个句子与每个选项之间的模糊匹配情况,设置激活阈值,超过阈值得分+1\
最后统计总得分,根据选择对的/不对的来选择最高激活值还是最低激活值\
