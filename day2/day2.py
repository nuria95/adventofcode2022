import numpy as np
with open("input.txt") as f:
    data = f.read().splitlines() # list of strings


class Game1():
    def __init__(self, op, me):

        self.map_digits = {'X': 'A', 'Y': 'B', 'Z':'C'}
        self.map_winner_score = {-1: 0, 0:3, 1:6}
        self.map_shape_score = {'A': 1, 'B':2, 'C':3}
        self.op = op
        self.me = self.map_digits[me]
    
    @property
    def find_winner(self):
        if self.op==self.me:
            result = 0

        else:
            if 'A' in [self.op, self.me]: 
                if 'B' in [self.op, self.me]: # AB, BA
                    result = -1 if self.op == 'B' else 1
                else: # 'AC', CA
                    result = -1 if self.op == 'A' else 1
            
            else: # BC CB
                result = -1 if self.op == 'C' else 1
        
        return result

    def score(self, winner):

        score_win = self.map_winner_score[winner] + self.map_shape_score[self.me]
        return score_win


    def play_game(self):
        winner = self.find_winner
        score = self.score(winner)
        return score


class Game2(Game1):
    def __init__(self, op, me):
        super().__init__(op,me)
        self.map_winner = {'X': -1, 'Y': 0, 'Z': 1}
        self.me = me
    
    @property
    def find_winner(self):
        return self.map_winner[self.me]
    
    @property
    def find_shape(self):
        if self.map_winner[self.me] == 0:
            shape = self.op
        
        else:
            if self.op == 'A': 
                shape = 'B' if self.map_winner[self.me] == 1 else 'C'
            elif self.op == 'B':
                shape = 'C' if self.map_winner[self.me] == 1 else 'A'
            else:
                shape = 'A' if self.map_winner[self.me] == 1 else 'B'
        
        return shape

            


    
    def score(self, winner):

        score_win = self.map_winner_score[winner] + self.map_shape_score[self.find_shape]
        return score_win


    


def main():
    # total_score1 = 0
    # total_score2 = 0

    # for game in data:
    

    #     op, me = game.split(" ")
    
    #     g1 = Game1(op,me)
    #     total_score1 +=g1.play_game()

    #     g2 = Game2(op,me)
    #     total_score2 +=g2.play_game()


    # print(total_score1, total_score2)

    # vals,point_shape={'A':2,'X':2,'B':0,'Y':0,'C':1,'Z':1},{2:1,0:2,1:3}

    for x in open('input.txt').read().split('\n'):
        print(x)
    #     for g in [vals[z] for z in x.split(' ')]:
    #         print(g)
    #         point_shape[g[1]]+((g[1]-g[0]+1)%3)*3  

    #     exit()


    vals,pts={'A':2,'X':2,'B':0,'Y':0,'C':1,'Z':1},{2:1,0:2,1:3}
    # print(sum([pts[g[1]]+((g[1]-g[0]+1)%3)*3 for g in [[vals[z] for z in x.split(' ')] for x in open('input.txt').read().split('\n')]]))


if __name__ == '__main__':
   main()

