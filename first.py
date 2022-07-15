n = int(input())
words = []

for i in range(n):
	word = str(input())
	words.append(word)


tmp = 0
distinct = 0



print(len(set(words)))


lis = list(dict.fromkeys(words))


for i in lis:
	count = words.count(i)
	print(count,end=" ")

print("\n")
