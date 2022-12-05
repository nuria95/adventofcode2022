with open("input.txt") as f:
	data = f.read().splitlines()

def fct(s: str):
	minn, maxx =s.split('-')
	return minn, maxx
num_subsets=0
num_overlaps = 0
for d in data:
	if len(d) <2:
		break
	a, b = list(map(lambda x: list(map(int,fct(x))), d.split(',')))
	

	if (a[0]>= b[0] and a[1]<=b[1]) or (b[0]>= a[0] and b[1]<=a[1]):
		num_subsets+=1

	if (a[0]<= b[1] and a[1]>=b[0]):
		num_overlaps+=1


print(num_subsets)
print(num_overlaps)