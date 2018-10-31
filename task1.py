import random 

ourList = list()
count = 0 
#the append command adds the specified number to the list/when increasing the number
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList
