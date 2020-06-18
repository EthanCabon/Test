import numpy as np
import matplotlib.pyplot as plt

class Graph_Temperature:
    
    def __init__(self,matrix_generation,solution):
        
        self.matrix_generation = matrix_generation
        self.solution = solution
        self.do_graph()
    
    def do_graph(self):
        self.t = np.linspace(0,(self.solution.nt+self.solution.nt1+self.solution.nt2)*self.matrix_generation.dt,self.solution.nt+self.solution.nt1+self.solution.nt2+1)
        fig = plt.figure()
        axes = fig.add_subplot(1,1,1)
        for i in range (self.matrix_generation.nx):
            axes.plot(self.t,self.solution.Ttot[i,:],label='Layer'+str(i+1))
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Temperature (K)",fontsize=16)
        axes.set_title("Evolution of the temperature of the layers")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((self.solution.Ttot.min(),self.solution.Ttot.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        