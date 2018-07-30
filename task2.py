import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])
reversePhrase = ""

n = len(randomPhrase)-1
while n >= 0: 
	reversePhrase += randomPhrase[n]
	n-=1
	


print(randomPhrase)
print(reversePhrase)
