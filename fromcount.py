try:
	fhand = open('mbox-short.txt')
except:
	print('file does not exist')
	exit()
count = 0
try:
	for line in fhand:
		words = line.split()
		if not len(words) == 0 and words[0] == 'From': print(words[1])
		count = count + 1
except:
	print('file cannot be read')
	exit()
print('There were', count, 'lines in the file with From as the first word.')
