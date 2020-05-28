"""
Sem de Algoritmia 2020A

Solución al probema de las 5 Reinas mediante algoritmo de Fuerza Bruta
Programado en Python versión 3."""

import sys, copy, pprint
import tkinter as tk
from tkinter import scrolledtext as st
import sys
import os
from os import listdir
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import font
from tkinter import *
from tkinter import ttk
import tkinter
import pandas as pd
from PIL import ImageTk, Image




class Aplicacion:
    def __init__(self):
    	self.plataforma = sys.platform
    	self.solutions = []
    	self.dim = 5
    	self.this_permutation = []
    	self.ventana1=tk.Tk()
    	self.ventana1.title("Reinas")
    	self.labels = []
    	style = ttk.Style()
    	self.ventana1.configure(background='navajo white')
    	appHighlightFont = font.Font(family='Helvetica', size=16, weight='normal')
    	label2 = Label(self.ventana1, text="Problema de las 5 reinas", font=appHighlightFont).place(x=20, y=20)
    	self.canvas1=tk.Canvas(self.ventana1, width=900, height=700, background="SteelBlue1")
    	self.canvas1.grid(column=1, row=0, padx=250, pady=80)
    	self.botonSetPos = Button(self.ventana1, text="Agregar", command=print("bien"), font=appHighlightFont, bg="pale green")
    	self.botonSetPos.place(x=20, y=410)
    	self.ventana1.mainloop()


    def start(self):
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
			print_solution(dim, this_permutation)
			result = is_solution(copy.copy(this_permutation), dim)
			if result:
				# was this solution encountered previously?
				if result not in solutions:
					print("Es solucion!")
					input("Oprima enter para continuar\n")
					solutions.append(result)
			else:
				print("no es solucion\n")


		print('\nInvestigated', possible_permutations, 'possibilities.')
		sol_cnt = len(solutions)
		print(sol_cnt, 'solutions found.')
		print('\n==========\nSolutions:\n==========')
		print('\n("x" position is position of value in array.\n"y" position is value in array)\n')
		cnt = 0
		for solution in solutions:
			cnt += 1
			print()
			print('Solution', cnt, ':')
			pprint.pprint(solution)
			print_solution(dim, solution)





aplicacion1=Aplicacion()