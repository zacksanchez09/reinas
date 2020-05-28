"""
Reinas - Algoritmo Fuerza Bruta
Seminario de Solución de Problemas de Algoritmia
Created By: Isaac Eduardo Sánchez Campos
Código: 211172172
"""

import sys, copy, pprint

def is_solution(coordinates, dimensions):
    for x in range(dimensions):
        pos = coordinates[x]
        for next_col in range(x + 1, dimensions):
            next_pos = coordinates[next_col]
            if pos == next_pos:
                return None
            if (pos + next_col - x) == next_pos:
                return None
            if (pos - next_col + x) == next_pos:
                return None
    return coordinates

def print_solution(dim, sol):
    for val in range(dim - 1, -1, -1):
        for y in sol:
            if y == val:
                print('Q ', end='')
            else:
                print('. ', end='')
        print()
    print()

def main():
    solutions = []
    dim = 5
    this_permutation = []
    for n in range(dim):
        this_permutation.append(0)
    possible_permutations = dim
    for n in range(dim):
        possible_permutations *= dim

    for n in range(possible_permutations):
        rem = n
        for m in range(dim):
            this_permutation[m] = rem % dim
            rem //= dim
        print_solution(dim, this_permutation)
        result = is_solution(copy.copy(this_permutation), dim)
        if result:
            if result not in solutions:
                print("¡Es solucion!")
                input("Oprima Enter para continuar.\n")
                solutions.append(result)
        else:
            print("No es solucion.\n")

    print('\nInvestigadas', possible_permutations, 'posibilidades.')
    sol_cnt = len(solutions)
    print(sol_cnt, ' soluciones encontradas.')

if __name__ == '__main__':
    main()
