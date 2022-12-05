with open("input.txt") as f:
	data = f.read().splitlines()
lines = []
n = 4 # each string element has length of 3 + one separation: i.e. [G] has len 3, or the spaces between columns too
for i, l in enumerate(data):
    if len(l)<2: # break between stacks and procedure
        next_idx = i # keep index for later
        break
    lines.append([l[i:i+n] for i in range(0,len(l),n)])


numpiles = len(lines[0])
 # Important!
# piles = [[]]*numpiles 
# This creates 4 different REFERENCES of [] and 
#inserted them into a new list. These are 4 empty lists inside the main list, but these are NOT different list objects
#  instead these are mere references of first list. So if we do: piles[0] = a, then 'a' Element was inserted 
# #in all the sub lists, because these are not different lists

# Correct way: Create a list of 5 empty sub lists
piles = [[] for i in range(numpiles)]


for l in reversed(lines):# start from below  
    for i, s in enumerate(l):
        if '[' in s:
            piles[i].append(s[1]) # remove [ ]

# for l in data[next_idx::]: # start the procedure part
#     if len(l)<2:
#         continue
#     _, num, _, s, _, e = l.split(' ')
#     num, s, e = list(map(int, [num,s,e]))
#     for n in range(num):
#         el = piles[s-1].pop()
#         piles[e-1].append(el)
       
# solution = ''
# for num in range(numpiles):
#     solution+=piles[num][-1]

# print(solution)


for l in data[next_idx::]: # start the procedure part
    if len(l)<2:
        continue
    _, num, _, s, _, e = l.split(' ')
    num, s, e = list(map(int, [num,s,e]))
    el = piles[s-1][-num::]
    assert len(el) == num
    piles[s-1] = piles[s-1][:-num]
    piles[e-1].extend(el)

solution = ''
for num in range(numpiles):
    solution+=piles[num][-1]

print(solution)
