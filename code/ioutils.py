def read_puzzle_from_file(filename):
    puzzle = []
    
    with open(filename, 'r') as f:
        rows = f.read().split('\n')
        
        for row in rows[1:]:
            puzzle.append([int(i) for i in row.split()])
            
        # First row (pad with zeros)
        size = len(puzzle[0])
        val = int(rows[0])
        first = [0] * (size - 1) + [val]
        
        puzzle = [first] + puzzle
    
    return puzzle

def write_solved_puzzle_to_file(puzzle, filename):
    f = open(filename, 'w')

    for row in range(len(puzzle)):
        # first row case
        if row == 0:
            for col in range(len(puzzle[0])):
                if col == 0:
                    f.write(' ')
                elif col == len(puzzle[0]) - 1:
                    f.write('{:>3}\n'.format(puzzle[row][col]))
                else:
                    f.write('{:>3}'.format(''))

        # printing every other row
        else:
            for col in range(len(puzzle[0])):
                if col == 0:
                    f.write(str(puzzle[row][col]))
                elif col == len(puzzle[0]) - 1:
                    f.write('{:>3}\n'.format(puzzle[row][col]))
                else:
                    f.write('{:>3}'.format(puzzle[row][col]))
    
    f.close()