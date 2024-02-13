# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 22-23
#
# Homework 1 : Interpolation de Padé
#
# Solution detaillée
#
#  Vincent Legat
#  Nathan Coppin
#
# -------------------------------------------------------------------------

from numpy import *
from numpy.linalg import solve


def padeInterpolationCompute(X,U):

  n = len(X) // 2 
  A = array([X**i for i in range(n+1)] + [-array(U)*array(X)**i for i in range(1,n+1)]).T
  return solve(A,U)

  
def padeEval(a,x) :

  n = len(a) // 2
  A = array([x**i for i in range(1,n+1)]).T
  return (a[0] + A@a[1:n+1])/(1 + A@a[n+1:]) 
  
