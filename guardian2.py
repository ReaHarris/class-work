try:
	fhand = open('mbox-short.txt')
except:
	print('file does not exist')
try:
	for line in fhand:
		words = line.split()
		#print('Debug: ', words)
		if not len(words) == 0 and words[0] == 'From': print(words[2])
except:
	print('file cannot be read')
	exit()