from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import warnings
import sympy
sympy.init_printing()


# Données du problème

# Propriétés mécaniques
alpha = 41*10**-6
rho = 1.25*10**3
# Propriétés thermiques
h = 100 # A déterminer
k = 0.13
Cp = 1800
D = k/(rho*Cp)
# Températures
Tbanc = 338
Textrusion = 453
Tamb = 295
# Maillage
nx = 5
dx = 200*10**-6
longueur = dx*(nx-1)
dt = rho*Cp*dx**2/(2*k*10) # Critère de stabilité dt/dx**2 < rho*Cp/(2*k)
temps = 20
nt = int(temps/dt)+1

# Constantes
C1 = dt*D/dx**2
C2 = 2*h*dx/k

# Création matrice

M = np.zeros((nx,nx))
Vsup = Vinf = np.ones((nx-1,1))*C1
Vdiag = np.ones((nx,1))*(1-2*C1)
np.fill_diagonal(M[1:],Vinf)
np.fill_diagonal(M,Vdiag)
np.fill_diagonal(M[:,1:],Vsup)

# Conditions aux limites

# Dirichlet en x = 0

V0 = np.zeros((1,nx))
V0[0,0] = 1
M[0,:] = V0

# Neumann en x = nx-1

Vnx = np.zeros((1,nx))
Vnx[0,nx-2] = 2*C1
Vnx[0,nx-1] = 1-C1*(C2+2)
M[nx-1,:] = Vnx

Vamb = np.zeros((nx,1))
Vamb[nx-1] = C1*C2*Tamb # Ajout du terme constant

# Résolution

# Conditions initiales

T = np.ones((nx,1))*Textrusion
T[0] = Tbanc

# Equation

Ttot = T
for t in range (nt-1):
    T = np.dot(M,T)+Vamb
    Ttot = np.append(Ttot,T,axis=1)

# Figure

t = np.linspace(0,nt*dt,nt)

fig = plt.figure()
axes = fig.add_subplot(1,1,1)
for i in range (nx):
    axes.plot(t,Ttot[i,:],label='Couche'+str(i))
axes.set_xlabel("Time (s)",fontsize=16)
axes.set_ylabel("Temperature (K)",fontsize=16)
axes.set_title("Evolution of the temperature of the layers")
axes.set_xlim((t.min(),t.max()))
axes.set_ylim((Ttot.min(),Ttot.max()))
axes.legend(loc='best')
axes.grid()
plt.show()









