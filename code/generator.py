from itertools import product
from random import randint, sample

# randomly generated a solved puzzle
# R rows by C columns
# entries from lo to hi
def get_random_solved_puzzle(R, C, lo, hi):
    puzzle = []

    # generate random values in each row
    for r in range(R):
        puzzle.append([randint(lo, hi) for c in range(C)] + [0])

    # fix last row
    puzzle.append([sum([puzzle[r][c] for r in range(R)]) for c in range(C)])

    # fix last column
    for r in range(R):
        puzzle[r][:-1]
        puzzle[r][C] = sum(puzzle[r][:-1])
        
    # fix main diagonal
    puzzle[R].append(sum([puzzle[r][c] for (r, c) in zip(range(R), range(C))]))

    # fix other diagonal
    d1 = sum([puzzle[r][c] for (r, c) in zip(range(R), reversed(range(C)))])
    first = [-1] * R + [d1]
    puzzle = [first] + puzzle
    
    return puzzle

# remove some entries from a solved puzzle
def make_holes_in_solved_puzzle(puzzle, n):
    R = len(puzzle) - 1    # number of rows
    C = len(puzzle[0]) - 1 # number of columns

    # randomly choose holes
    holes = sample(set(product(range(1, R), range(C))), n)

    for (r, c) in holes:
        puzzle[r][c] = 0
    
    return puzzle