def count(x, y):
	count = 0
	for letter in x:
		if letter == y:
			count = count + 1
	return count
	
x = input('Enter word: ')
y = input('Enter letter: ')
answer = count(x,y)
print(answer)