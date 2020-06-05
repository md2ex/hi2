import random
x = random.randint(1, 100)
count = 0
while True:
	y = input('請猜數字1-100: ')
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

