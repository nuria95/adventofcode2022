
from collections import defaultdict
from functools import reduce

import numpy as np
class Solution():
    def __init__(self):
        with open('input.txt') as f:
            self.monkey_pars= f.read().split('\n\n')
        with open('input.txt') as f:
            self.data = f.read().splitlines()
        self.info = defaultdict(list)
        self.monkeys = {}
        
    def populate(self):
        for n in self.monkey_pars:
            num_monkey = int(n.splitlines()[0].split()[1][0])
            items = eval(n.splitlines()[1].split(':')[1][1:])
            if isinstance(items, int):
                items = [items]
            op = ''.join(n.splitlines()[2].split()[3:])
            test = int(n.splitlines()[3].split()[3])
            istrue = int(n.splitlines()[4].split()[5])
            isfalse = int(n.splitlines()[5].split()[5])
            inspections = 0

            self.monkeys[num_monkey] = {'items': list(items), 
                                        'op': op, 
                                        'div': test,
                                        'istrue': istrue, 
                                        'isfalse': isfalse, 
                                        'inspections': inspections}

    def part1_2(self, rounds = 20, part=1):
        modulo_trick = reduce((lambda x,y: x*y), [m['div'] for m in self.monkeys.values()]) # multiply all the modulos. Trick to make code more efficient
        for _ in range(rounds):
            for monk in self.monkeys.values():
                monk['inspections'] += len(monk['items'])
                new = []
                for old in monk['items']:
                    new.append((eval(monk['op']) % modulo_trick) //(5-2*part)) # use modulo trick to make code more efficient. division is by 3 for part1 and by 1 for part 2
            
                test = np.array([not (n % monk['div'] ) for n in new])
                
                self.monkeys[monk['istrue']]['items'].extend(list(np.array(new)[test==1]))
                self.monkeys[monk['isfalse']]['items'].extend(list(np.array(new)[test==0]))
                monk['items'] = []
              
            
        insp = [m['inspections'] for m in self.monkeys.values()]

        insp.sort()
        return insp[-1]*insp[-2]
                    
              
                   
            
            
            
     
    
if __name__=='__main__':
    solution = Solution()
    solution.populate()
    print('part 1 ', solution.part1_2(rounds=20))
    solution.populate()
    print('part2 ',solution.part1_2(rounds=10000, part=2))
    # solution.part2()