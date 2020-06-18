from problem import *
import os, sys
import glob
import matplotlib.pyplot as plt
import pdb
from PIL import Image

cwd = os.getcwd()

deck = Deck(cwd + "/deck.yaml")

matrix_generation = Matrix_Generation(deck)

boundary_conditions = Boundary_Conditions(deck,matrix_generation)

initial_conditions = Initial_Conditions(deck, matrix_generation)

solution = Solution(deck, matrix_generation, initial_conditions, boundary_conditions)

# graph_temperature = Graph_Temperature(matrix_generation, solution)

deformation_calculation = Deformation_Calculation(deck, matrix_generation, initial_conditions, solution)

graph_deformation = Graph_Deformation(matrix_generation, solution, deformation_calculation)