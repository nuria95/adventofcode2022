import numpy as np
with open("day1/input.txt") as f:
    data = f.read().splitlines() # list of strings




# total_indiv_cal = 0
# total_cals = []
# for d in data:
#     if len(d)>0:
#         total_indiv_cal += int(d)
#     else:
#         total_cals.append(total_indiv_cal)
#         total_indiv_cal = 0

# One liner:
data_splitted = " ".join(data).split("  ") # join returns a string by joinng all the elements together of the data list, separated by separator " ", and then we split this list wherever there is a double space
total_cals = [sum(map(int, row.split(" "))) for row in " ".join(data).split("  ") ]


print('Max cals', max(total_cals))

print('Top 3', sum(sorted(total_cals, reverse=True)[0:3]))

