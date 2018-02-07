smallest = None
largest = None
count = 0
while True:
	line = input('enter a number: ')
	if line == 'done':
		break
	try:
		num = float(line)
	except:
		print('Invalid input')
		continue
	if smallest is None or num < smallest:
		smallest = num
	if largest is None or num > largest:
		largest = num
print('Max: ', largest)
print('Min: ', smallest)


