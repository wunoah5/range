#range 範圍
#python內建功能:清單產生器
import random

range(3) #[0, 1, 2]
range(8, 10)  #隨機產生起始值為8，結尾值10是不包含的，[8, 9]
range(2, 10, 3)  #3稱為階梯值。開始值2每次增加3，[2, 5, 8]
range(10, 3, -2)  #階梯值可以是負的。[10, 8, 6, 4]

#拿來當作「執行固定次數」用
for i in range(3):    #執行3次
    print(i)


for i in range(6):
	r = random.randint(1, 49)
	print('這是第', i+1, '次產生隨機數字', r)


for i in range(2, 12, 3):
    print(i)