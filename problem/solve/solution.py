import numpy as np

class Solution:
    
    def __init__(self, deck, matrix_generation, initial_conditions, boundary_conditions):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
        self.initial_conditions = initial_conditions
        self.boundary_conditions = boundary_conditions
        self.hot_bed()
        self.bed_cooling()
        self.cold_bed()
    
    def hot_bed(self):
        
        self.nt = int(float(self.deck.doc["Simulation"]["time"])/self.matrix_generation.dt)
        self.Ttot = self.initial_conditions.T
        for t in range (self.nt):
            self.initial_conditions.T = np.dot(self.matrix_generation.M,self.initial_conditions.T)+self.boundary_conditions.Vamb
            self.Ttot = np.append(self.Ttot,self.initial_conditions.T,axis=1)
    
    def bed_cooling(self):
        
        Vcooling = float(self.deck.doc["Simulation"]["Vcooling"])
        timecooling = (self.initial_conditions.Tbed-self.boundary_conditions.Troom)/Vcooling
        self.nt1 = int(timecooling/self.matrix_generation.dt)
        
        self.boundary_conditions.Vamb[0]=-Vcooling*self.matrix_generation.dt
        for t in range (self.nt1):
            self.initial_conditions.T = np.dot(self.matrix_generation.M,self.initial_conditions.T)+self.boundary_conditions.Vamb
            self.Ttot = np.append(self.Ttot,self.initial_conditions.T,axis=1)
    
    def cold_bed(self):
        self.nt2 = int(float(self.deck.doc["Simulation"]["time2"])/self.matrix_generation.dt)
        
        self.boundary_conditions.Vamb[0]=0
        for t in range (self.nt2):
            self.initial_conditions.T = np.dot(self.matrix_generation.M,self.initial_conditions.T)+self.boundary_conditions.Vamb
            self.Ttot = np.append(self.Ttot,self.initial_conditions.T,axis=1)
        
        