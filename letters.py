fname = input('Enter file name: ')
try:
	fhand = open(fname)
except:
	print('file does not exist')
	exit()
letters = dict()
for line in fhand:
	line = line.lower()
	for x in line:
		if x not in 'abcdefghijklmnopqrstuvwxyz': continue
		if x not in letters:
			letters[x] = 1
		else:
			letters[x] += 1
			
lst = list()
for key, val in list(letters.items()):
	lst.append((val,key))

lst.sort(reverse=True)

for key, val, in lst:
	print(key, val)