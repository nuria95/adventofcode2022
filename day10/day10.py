
class Solution():
    def __init__(self):
        with open('input.txt') as f:
            self.data = f.read().splitlines()

    def part1(self):
        sol = 0
        X = [1]
        [X.extend([X[-1]] if instr.split()[0][0]=='n' else [X[-1], X[-1]+int(instr.split()[1])]) for instr in self.data]
        checkpoints = list(range(20,221,40))
        for cycle in checkpoints:
            sol += (X[cycle-1]*cycle)
    
        self.X = X
        return sol

    def part2(self):
        screen = ''
        for c,r  in enumerate(self.X):
            if not c % 40: # change line
                screen += '\n'
            if r in [c%40-1,c%40, c%40+1]: 
                screen +='#' 
            else:
                 screen += '.'
        print(screen)


if __name__=='__main__':
    solution = Solution()
    print(solution.part1())
    solution.part2()