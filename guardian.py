try:
	fhand = open('tmp.rtf')
except:
	print('file does not exist')
try:
	for line in fhand:
		words = line.split()
		#print('Debug: ', words)
		if len(words) == 0 : continue
		if words[0] != 'From': continue
		print(words[2])
except:
	print('file cannot be read')
	exit()