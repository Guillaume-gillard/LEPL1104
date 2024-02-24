# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 22-23
#
# Homework 3 : Splines cubiques périodiques
#
# Solution detaillée préliminaire :-)
# Si y a des trucs géniaux des tuteurs, je la mettrai à jour :-)
#
#  Vincent Legat
#  Nathan Coppin
#
# -------------------------------------------------------------------------

from numpy import *
from numpy.linalg import solve


def spline(x,h,U):

#
# -0- On crée les abscisses
#
    
  n = size(U)
  X = arange(0,n+1)*h
  
#
# -1- Résolution du système linéaire
#
      
  A = zeros((n,n))
  b = zeros(n)
  for i in range(-1,n-1):
    A[i,[i-1,i,i+1]] = [1,4,1]
    b[i] = 6*(U[i-1] - 2*U[i] + U[i+1])/(h*h)
  ddU = solve(A,b)
  
#
# -2- Evaluation des cubiques
#  
  i = zeros(len(x),dtype=int)
  for j in range(1,n):
      i[X[j]<=x] = j
      
  U = append(U,U[0])
  ddU = append(ddU,ddU[0])
           
  s1 = x - X[i]
  s2 = X[i+1] - x  
  return s2 * ((U[i]/h - (ddU[i]*h)/6) 
            + (ddU[i]/(6*h)) * (s2**2)) + \
         s1 * ((U[i+1]/h - (ddU[i+1]*h)/6) 
            + (ddU[i+1]/(6*h)) * (s1**2))
         





    
