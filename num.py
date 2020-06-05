import random
x = random.randint(1, 100)
while True:
	y = input('請猜數字1-100: ')
	y = int(y)
	if y == x:
		print('"終於猜對了"')
		break
	elif y > x:
		print('比答案大')
	else:
		print('比答案小')	

