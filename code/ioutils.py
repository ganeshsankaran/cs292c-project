# import matplotlib.pyplot as plt
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
    with open(filename, 'w') as f:
        for r in range(len(puzzle)):
            # first row case
            if r == 0:
                for c in range(len(puzzle[0])):
                    if c == len(puzzle[0]) - 1:
                        f.write('{:>3}\n'.format(puzzle[r][c]))
                    else:
                        f.write('{:>3}'.format(''))

            # printing every other row
            else:
                for c in range(len(puzzle[0])):
                    if c == len(puzzle[0]) - 1:
                        f.write('{:>3}\n'.format(puzzle[r][c]))
                    else:
                        f.write('{:>3}'.format(puzzle[r][c]))

def plot_graph(title,x_arr, y_arr, x_label, y_label): 
    plt.figure()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('title')
    plt.scatter(x_arr, y_arr, s = 5)
    plt.savefig(f'./results/graphs/{title}.jpg')

# test = [0, 1, 2, 3, 4, 5]
# plot(test, test, 'testing graph', 'x_label', 'y_label')