from itertools import product
from z3 import *

# SMT-LIB declaration
def declaration(var):
    return f'(declare-const {var} Int)\n'

# SMT-LIB assertion
def assertion(expr):
    return f'(assert {expr})\n'

# Generate SMT-LIB constraints naively.
# Declare a variable for every entry
def get_constraints_naive(puzzle):
    f = '' # formula

    R = len(puzzle) - 1    # number of rows
    C = len(puzzle[0]) - 1 # number of columns

    # add declarations assertions on each entry
    for (r, c) in product(range(1, R), range(C)):
        var = f'x_{r}_{c}'
        f += declaration(var)

        if puzzle[r][c] == 0: # hole
            f += assertion(f'(and (>= {var} 1) (<= {var} 9))')
        else:
            f += assertion(f'(= {var} {puzzle[r][c]})')

    # add column assertions
    for c in range(C):
        lhs = '(+ '
        lhs += ' '.join(
            [f'x_{r}_{c}' for (r, c) in list(product(range(1, R), [c]))]
        )
        lhs += ')'
        rhs = puzzle[R][c]
        f += assertion(f'(= {lhs} {rhs})')

    # add row assertions
    for r in range(1, R):
        lhs = '(+ ' 
        lhs += ' '.join([
            f'x_{r}_{c}' 
            for (r, c) 
            in list(product([r], range(C)))
        ])
        lhs += ')'
        rhs = puzzle[r][C]
        f += assertion(f'(= {lhs} {rhs})')

    # add top left to bottom right (main) diagonal assertion
    lhs = '(+ '
    lhs += ' '.join([
        f'x_{r}_{c}' 
        for (r, c) 
        in zip(range(1, R), range(C))
    ])
    lhs += ')'
    rhs = puzzle[R][C]
    f += assertion(f'(= {lhs} {rhs})')

    # add rop right to bottom left diagonal assertion
    lhs = '(+ '
    lhs += ' '.join([
        f'x_{r}_{c}' 
        for (r, c) 
        in zip(range(1, R), reversed(range(C)))
    ])
    lhs += ')'
    rhs = puzzle[0][C]
    f += assertion(f'(= {lhs} {rhs})')

    return f

# Generate SMT-LIB constraints.
# Declare a variable for every hole,
# not every entry.
def get_constraints(puzzle):
    f = '' # formula

    R = len(puzzle) - 1   # number of rows
    C = len(puzzle[0]) - 1 # number of columns

    holes = set() # holes

    # add declarations assertions on each entry
    for (r, c) in product(range(1, R), range(C)):
        if puzzle[r][c] == 0: # hole
            var = f'x_{r}_{c}'
            f += declaration(var)
            f += assertion(f'(and (>= {var} 1) (<= {var} 9))')

            # add position to holes
            holes.add((r, c))

    # add column assertions
    for c in range(C):
        lhs = '(+ '
        # holes
        lhs += ' '.join([
            f'x_{r}_{c}' 
            for (r, c) 
            in list(product(range(1, R), [c]))
            if (r, c) in holes
        ])
        lhs += ' '
        # non-holes
        lhs += ' '.join([
            str(puzzle[r][c])
            for (r, c) 
            in list(product(range(1, R), [c]))
            if (r, c) not in holes
        ])
        lhs += ')'
        rhs = puzzle[R][c]
        f += assertion(f'(= {lhs} {rhs})')

     # add row assertions
    for r in range(1, R):
        lhs = '(+ ' 
        lhs += ' '.join([
            f'x_{r}_{c}' 
            for (r, c) 
            in list(product([r], range(C)))
            if (r, c) in holes
        ])
        lhs += ' '
        # non-holes
        lhs += ' '.join([
            str(puzzle[r][c])
            for (r, c) 
            in list(product([r], range(C)))
            if (r, c) not in holes
        ])
        lhs += ')'
        rhs = puzzle[r][C]
        f += assertion(f'(= {lhs} {rhs})')

    # add main diagonal assertion
    lhs = '(+ '
    lhs += ' '.join([
        f'x_{r}_{c}' 
        for (r, c) 
        in zip(range(1, R), range(C))
        if (r, c) in holes
    ])
    lhs += ' '
    lhs += ' '.join([
        str(puzzle[r][c])
        for (r, c) 
        in zip(range(1, R), range(C))
        if (r, c) not in holes
    ])
    lhs += ')'
    rhs = puzzle[R][C]
    f += assertion(f'(= {lhs} {rhs})')

    # add other diagonal assertion
    lhs = '(+ '
    lhs += ' '.join([
        f'x_{r}_{c}' 
        for (r, c) 
        in zip(range(1, R), reversed(range(C)))
        if (r, c) in holes
    ])
    lhs += ' '
    lhs += ' '.join([
        str(puzzle[r][c])
        for (r, c) 
        in zip(range(1, R), reversed(range(C)))
        if (r, c) not in holes
    ])
    lhs += ')'
    rhs = puzzle[0][C]
    f += assertion(f'(= {lhs} {rhs})')
    
    return f

# solve SMT-LIB formula using Z3
def solve_constraints(f):
    s = Solver()
    s.add(parse_smt2_string(f))
    
    if s.check() == sat:
        return s.model(), s.statistics()
    else:
        return None, s.statistics()

# fill in holes based on a model
def fill_holes_from_model(puzzle, model):
    R = len(puzzle) - 1    # number of rows
    C = len(puzzle[0]) - 1 # number of columns

    for (r, c) in product(range(1, R), range(C)):
        if puzzle[r][c] == 0:
            puzzle[r][c] = model[Int(f'x_{r}_{c}')].as_long()

    return puzzle