# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 
# Problème de Lorenz
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#

from numpy import *

# ============================================================
# FONCTION A MODIFIER [begin]
#
#

from numpy import *
import numpy as np

#
# TOUTE AUTRE INSTRUCTION CONTENANT import / from SERA AUTOMATIQUEMENT SUPPRIMEE
#

  
def f(xt):
  ut, vt, wt = xt 
  dudt = 10*vt - 10*ut
  dvdt = 28*ut - vt - ut*wt
  dwdt = ut * vt - 8*wt/3
  ft = array([dudt, dvdt, dwdt])
  return ft

def lorenz(Xstart,Xend,Ustart,n):
  X = linspace(Xstart, Xend, n+1)
  U = ones((n+1,3))
  U[0, :] = Ustart
  h = (Xend - Xstart) / n
  for i in range(1, n+1):
    k1 = f(U[i-1, :])
    k2 = f(U[i-1, :] + h/2 * k1)
    k3 = f(U[i-1, :] + h/2 * k2)
    k4 = f(U[i-1, :] + h * k3)
    U[i, :] = U[i-1, :] + h * (k1 + 2*k2 + 2*k3 + k4)/6
  return X,U

    
#
# FONCTION A MODIFIER [end]
# ============================================================



def main():
  
# ------------------------------------------------------------------------------------ 
#
# Script de test
#
#
# ------------------------------------------------------------------------------------



  from matplotlib import pyplot as plt
  plt.rcParams['toolbar'] = 'None'
  plt.rcParams['toolbar'] = 'None'
  plt.rcParams['figure.facecolor'] = 'lavender'
  plt.rcParams['axes.facecolor'] = 'lavender'


  plt.figure("Lorenz Equations")
  Xstart = 0; Xend = 100;
  Ustart = [0,1,0]
  n = 10000;

  X,U = lorenz(Xstart,Xend,Ustart,n)
  plt.plot(U[:,0],U[:,2],'-r',linewidth=0.5)
  plt.show()



main()  
