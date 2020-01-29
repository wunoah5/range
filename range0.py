#range 範圍
#python內建功能:清單產生器
import random

range(3) #[0, 1, 2]


#拿來當作「執行固定次數」用
for i in range(3):    #執行3次
    print(i)


for i in range(6):
	r = random.randint(1, 49)
	print('這是第', i+1, '次產生隨機數字', r)