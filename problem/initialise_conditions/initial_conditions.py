import numpy as np

class Initial_Conditions:
    
    def __init__(self, deck, matrix_generation):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
        self.do_vector_temperature()
        
    
    def do_vector_temperature(self):
        
        self.Textrusion = float(self.deck.doc["Experimental Conditions"]["Extrusion Temperature"])
        self.T = np.ones((self.matrix_generation.nx,1))*self.Textrusion
        self.Tbed = float(self.deck.doc["Experimental Conditions"]["Bed Temperature"])
        self.T[0] = self.Tbed