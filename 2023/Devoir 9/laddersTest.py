# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 22-23
# Problème 9
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#

from scipy.linalg import norm,solve

# ============================================================
# FONCTIONS A MODIFIER [begin]
#
#

def f(geometry, var):
  a, b, c = geometry
  x, y = var
  syst1 = [0, 0]
  syst1[0] = (a *x)**2 - (c**2 + x**2)*(x + y)**2
  syst1[1] = (b *y)**2 - (c**2 + y**2)*(x + y)**2
  return syst1

def dfdx(geometry, var):
  a, b, c = geometry
  x, y = var
  dsystdx = [[0, 0], [0, 0]]
  dsystdx[0][0] = a**2 * 2 * x - 2*(x+y)*(c**2 + x*(2*x + y))
  dsystdx[0][1] = -2*(x+y)*(c**2 + x**2)
  dsystdx[1][0] = -2*(x+y)*(c**2 + y**2)
  dsystdx[1][1] =  2 * b**2 * y - 2*(x+y)*(c**2 + y*(2*y + x))
  return dsystdx

def laddersIterate(geometry,x):
  sol = solve(dfdx(geometry, x), f(geometry, x))
  return x - sol 
    
# ============================================================

def laddersSolve(geometry, tol, nmax) :
  a, b, c = geometry
  m = min(a, b)
  if m/2 < c:
    x = [(b-c)/2, (a-c)/2]
  else:
    sol = (m**2 / 4 - c**2) ** 1/2
    x = [sol, sol]
    
    if geometry[0] == geometry[1] :
      return x
    else:
      x[0] *= b**2/a**2
      x[1] *= a**2/b**2
    x[0] = min(x[0], m)
    x[1] = min(x[1], m)
    x[0] = (b-c)/2
    x[1] = (a-c)/2
  n = 0
  delta = tol + 1
  while delta > tol and n < nmax :
    n +=1
    xold = x
    x = laddersIterate(geometry, x)
    delta = norm(x-xold)
  if x[0] <= tol or x[1] <= tol :
    return [-1, -1] 
  return x


    
#
# FONCTIONS A MODIFIER [end]
# ============================================================


def main():
  
# ------------------------------------------------------------------------------------ 
#
# Script de test
#
#
# ------------------------------------------------------------------------------------
#
# -1- Calcul de l'écart entre les deux murs :-)
#

  import numpy as np
  geometry = [3,4,1]
  print(" ========= my Newton-Raphson scheme with your proposed step :-)")

  x = np.array([1.0,1.5]); tol = 10e-12; nmax = 50
  n = 0; delta = tol+1
  while (norm(delta) > tol and n < nmax):
    xold = x
    x = laddersIterate(geometry,xold)
    delta = x-xold; n = n+1
    print(" Estimated error %9.2e at iteration %d : " % (norm(delta),n),x)
  print(" Computed distance is : %13.6f " % sum(x))


  print(" ========= your full computation :-)")
  sol = laddersSolve(geometry,1e-14,50)
  print(" Computed distance is : %13.6f " % sum(sol))

  a = geometry[0]
  b = geometry[1]
  c = geometry[2]
  ab = max(a,b)

#
# -2- Et un joli dessin
#

  import matplotlib.pyplot as plt
  import matplotlib
 
  matplotlib.rcParams['toolbar'] = 'None'
  plt.rcParams['figure.facecolor'] = 'lavender'

  plt.figure("Ladders geometry")
  x = sol[0]; y = sol[1]; d = x + y
  hx = np.sqrt(b*b - d*d); hy = np.sqrt(a*a - d*d)
  plt.plot([-x,y],[hx,0],'-r')
  plt.plot([-x,y],[0,hy],'-b')
  plt.plot([-x,-x,y,y],[ab,0,0,ab],'k')
  plt.axis('equal')
  ax = plt.gca()
  ax.yaxis.grid(color='gray',linestyle='dashed')
  ax.xaxis.grid(color='gray',linestyle='dashed')
  plt.xticks(np.arange(-ab,ab+1,1))
  plt.yticks(np.arange(0,ab+1,1))
  plt.show()
  
  
  
main()  
