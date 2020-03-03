#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
import sys

print("武汉加油💪 💪 💪，白衣天使来拯救你，🦠 死光光")
perc = input("你猜猜，一天可以消灭百分之多少🦠 ：")
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

l1 = "="
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
    
print("\n哈哈哈，🦠已经死光光啦～😄😄😄")


# In[ ]:





# In[ ]:





# In[ ]:




