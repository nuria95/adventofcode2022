import numpy as np
import time


class Solution():
    def __init__(self):
        with open('input.txt') as f:
            data = f.read().splitlines()

        self.forest = np.array([list(map(int, line)) for line in data])
        self.vis_matrix = np.zeros(
            (4, self.forest.shape[0], self.forest.shape[1]))

    def find_visibility_horizontal(self, flip=False):
        matrix = np.fliplr(self.forest) if flip else self.forest
        rightmax = np.diff(np.transpose(
            [np.max(matrix[:, 0:i], axis=1) for i in range(1, matrix.shape[1]+1)]), prepend=-1)
        return np.fliplr(rightmax > 0) if flip else rightmax > 0

    def find_visibility_vertical(self, flip=False):
        matrix = np.flipud(self.forest) if flip else self.forest
        topmax = np.diff(np.array([np.max(matrix[0:i, :], axis=0) for i in range(
            1, matrix.shape[0]+1)]), axis=0, prepend=-1)
        return np.flipud(topmax > 0) if flip else topmax > 0

    def part1(self):
        vis = self.find_visibility_horizontal()
        self.vis_matrix[0, :, :] = vis

        vis = self.find_visibility_horizontal(flip=True)
        self.vis_matrix[1, :, :] = vis

        vis = self.find_visibility_vertical()
        self.vis_matrix[2, :, :] = vis

        vis = self.find_visibility_vertical(flip=True)
        self.vis_matrix[3, :, :] = vis
        return np.sum(np.max(self.vis_matrix, axis=0))

    def distance(self, line, tree):
        i = 0
        for i, x in enumerate(line, 1):
            if x >= tree:
                break
        return i

    def distance2(self, line, tree):
        i = 0  #  if line has only 1 element (i.e. edge) then return this!
        for i, n in enumerate(line[1:], 1):
            if n >= tree:
                break
        return i

    def part2(self):
        score = 0
        for r, c in np.ndindex(self.forest.shape):
            tree = self.forest[r, c]

            score = max(self.distance2(self.forest[r, c:], tree) *
                        self.distance2(np.flip(self.forest[r, :c+1]), tree) *
                        self.distance2(self.forest[r:, c], tree) *
                        self.distance2(np.flip(self.forest[:r+1, c]), tree), score)

        return score


if __name__ == '__main__':
    solution = Solution()
    t = time.time()
    print(f'Solution for part one: {solution.part1()}')
    print('time ', time.time()-t)

    t = time.time()
    print(f'Solution for part two: {solution.part2()}')
    print('time', time.time()-t)
