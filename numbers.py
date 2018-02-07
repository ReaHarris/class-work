total = 0
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
	count = count + 1
	total = total + num
print('Count: ', count)
print('Total: ', total)
print('Average: ', total/count)


