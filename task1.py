import random 

ourList = list()
belowFive = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
for val in ourList:
	if (val < 5 ):
		belowFive.append(val)
    
print(ourList)
print(belowFive)


