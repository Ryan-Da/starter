#!/usr/bin/env python
# coding: utf-8

# In[12]:


BOARD_SIZE = 15
board=[]


# In[14]:


def initBoard()  :
    for i in range(BOARD_SIZE):
        row = ["➕"] * BOARD_SIZE
        board.append(row)
        def printBoard():
            for j in range(BOARD_SIZE):
                print(board [i] [j] , end="")
                print ()


# In[15]:


initBoard ()
inputStr = input ("请输入你下棋的坐标，应以x,y的格式：\n")


# In[17]:


def printBoard():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end = "")
        print()


# In[ ]:


while inputStr != None :
    x_str, y_str =inputStr.split(sep = ",")
    print("x_str = " + x_str +", y_str = " + y_str)
    board[int(y_str) - 1] [int(x_str) - 1] ="♟"
    printBoard( )
    inputStr =input("请输入你下棋的坐标，应以x,y的格式：\n")


# In[1]:



printBoard ()


# In[2]:


import time
import sys

perc = input("请输入每次增长的百分比：")
perc1 = int(perc)
count = 2  
while int(perc)>100 and count > 0:
    perc = input("请重新输入:")
    count = count-1
 


    
    


# In[3]:


if count == 0:
        print("输入字数过多，下次再来试吧！！！")
count = int(100 /perc1)
yushu = (100%perc1)
print("余数是：", yushu)


# In[4]:


l1 = "="
l1_perc = l1 + perc + "%"     # =5%
print(l1_perc, end = '\r')
time.sleep(1)


# In[5]:


for i in range(1, count):  
    h = (i + 1) * perc1               # (1 + 1) * 5, (2 + 1) * 5, (3 + 1) * 5, ...
    l11 = l1 * (i + 1) + str(h) + "%"   # ==10%, ===15%, ====20%
    print(l11, end = '\r')          
    sys.stdout.flush()
    time.sleep(1)
if yushu>0:
    l11 = l1 * (count+1) +"100%" 
    print(l11, end = '\r')  


# In[20]:


user_name = "Ryan" 
user_age = 9
print("读者名：" ,user_name,"年龄："  ,user_age)
         


# In[7]:





# In[21]:





#  print("欢迎来到香肠派对！！！")
# print("这个游戏是小恐龙公司出品！！")
# print("正在加载中。 。 。")
# import time
# import sys
# 
#  perc = input("请输入每次增长的百分比：")
# perc = '5'
# perc1 = int(perc)
# count = 2  
# while int(perc)>100 and count > 0:
#     perc = input("请重新输入:")
#     count = count-1
#  
# 
# if count == 0:
#         print("输入字数过多，下次再来试吧！！！")
# count = int(100 / perc1)
# 
# l1 = "■"
# l1_0 = l1 + perc + "%"     # =5%
# print(l1_0, end = '\r')
# time.sleep(1)
# for i in range(1, count):  
#     h = (i + 1) * perc1
#     l11 = l1 * (i + 1) + str(h) + "%" # ==10%, ===15%
#     print(l11, end = '\r')
#     sys.stdout.flush()
#     time.sleep(1)
# print("\n加载完成！！！") 
# 
# from random import *
# number = randint(1000,9999)
# print("验证码是" ,number)
# count = 2
# 
# while(count>0):
#     
#     answer = input("验证码是：")
#     answer =int(answer) 
#     if answer =="number":
#         print("验证通过！！！")
#         print("启动游戏中。。。")  
#     else:
#         print("验证未通过!请重新输入:")
#         count = count-1
#         
#     if  count == 0 :
#         print("\n输入次数过多，下次再玩吧！！")
#     
#     
#     

# In[2]:


print("欢迎来到香肠派对！！！")
print("这个游戏是小恐龙公司出品！！")
print("正在加载中。 。 。")

import time
import sys

perc = '5' 
perc1 = int(perc)

count = 2  
while int(perc)>100 and count > 0:
    perc = input("请重新输入:")
    count = count-1
if count == 0:
        print("输入字数过多，下次再来试吧！！！")
        
count = int(100 /perc1)
yushu = (100%perc1)
# print("余数是：", yushu)    

l1 = "■"
l1_perc = l1 + perc + "%"     # =5%
print(l1_perc, end = '\r')
time.sleep(1)

for i in range(1, count):  
    h = (i + 1) * perc1               # (1 + 1) * 5, (2 + 1) * 5, (3 + 1) * 5, ...
    l11 = l1 * (i + 1) + str(h) + "%"   #==10%, ===15%, ====20%
    print(l11, end = '\r')          
    sys.stdout.flush()
    time.sleep(1)
if yushu>0:
    l11 = l1 * (count+1) +"100%" 
    print(l11, end = '\r')  
    time.sleep(2)
else:
    time.sleep(1)
    print("\n加载完毕！！")
    
from random import *
number = randint(1000,9999) 
print("\n验证码是" ,number) 
count = 4
while(count>0):
    answer = input("验证码是：")
    answer  = int(    answer  )
    if answer ==number:
        print("验证通过！！！")
        print("启动游戏中。。。")
        print("启动完毕！！！游戏开始！！！")
        print("准备跳伞！！")
        print("\n你想跳到：1.城堡 2.飞行禁地")
        answer = input("请输入你想跳的地方：")
        if answer =="1":
            print("没问题，已跳伞！")
            print("\n城堡有：AK47，三级书包，三级头盔 1.拿 2.不拿")
            answer = input("请输入1或2:")
            if answer =="1":   
                print("恭喜你获得AK47，三级书包，三级头盔！！！")
                print("来了一个有四级头盔的人！ 1.打 2.跑")
                answer = input("请输入1或2:")
                if answer =="1":
                    print("你打死了有四级头盔的人")
                    print("有四级头盔 1.拿 2.不拿")
                    answer = input("请输入1或2:")
                    if answer =="1":
                        print("恭喜你获得四级头盔!!")
                        print("前方有人！1.逃跑 2.打")                        
                        answer = input("请输入1或2:")
                        if answer =="2":
                            print("三杀，大吉大利今晚吃鸡！！！！！")
                        if answer =="1":
                            print("你被打死了，那个人吃鸡了！！！")
                        break    
                    if answer =="2":
                        print("有个叫:狙击战神的拿了，你被打死了！！")
                    break    
                if answer =="2":
                    print("你被打死了！！")
                break    
                
            if answer =="2": 
                print("一个叫：毛绒绒的小狗拿了！把你打死了！！")
            break     
        if answer =="2":
            print("没问题，已跳伞！")
            print("\n飞行禁地有：三级头盔 1.不拿  2.拿")
            answer = input("请输入1或2:")
            if answer =="1":   
                print("那是诱饵，你被一个叫：小虫虫的打死了！") 
            if answer =="2": 
                print("你没被骗！但你没装备被一个叫：胜利属于我们的打死了！")
            break
    else:
        print("验证未通过!请重新输入:")
        count = count-1

    if  count == 0 :
        print("\n输入次数过多，下次再玩吧！！")
     
   



# In[ ]:




