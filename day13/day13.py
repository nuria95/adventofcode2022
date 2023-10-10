from itertools import zip_longest

with open('input.txt') as f:
    data = f.read().split('\n\n')


def compare(p1, p2):
    # llista d'integers, integer
    for ll, rr in zip_longest(p1, p2):
        if rr is None:
            return False
        if ll is None:
            return True
        if isinstance(ll, int) and isinstance(rr, int):
            if rr > ll:
                return True
            if rr < ll:
                return False
        else:  # one of them not int
            # convert the int to list so that we can iterate through them
            if isinstance(ll, int):
                ll = [ll]
            if isinstance(rr, int):
                rr = [rr]
            ret = compare(ll, rr)  # si no es compleix res, retorna None
            if ret in [True, False]:
                return ret


total = 0
for i, p in enumerate(data, 1):
    p1, p2 = [eval(line) for line in p.splitlines()]
    total += i if compare(p1, p2) == True else 0

print('Part 1', total)


# Part 2
pkts = [eval(p)
        for block in data for p in block.splitlines()] + [[[2]]] + [[[6]]]
done = False
while True:
    for i in range(len(pkts)-1):
        if compare(pkts[i], pkts[i+1]) == False:
            pkts[i], pkts[i+1] = pkts[i+1], pkts[i]
            done = False

    if done == True:
        break
    done = True

print('Part 2', (pkts.index([[2]])+1) * (pkts.index([[6]])+1))
