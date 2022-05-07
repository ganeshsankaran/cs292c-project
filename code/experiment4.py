# 4x4 grid fixed
# number of holes fixed to 12 (n^2 - n)
# vary the numbers (low 1-3), (med 4-6), (high 7-9) 
# for each, calculate avg time, memory usage, rlimit count, model count

import csv

from generator import *
from smtutils import *
from statistics import mean

dims = [4,4]
val_range = [[1,3], [4,6], [7,9], [1,9]]
num_holes = 12

fields = ['val_range', 'time', 'memory', 'rlimit count', 'mk bool var', 'mk clause', 'decisions', 'propagations', 'conflicts']

with open('../results/experiment4_results.csv', 'w') as f:
    f.write(','.join(fields) + '\n')

    for v in val_range:
        results = []
        for i in range(10):
            puzzle = get_random_solved_puzzle(*dims, *v)
            puzzle = make_holes_in_solved_puzzle(puzzle, num_holes)
            constraints = get_constraints(puzzle)
            model, stats = get_model(constraints)
            results.append([get_statistic(field, stats) for field in fields[1:]])
        
        avg = list(map(mean, zip(*results)))
        row = [str(v)] + [str(a) for a in avg]

        f.write(','.join(row) + '\n')
