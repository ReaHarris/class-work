try:
	hours = float(input('enter hours\n'))
	rate = float(input('enter rate\n'))
except:
	print('please enter a numerical number')
	exit()
if hours > 40:
	x = hours - 40
else:
	x = 0
pay = (40+(x*1.5))*rate
print('Pay: $', pay)
