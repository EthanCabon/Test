class Deformation_Calculation():
    
    def __init__(self, deck, matrix_generation, initial_conditions, solution):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
        self.initial_conditions = initial_conditions
        self.solution = solution
        self.do_calculation()
        
    def do_calculation(self):
        
        Tmoy=self.solution.Ttot[0,:]+self.solution.Ttot[self.matrix_generation.nx-1,:]
        
        for i in range (1,self.matrix_generation.nx-1):
            Tmoy += 2*self.solution.Ttot[i,:]
        
        Tmoy /= 2*self.matrix_generation.nx-1
        self.Eps = float(self.deck.doc["Materials"]["Mechanical"]["Coefficient of Thermal Expansion"])*(Tmoy-self.initial_conditions.Textrusion)