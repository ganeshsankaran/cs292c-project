import argparse as ap
from generator import *
from ioutils import *
from smtutils import *

# fill in holes based on a model
def fill_holes(puzzle, model):
    R = len(puzzle) - 1    # number of rows
    C = len(puzzle[0]) - 1 # number of columns

    for (r, c) in product(range(1, R), range(C)):
        if puzzle[r][c] == 0:
            puzzle[r][c] = model[Int(f'x_{r}_{c}')].as_long()

    return puzzle

# parse command-line args
parser = ap.ArgumentParser(description='Solve a Challenger puzzle using Z3')
parser.add_argument('-i', '--input', help='Input filename', required=False)
parser.add_argument('-o', '--output', help='Output filename', required=True)
parser.add_argument('-g', '--generate', help='Generate a puzzle', required=False, action='store_true')
parser.add_argument('-n', '--naive', help='Use naive symbolic compilation', required=False, action='store_true')
args = parser.parse_args()

# get puzzle internal representation
if not args.generate:
    puzzle = read_puzzle_from_file(args.input)
else:
    f = open(args.input, 'w')
    f.write('')
    f.close()

    puzzle = get_random_solved_puzzle(4, 4, 1, 9)
    puzzle = add_holes_to_solved_puzzle(puzzle, 12)
    write_solved_puzzle_to_file(puzzle, args.input)

# get constraints
if args.naive:
    formula = get_constraints_naive(puzzle)
else:
    formula = get_constraints(puzzle)

# solve constraints
model, statistics = solve_constraints(formula)
print(statistics)

# get solved puzzle
solved_puzzle = fill_holes(puzzle, model)

# dump solved puzzle
write_solved_puzzle_to_file(solved_puzzle, args.output)