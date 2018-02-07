fname = input('Enter file name: ')
try:
	fhand = open(fname)
except:
	print('file does not exist')
	exit()
t = []
for line in fhand:
	words = line.split()
	for x in words:
		if x in t: continue
		t.append(x)
t.sort()
print(t)