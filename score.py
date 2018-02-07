try:
	x = float(input('please enter a number between 0.0 and 1.0: '))
except:
	print('Please enter a numerical value')
	exit()
if x >= 1.0:
	print('bad score') 
elif x >= 0.9:
	print('A')
elif x >= 0.8:
	print('B')
elif x >= 0.7:
	print('C')
elif x >= 0.6:
	print('D')
elif x < 0.0:
	print('bad score')
elif x < 0.6:
	print('F')

