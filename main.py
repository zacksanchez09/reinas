#
#  reinas.py
#  Reinas
#
#  Created by Zack Sanchez on 06/02/20.
#  Copyright © 2020 IA Society. All rights reserved.
#

import sys, copy, pprint


def is_solution(coordinates, dimensions):
    # check if multiple queens on same row
    for x in range(dimensions):
        pos = coordinates[x]
        for next_col in range(x + 1, dimensions):
            next_pos = coordinates[next_col]
            # check if multiple queens on same row
            if pos == next_pos:
                return None
            # check if multiple queens on same diagonal
            if (pos + next_col - x) == next_pos:
                return None
            if (pos - next_col + x) == next_pos:
                return None
    return coordinates


def print_solution(dim, sol):
    for val in range(dim - 1, -1, -1):
        for y in sol:
            if y == val:
                print(' Q  ', end='')
            else:
                print(' 0  ', end='')
        print()
    print()


def main():
    solutions = []
    dim = 5
    # populate this_permutation
    this_permutation = []
    for n in range(dim):
        this_permutation.append(0)

    # calculate the number of permutations
    possible_permutations = dim
    for n in range(dim):
        possible_permutations *= dim

    # initialize the counter
    #placement_cnt = 0

    # go through the permutations searching for all possible solutions
    for n in range(possible_permutations):
        rem = n
        for m in range(dim):
            this_permutation[m] = rem % dim
            rem //= dim
        # is this_permutation a solution?
        result = is_solution(copy.copy(this_permutation), dim)
        if result:
            # was this solution encountered previously?
            if result not in solutions:
                print_solution(dim, this_permutation)
                print("es solución!")
                input("presiona enter para continuar")
                solutions.append(result)
        else:
            print_solution(dim, this_permutation)


    print('\nInvestigadas', possible_permutations, 'Posibilidades')
    sol_cnt = len(solutions)
    print(sol_cnt, 'Soluciones encontradas')
"""
    print('\n==========\nSolutions:\n==========')
    print('\n("x" position is position of value in array.\n"y" position is value in array)\n')
    cnt = 0
    for solution in solutions:
        cnt += 1
        print()
        print('Solution', cnt, ':')
        pprint.pprint(solution)
        print_solution(dim, solution)"""


if __name__ == '__main__':
    main()