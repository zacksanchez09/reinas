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
import numpy as np

PADDING = dict(padx=1, pady=1)




class Aplicacion:
	def __init__(self):
		self.plataforma = sys.platform
		self.solutions = []
		self.dim = 5
		self.labels = []
		self.this_permutation = []

		style = ttk.Style()
		image1 = Image.open("black.png")
		image1 = image1.resize((35, 35), Image.ANTIALIAS)
		photo1 = ImageTk.PhotoImage(image1)
		style.configure("black.TLabel", image=photo1)

		image2 = Image.open("white.png")
		image2 = image2.resize((35, 35), Image.ANTIALIAS)
		photo2 = ImageTk.PhotoImage(image2)
		style.configure("white.TLabel", image=photo2)

		image3 = Image.open("queen.png")
		image3 = image3.resize((35, 35), Image.ANTIALIAS)
		photo3 = ImageTk.PhotoImage(image3)
		style.configure("green.TLabel", image=photo3)

		self.ventana1=tk.Tk()
		self.ventana1.title("Reinas")
		self.ventana1.configure(background='navajo white')
		appHighlightFont = font.Font(family='Helvetica', size=16, weight='normal')
		label2 = Label(self.ventana1, text="Problema de las 5 reinas", font=appHighlightFont).place(x=20, y=20)
		self.canvas1=tk.Canvas(self.ventana1, width=900, height=700, background="SteelBlue1")
		self.canvas1.grid(column=1, row=0, padx=250, pady=80)
		self.botonSetPos = Button(self.ventana1, text="Agregar", command=self.start, font=appHighlightFont, bg="pale green")
		self.botonSetPos.place(x=20, y=410)
		self.ventana1.mainloop()

	def is_solution(self, coordinates, dimensions):
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


	def print_solution(self, dim, sol):
		for val in range(dim - 1, -1, -1):
			for y in sol:
				if y == val:
					print('Q ', end='')
				else:
					print('. ', end='')
			print()
		print()


	def start(self):
		solutions = []
		self.matriz = np.zeros((5, 5))
		#data=self.matriz.to_numpy()
		#self.matriz=pd.DataFrame(data=data, columns=[self.namecolumnas], index=[self.namefilas])
		for val in range(5 -1, -1, -1):
			for y in self.matriz:
				#nombre=str(row) + str(col)
				#print(nombre)
				#sys.stdout.flush()
				#nombre=str(row) + " " + str(col)
				#print("coordenadas", nombre)
				#sys.stdout.flush()
				lbl = ttk.Label(self.canvas1, text='reinas', style=self.get_style(val), cursor='man', relief="raised", width=-5)
				lbl.grid(row=val, column=y+1, **PADDING)
				self.labels.append(lbl)
		mb.showinfo("Mapa Cargado","¡Mapa Cargado Correctamente! ✅")

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
			self.print_solution(dim, this_permutation)
			result = self.is_solution(copy.copy(this_permutation), dim)
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
			self.print_solution(dim, solution)


	@staticmethod
	def get_style(tiposid):
		if tiposid == "bosque":
			return "black.TLabel"
		elif tiposid == "camino":
			return "white.TLabel"
		elif tiposid == "lava":
			return "green.TLabel"
		else:
			return None


aplicacion1=Aplicacion()