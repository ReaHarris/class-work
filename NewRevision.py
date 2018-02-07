import re
fname = input('Enter file name: ')
try:
	fhand = open(fname)
except:
	print('file does not exist')
	exit()
nums = list()
for line in fhand:
	line = line.rstrip()
	x = re.findall('New Revision: ([0-9]+)', line)
	if len(x) == 1:
		val = float(x[0])
		nums.append(val)
print(val)
print(sum(nums)/len(nums))