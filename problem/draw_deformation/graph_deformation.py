import numpy as np
import matplotlib.pyplot as plt

class Graph_Deformation():
    
    def __init__(self, matrix_generation, solution, deformation_calculation):
        
        self.matrix_generation = matrix_generation
        self.solution = solution
        self.deformation_calculation = deformation_calculation
        self.do_graph()
        
    def do_graph(self):
        
        self.t = np.linspace(0,(self.solution.nt+self.solution.nt1+self.solution.nt2)*self.matrix_generation.dt,self.solution.nt+self.solution.nt1+self.solution.nt2+1)
        fig = plt.figure()
        axes = fig.add_subplot(1,1,1)
        axes.plot(self.t,self.deformation_calculation.Eps)
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Deformation",fontsize=16)
        axes.set_title("Evolution of the deformation during the time")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((self.deformation_calculation.Eps.min(),self.deformation_calculation.Eps.max()))
        axes.grid()
        plt.show()