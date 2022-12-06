with open("input.txt") as f:
	data = f.read()

nchars = 4 #14   
for i in range(nchars, len(data)):
    seq = data[i-nchars:i]
    if len(set(seq)) == nchars:
        print(i, seq)
        break

