# keep size fixed at 4x4
# change # holes from 0 to 12
# for each, calculate avg time, memory usage, rlimit count, model count

import csv

from generator import *
from smtutils import *
from statistics import mean

dims = [4, 4]
val_range = [1, 9]
max_holes = 12

fields = ['num_holes', 'time', 'memory', 'rlimit count', 'mk bool var', 'mk clause', 'decisions', 'propagations', 'conflicts']

with open('../results/csv/experiment2_results.csv', 'w') as f:
    f.write(','.join(fields) + '\n')

    for holes in range(max_holes + 1):
        results = []
        for i in range(10):
            puzzle = get_random_solved_puzzle(*dims, *val_range)
            puzzle = make_holes_in_solved_puzzle(puzzle, holes)
            constraints = get_constraints(puzzle)
            model, stats = get_model(constraints)
            results.append([get_statistic(field, stats) for field in fields[1:]])
        
        avg = list(map(mean, zip(*results)))
        row = [str(holes)] + [str(a) for a in avg]
        
        f.write(','.join(row) + '\n')


