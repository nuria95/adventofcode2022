import os
import numpy as np
import time

with open('input.txt') as f:
    data = f.read().splitlines()


tree = {'/': {'size': 0, 'parent': None}}
path = []


def bottom_to_top(path: str, size: int):
    # Update sizes of the whole tree recursively
    if path == None:  # reached root
        return
    tree[path]['size'] += size
    bottom_to_top(tree[path]['parent'], size)

t = time.time()
for c in data:

    # moving directory
    if c[0] == '$':
        if 'cd' in c:
            to_move = c.split(' ')[2]
            if to_move == '..':
                path.pop()  # move one backwards
            else:
                path.append(to_move)  # move inside 'to_move'
    # ignore
    elif c[0:2] == 'ls':  # ignore
        continue

    # stating files and folders
    else:
        if 'dir' in c:
            dir_name = c.split(' ')[1]
            path_dir_name = ('/').join(path+[dir_name])

            # create new leave in tree
            if path_dir_name not in tree.keys():
                tree[path_dir_name] = {'size': 0, 'parent': ('/').join(path)}

        # update size of the whole tree with filesize
        else:
            size = int(c.split(' ')[0])
            bottom_to_top('/'.join(path), size)


total_size = 0
for k, v in tree.items():
    if v['size'] <= 100000:
        total_size += v['size']


print('Part 1', total_size)
print(time.time()-t)
required_space = 30000000
disk_space = 70000000
unused_space = disk_space - tree['/']['size']
to_delete = required_space - unused_space


sol = min(v['size'] for v in tree.values() if v['size']>=to_delete)
print('Part 2', sol)
