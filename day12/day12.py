import numpy as np
from collections import deque
import time
#Timing: Star
start = time.perf_counter()


class Solution():
    def __init__(self):

        with open('input.txt') as f:
            self.data = f.read().splitlines()

        self.values = np.array(
            [list(map(lambda x: ord(x)-96, line)) for line in self.data])
        self.values_ = self.values.copy()
        self.values_[self.values == ord('S')-96] = ord('a') - 96
        self.values_[self.values == ord('E')-96] = ord('z') - 96
        self.rows, self.cols = self.values_.shape
        self.compute_graph()  # dict with key node and values neighbors.

    def part1(self):
        start = self.ind2digit(
            *list(map(lambda x: x.item(), np.where(self.values == ord('S')-96))))
        end = self.ind2digit(
            *list(map(lambda x: x.item(), np.where(self.values == ord('E')-96))))
        bfs = self.breadth_first_search(start, end)  # shortest path bfs
        return bfs

    def get_all_starts(self):
        starts_index = np.nonzero(self.values_ == 1)

        starts = [self.ind2digit(r, c) for r, c in zip(
            starts_index[0], starts_index[1])]
        return starts

    def part2(self):
        all_dists = []
        starts = self.get_all_starts()
        end = self.ind2digit(
            *list(map(lambda x: x.item(), np.where(self.values == ord('E')-96))))
        for start in starts:
            dist = self.breadth_first_search(start, end)
            if dist != -1:
                all_dists.append(dist)
        return min(all_dists)

    def breadth_first_search(self, start, end):
        self.queue = deque()
        self.queue.append((start, [start]))  #  node, path_to_node

        self.visited = set()

        self.visited.add(start)
        cur_node = start

        while len(self.queue):
            cur_node, path_to_node = self.queue.popleft()

            if cur_node == end:
                return len(path_to_node)-1

            self.queue.extend([[n, path_to_node+[n]]
                              for n in self.graph[cur_node] if n not in self.visited])
            self.visited.update(
                [n for n in self.graph[cur_node] if n not in self.visited])

        return -1

    def compute_graph(self):
        self.graph = {node: self.get_neighbors(
            *self.digit2ind(node)) for node in range(self.rows*self.cols)}

    def get_neighbors(self, i, j):
        neighbors = []
        for r, c in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            if (i+r) < 0 or (i+r) > self.rows-1 or (j+c) < 0 or j+c > (self.cols-1):
                continue
            if (self.values_[i, j] - self.values_[i+r, j+c]) >= -1:
                neighbors.append(self.ind2digit(i+r, j+c))
        return neighbors

    def ind2digit(self, row, col):
        v = (row * self.cols) + col
        return v

    def digit2ind(self, n):
        row = n//self.cols
        col = n % self.cols

        return row, col


if __name__ == '__main__':
    solution = Solution()
    t = time.time()
    len_shortest_path = solution.part1()
    print('Solution part 1', len_shortest_path)
    print('Solution part 2', solution.part2())

    #Timing: End
    end = time.perf_counter()
    print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")
