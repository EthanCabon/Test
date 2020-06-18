import numpy as np

class Matrix_Generation:
    
    def __init__(self, deck):
        
        self.deck = deck
        self.do_matrix()
        
    
    def do_matrix(self):
        
        self.lenX = float(self.deck.doc["Simulation"]["lenX"])
        self.dx =  float(self.deck.doc["Simulation"]["dx"])             
        self.nx =int(self.lenX/self.dx)+1
        self.k =  float(self.deck.doc["Materials"]["Thermal"]["Thermal Conductivity"])
        self.rho = float(self.deck.doc["Materials"]["Mechanical"]["Density"])
        self.Cp = float(self.deck.doc["Materials"]["Thermal"]["Heat Capacity"])
        self.D = self.k/(self.rho*self.Cp)
        self.dt = float(self.rho*self.Cp*self.dx**2/(2*self.k*10))              
        self.C1=self.dt*self.D/self.dx**2
        
        
        self.M = np.zeros((self.nx,self.nx))
        Vsup = Vinf = np.ones((self.nx-1,1))*self.C1
        Vdiag = np.ones((self.nx,1))*(1-2*self.C1)
        np.fill_diagonal(self.M[1:],Vinf)
        np.fill_diagonal(self.M,Vdiag)
        np.fill_diagonal(self.M[:,1:],Vsup)