# -*- coding: utf-8 -*-
import numpy as np


class Solves: 
    
    def __init__(self, deck,model,meshes):
        self.deck = deck
        # Compute the TEMPERATURE for each node
        self.T0 = meshes.T0
        self.T = meshes.T
        self.model = model
        self.meshes=meshes  
        self.do_solver()
            
        
        
        
    def do_solver(self):
        for m in range(int(self.deck.doc["Simulation"]["Number Time Steps"])):
            self.T0, self.T = self.model.do_timestep(self.T0, self.T, self.meshes.DiffTotalX, self.meshes.DiffTotalY)
            self.T[int(self.meshes.nx/2), int(0.2*self.meshes.nx):int(0.8*self.meshes.nx+1)] = 100
            self.T[int(self.meshes.nx/2-1), int(0.2*self.meshes.nx):int(0.8*self.meshes.nx+1)] = 100
            self.T0=self.T.copy()
    
