str = 'X-DSPAM-Confidence:0.8475'
colpos = str.find(':')
print(colpos)
num = str[colpos+1:]
print(float(num))