fhand = open('words.txt')
d = dict()
for line in fhand:
	words = line.split()
	for word in words:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
print(d)