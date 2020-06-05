import random
num1 = input('請輸入隨機數字開始範圍值')
num2 = input('請輸入隨機數字結束範圍值')
num1 = int(num1)
num2 = int(num2)
x = random.randint(num1, num2)
count = 0
while True:
	print('範圍', num1, '-', num2)
	y = input('請猜數字:')
	y = int(y)
	count = count + 1
	if y == x:
		print('"終於猜對了"')
		print('這是你猜的第', count, '次')	
		break
	elif y > x:		
		print('比答案大')
	elif y < x:		
		print('比答案小')
	print('這是你猜的第', count, '次')	

