import numpy as np
import time


class Solution():
    def __init__(self):
        with open('input.txt') as f:
            self.data = f.read().splitlines()
        # list of all positions travelled by tail

        self.action = {'U': [1, 0], 'D': [-1, 0], 'L': [0, -1], 'R': [0, 1]}
        self.last = lambda in_list: in_list[-1]

    def part1(self):
        self.head = np.array([0, 0])
        self.tails = [np.array([0, 0])]
        for line in self.data:
            self.move_head(*line.split())

        return len(set([(i[0], i[1]) for i in self.tails]))

    def move_head(self, move, units):
        for i in range(int(units)):
            # print('\n', move, units)
            self.head += self.action[move]

            self.distance = self.head - self.last(self.tails)
            if np.all(np.abs(self.distance) <= 1):  # touching or overlapping
                pass
            else:
                # move tail
                self.tails.append(self.last(self.tails) +
                                  np.sign(self.distance))

    def part2(self):
        self.head = np.array([0, 0])  #  reset from part 1
        # last tail tracked path (i.e. element 9)
        self.tails = [np.array([0, 0])]
        #  consider all elements of the knots tails. Important not to do [np.array(..) * 10]! same as in day5
        self.p_tails = [np.array([0, 0]) for i in range(10)]
        for line in self.data:
            self.move_head2(*line.split())

        return len(set([(i[0], i[1]) for i in self.tails]))

    def move_head2(self, move, units):

        for n in range(int(units)):
            # print('\n', move, units)
            self.head += self.action[move]
            self.p_tails[0] = self.head.copy()
            for i in range(len(self.p_tails)-1):
                dist = self.p_tails[i] - self.p_tails[i+1]
                if np.all(np.abs(dist) <= 1):  # touching or overlapping
                    pass
                else:  # move tail
                    self.p_tails[i+1] += np.sign(dist)
            # print('head', self.head)
            # print('tails', self.p_tails[1:])

                add = self.last(self.p_tails).copy() # important the copy!!!
                self.tails.append(add)  # add position of last tail to track


if __name__ == '__main__':
    solution = Solution()
    t = time.time()
    print(f'Solution for part one: {solution.part1()}')
    print('time ', time.time()-t)

    t = time.time()
    print(f'Solution for part two: {solution.part2()}')
    print('time', time.time()-t)
