#
# PYTHON for DUMMIES 23-24
# Problème 2
#
# Splines cubiques périodiques
#
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 


from numpy import *
from numpy.linalg import solve
import time


# ============================================================
# FONCTIONS A MODIFIER [begin]
#
#

def spline(x, h, U):
  start = time.time()

  # Creating abscisses
  n = size(U)
  X = arange(0, n+1)*h

  # Solving linear system
  A = (h**2/6)*(identity(n)*4 + eye(n, k=1) + eye(n, k=-1))   
  A[0][-1] = h**2/6
  A[-1][0] = h**2/6
  b = zeros_like(U)
  b[1:-1] = U[:-2] - 2*U[1:-1] + U[2:]
  b[0] = U[-1] - 2*U[0] + U[1]  
  b[-1] = U[-2] - 2*U[-1] + U[0]
  d2U = solve(A, b)

  # Evaluating cubics
  i = zeros(len(x), dtype=int)
  for j in range(1, n):
      i[X[j]<=x] = j
    
  U = append(U, U[0])
  d2U = append(d2U, d2U[0])

  end = time.time()
  print("Execution time :", end-start)

  return ((d2U[i]*(X[i+1]-x)**3)/(6*h) + 
          (d2U[i+1]*(x-X[i])**3)/(6*h) + 
          (U[i]/h - d2U[i]*h/6)*(X[i+1]-x) + 
          (U[i+1]/h - d2U[i+1]*h/6)*(x-X[i]))

#
# FONCTIONS A MODIFIER [end]
# ============================================================
#
# -1- Interpolation d'un cercle :-)     
#

def main() :

  from matplotlib import pyplot as plt
  plt.rcParams['toolbar'] = 'None'
  plt.rcParams['figure.facecolor'] = 'lavender'

  n = 4
  h = 3*pi/(2*(n+1))
  T = arange(0,3*pi/2,h)
  X = cos(T); Y = sin(T)

  fig = plt.figure("Splines cubiques et cercle :-)")
  plt.plot(X,Y,'.r',markersize=10)
  t = linspace(0,2*pi,100)
  plt.plot(cos(t),sin(t),'--r')

  t = linspace(0,3*pi/2,100)
  plt.plot(spline(t,h,X),spline(t,h,Y),'-b')
  plt.axis("equal"); plt.axis("off")
  plt.show()
 
if __name__ == '__main__': 
  main()
