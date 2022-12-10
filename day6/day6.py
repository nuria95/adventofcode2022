with open("input.txt") as f:
	data = f.read()

for part, nchars in zip(['part1', 'part2'], [4,14]): 
    for i in range(nchars, len(data)):
        seq = data[i-nchars:i]
        if len(set(seq)) == nchars:
            print('Solution ', part, i)
            break

