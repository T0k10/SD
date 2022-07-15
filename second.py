t = int(input())
words = []
for i in range(t):
	ask = input()
	words.append(ask)


def bigger_is_greater(word):
	

	lis = []
	for i in word:
		for j in i:
			lis.append(j)
	lis.sort()
	print(lis)
bigger_is_greater(words)
