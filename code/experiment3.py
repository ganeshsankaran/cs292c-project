# changing size from 2x2 to 10x10 grid
# n^2 - n holes (equivalently, n filled entries)
# for each, calculate avg time, memory usage, rlimit count, model count

import csv

from generator import *
from smtutils import *
from statistics import mean

dim_range = [2, 10]
val_range = [1, 9]

fields = ['size (nxn)', 'num_holes', 'time', 'memory', 'rlimit count', 'mk bool var', 'mk clause', 'decisions', 'propagations', 'conflicts']

with open('../results/experiment3_results.csv', 'w') as f:
    f.write(','.join(fields) + '\n')

    for n in range(dim_range[0], dim_range[1] + 1):
        holes = (n * n) - (n)
        results = []
        for i in range(10):
            puzzle = get_random_solved_puzzle(n, n, *val_range)
            puzzle = make_holes_in_solved_puzzle(puzzle, holes)
            constraints = get_constraints(puzzle)
            model, stats = get_model(constraints)
            results.append([get_statistic(field, stats) for field in fields[2:]])
        
        avg = list(map(mean, zip(*results)))
        row = [str(n), str(holes)] + [str(a) for a in avg]
        
        f.write(','.join(row) + '\n')
