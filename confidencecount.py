fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()
total = 0.0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:') :
        tline = float(line[20:])
        total = total + tline
        count = count + 1
print('Average spam confidence: ', total/count)
	