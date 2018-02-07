import re
hand = open('mbox.txt')
count = 0
reg = input('Enter a regular expression: ')
for line in hand:
	line = line.rstrip()
	x = re.findall(reg, line)
	if len(x) > 0:
		count = count + 1 
print('mbox.txt had', count, 'lines that matched', reg)