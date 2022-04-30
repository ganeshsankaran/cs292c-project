import random

def get_random_solved_puzzle(R, C, lo, hi):
    puzzle = []

    # generate random values in each row
    for r in range(R):
        row = []
        for c in range(C):
            row.append(random.randint(lo, hi))
        puzzle.append(row + [0])

    # fix last row
    last = []
    for c in range(C):
        last.append(sum([puzzle[i][c] for i in range(R)]))
    puzzle.append(last)

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

def add_holes_to_solved_puzzle(puzzle, num_holes):
    # gather possible options for holes
    options = []
    for row in range(1, len(puzzle) - 1):
        for col in range(len(puzzle[row]) - 1):
            options.append((row, col))
    
    hole_indexes = random.sample(options, num_holes)

    for point in hole_indexes:
        puzzle[point[0]][point[1]] = 0
    
    return puzzle