'''
- run each of the real-world puzzle examples 10 times
- for each, use both naive and smarter constraint generation
- for each, calculate avg time, memory usage, rlimit count, model count

- solver vs human comparison:
- time graphs comparison, is the relationship linear?
- not an apples to apples comparison
  (diff units, diff platforms) for solver memory, rlmit, model count vs human time
'''
from ioutils import *
from smtutils import *
import csv
import time

fields = ['puzzle', 'human time', 'time', 'memory', 'rlimit count', 'mk bool var', 'mk clause', 'decisions', 'propagations', 'conflicts', 'model count']

# run the experiments

csvfile = open('../samples/times.csv', newline='\n')
reader = csv.reader(csvfile, delimiter=',')
next(reader)

with open('../results/experiment1_results_naive.csv', 'w') as f:
  f.write(','.join(fields) + '\n')
  for r in reader:
    puzzle = read_puzzle_from_file(f'../samples/puzzle{r[0]}.txt')
    constraints = get_constraints_naive(puzzle)
    model, stats = get_model(constraints)
    n = count_models(constraints)
    row = [str(r[0])] + [str(60 * int(r[1]) + int(r[2]))] + [str(get_statistic(field, stats)) for field in fields[2:]] + [str(n)]
    f.write(','.join(row) + '\n')

# run the experiments

csvfile = open('../samples/times.csv', newline='\n')
reader = csv.reader(csvfile, delimiter=',')
next(reader)

with open('../results/experiment1_results.csv', 'w') as f:
  f.write(','.join(fields) + '\n')
  for r in reader:
    puzzle = read_puzzle_from_file(f'../samples/puzzle{r[0]}.txt')
    constraints = get_constraints(puzzle)
    model, stats = get_model(constraints)
    n = count_models(constraints)
    row = [str(r[0])] + [str(60 * int(r[1]) + int(r[2]))] + [str(get_statistic(field, stats)) for field in fields[2:]] + [str(n)]
    f.write(','.join(row) + '\n')

csvfile.close()