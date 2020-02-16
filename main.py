#
#  reinas.py
#  Reinas
#
#  Created by Zack Sanchez on 06/02/20.
#  Copyright © 2020 IA Society. All rights reserved.
#

import random
import numpy
import matplotlib.pyplot as plt
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# Número de Reinas
NB_QUEENS = 5

# Algotimo Fitness
def evalNQueens(individual):
    size = len(individual)

    diagonal_izquierda_derecha = [0] * (2*size-1)
    diagonal_derecha_izquierda = [0] * (2*size-1)


    for i in range(size):
        diagonal_izquierda_derecha[i+individual[i]] += 1
        diagonal_derecha_izquierda[size-1-i+individual[i]] += 1

    suma = 0
    for i in range(2*size-1):
        if diagonal_izquierda_derecha[i] > 1:
            suma += diagonal_izquierda_derecha[i] - 1
        if diagonal_derecha_izquierda[i] > 1:
            suma += diagonal_derecha_izquierda[i] - 1
    return suma,

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(NB_QUEENS), NB_QUEENS)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalNQueens)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/NB_QUEENS)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    seed = 0
    random.seed(seed)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=True)

    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, best = main()
    print(best)
    print(best[0].fitness.values)
    y = best[0]
    x = range(NB_QUEENS)
    x = numpy.array(x)
    print(x)
    y = numpy.array(y)
    print(y)
    x = x + 0.5
    y = y + 0.5
    plt.figure()
    plt.scatter(x,y)
    plt.xlim(0,NB_QUEENS)
    plt.ylim(0,NB_QUEENS)
    plt.xticks(x-0.5)
    plt.yticks(x-0.5)
    plt.grid(True)
    plt.title(u"Mejor Posición")
    plt.show()
