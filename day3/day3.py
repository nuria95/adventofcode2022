with open("input.txt") as f:
	data = f.read().splitlines()

def split(n):
	return list(n) #split string into chars

def compute_priority(m: str):
	return int(common_item.isupper())*26 + ord(common_item.lower())-96 #-96 since ord('a) is 96, ord('b') is 97...

priority = 0
for bag in data:
	if len(bag) < 1: # empty line in end of file
		break
	c1, c2 = bag[:int(len(bag)/2)], bag[int(len(bag)/2)::]
	setc1, setc2 = list(map(lambda x: set(split(x)),[c1,c2]))
	
	common_item = list(setc1.intersection(setc2))[0]
	priority += compute_priority(common_item) 

print(priority)

priority = 0
for idx in range(0,len(data),3):
	c1, c2,c3 = data[idx], data[idx+1], data[idx+2]
	setc1, setc2, setc3 = list(map(lambda x: set(split(x)),[c1,c2,c3]))
	common_item = list(setc1.intersection(setc2).intersection(setc3))[0]
	priority += compute_priority(common_item) #-96 since ord('a) is 96, ord('b') is 97...

print(priority)


