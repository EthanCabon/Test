

class HeatTransfer: 

    def __init__(self, deck):
        self.alpha = float(deck.doc["Materials"]["Mechanical"]["Coefficient of Thermal Expansion"])
        self.rho = float(deck.doc["Materials"]["Mechanical"]["Density"])
        self.h = float(deck.doc["Materials"]["Thermal"]["Heat Transfer Coefficient"])
        self.f = float(deck.doc["Materials"]["Thermal"]["Thermal Conductivity"])
        self.Cp = float(deck.doc["Materials"]["Thermal"]["Heat Capacity"])
        self.D = self.k/(self.rho*self.Cp)
        self.Tbed = float(deck.doc["Experimental Conditions"]["Bed Temperature"])
        self.Textrusion = float(deck.doc["Experimental Conditions"]["Extrusion Temperature"])
        self.Troom = float(deck.doc["Experimental Conditions"]["Room Temperature"])
        self.dx = float(deck.doc["Simulation"]["dx"])
        self.lenX = float(deck.doc["Simulation"]["lenX"])
        self.time = float(deck.doc["Simulation"]["time"])
        self.nx = int(self.lenX/self.dx+1)
        self.dt = float(self.rho*self.Cp*self.dx**2/(2*self.k*10))
        self.nt = int(self.time/self.dt+1)

    def do_timestep(self, u0, u, Diffx, Diffy):
        # Propagate with forward-difference in time, central-difference in space
        u[1:-1, 1:-1] = u0[1:-1, 1:-1] + Diffx[1:-1, 1:-1]* self.dt * ((u0[2:, 1:-1] - 2*u0[1:-1, 1:-1] + u0[:-2, 1:-1])/self.dx2 )+ Diffy[1:-1, 1:-1]* self.dt * ( (u0[1:-1, 2:] - 2*u0[1:-1, 1:-1] + u0[1:-1, :-2])/self.dy2 )
        u0 = u.copy()
        
        return u0, u