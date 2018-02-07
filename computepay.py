def computepay(hours, rate):
	if hours > 40:
		pay = (hours * rate) + (hours - 40) * rate * 0.5
	else:
		pay = hours*rate
	print('Pay: $', pay)

hours = float(input('enter hours\n'))
rate = float(input('enter rate\n'))

computepay(hours, rate)
