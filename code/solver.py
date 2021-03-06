import argparse as ap
from generator import *
from ioutils import *
from smtutils import *

# parse command-line args
parser = ap.ArgumentParser(description='Solve a Challenger puzzle using an SMT solver')
parser.add_argument('-i', '--input', help='Input filename', required=True)
parser.add_argument('-o', '--output', help='Output filename', required=True)
parser.add_argument('-g', '--generate', help='Use a randomly generated puzzle as input', required=False, action='store_true')
parser.add_argument('-n', '--naive', help='Use naive symbolic compilation', required=False, action='store_true')
args = parser.parse_args()

# get puzzle internal representation
if not args.generate:
    puzzle = read_puzzle_from_file(args.input)
else:
    puzzle = get_random_solved_puzzle(4, 4, 1, 9)
    puzzle = make_holes_in_solved_puzzle(puzzle, 12)
    write_solved_puzzle_to_file(puzzle, args.input)

# get constraints
if args.naive:
    formula = get_constraints_naive(puzzle)
else:
    formula = get_constraints(puzzle)

# solve constraints
model, statistics = get_model(formula)

# get solved puzzle
solved_puzzle = fill_holes_from_model(puzzle, model)

# dump solved puzzle
write_solved_puzzle_to_file(solved_puzzle, args.output)