import numpy as np
with open("input.txt") as f:
    data = f.read().splitlines() # list of strings

map_digits = {'A':0,'X':0,'B':1,'Y':1,'C':2,'Z':2} # 0 rock, 1 paper, 2 scissors
map_winner_score = {1: 0, 0:3, 2:6} # lose:0, draw: 3, win: 6 using modulo output
map_shape_score = {0: 1, 1:2, 2:3}
total_score = 0
for game in data:
    op, me = [map_digits[z] for z in game.split(' ')]
    winner = (op-me)%3 # 0 = draw, 1=lose, 2 win (-1%3 = 2 )  (-2%3 == 1)
    total_score += (map_winner_score[winner] + map_shape_score[me])

print("Part 1", total_score)

total_score = 0
map_winner_score = {0: 0, 1:3, 2:6} # lose:0, draw: 3, win: 6 using XYZ solution

for game in data:
    op, winner = [map_digits[z] for z in game.split(' ')] # 0 lose, 1 draw, 2 win

    me = (op + winner - 1)%3
    total_score += (map_winner_score[winner] + map_shape_score[me])
print("Part 2", total_score)





