# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 22-23
# Problème 8
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#

from numpy import *


# ============================================================
# FONCTIONS A MODIFIER [begin]
#  A titre d'exemple, on considère ici le système suivant !
#
#           dudt(t) =  u(t)
#           dvdt(t) =  0.001 * w(t)
#           dwdt(t) =  w(t) 
#

def f(u):
  dudt =   u[1]
  dvdt =   u[2] 
  dwdt = - u[0] *dvdt
  return array([dudt,dvdt,dwdt])
  
#
# Les trois diagnostics sont fournis :-)
#  

def shoot_method(a, h, integrator):
  X, U = integrator(0, [0,0,a],5,h,f)
  return U[-1, 1] - 1
  
def blasius(delta,nmax,tol,h,integrator):
  a = delta[0]; b = delta[1]
  n = 1
  delta = (b - a)/2
  fa = shoot_method(a, h, integrator)
  fb = shoot_method(b, h, integrator)
  messageBadInterval = 'Bad initial interval :-('
  messageMoreIterations = 'Increase nmax : more iterations are needed :-('
  messageGoodJob = 'Convergence observed :-)'
  if fa*fb > 0 : # si on intercepte pas le zero
    return 0, messageBadInterval
  while (abs(delta) >= tol and n <= nmax) :
    delta = (b-a)/2
    n += 1
    x = a + delta
    fx = shoot_method(x, h, integrator)
    if fx*fa > 0 :
      a = x 
    else : 
      b = x
  if n > nmax : # limit of itteration
    return x, messageMoreIterations
  return x, messageGoodJob


#
# FONCTIONS A MODIFIER [end]
# ============================================================


 
def main() :   
     
#
# -1- Schema de Runge-Kutta classique d'ordre 4
# 
  
  def integrator(Xstart,Ustart,Xend,h,f):
    imax = int((Xend-Xstart)/h)
    X = Xstart + arange(imax+1)*h
    U = zeros((imax+1,3)); U[0,:] = Ustart
    for i in range(imax):  
      K1 = f(U[i,:]       )
      K2 = f(U[i,:]+K1*h/2)
      K3 = f(U[i,:]+K2*h/2)
      K4 = f(U[i,:]+K3*h  )
      U[i+1,:] = U[i,:] + h*(K1+2*K2+2*K3+K4)/6     
    return X,U

#
# -2- Utilisation de la méthode de bissection
#     pour obtenir f''(0) afin que f'(\infty) = 1
#

  h   = 0.1
  tol = 1e-7
  nmax = 40
  a,message = blasius([0,1],nmax,tol,h,integrator)
  X,U = integrator(0,[0,0,a],5,h,f)
 
  print(" === Requested f''(0) = %.4f === %s" % (a,message))
  print(" === Obtained final value for f'(-1) = %.4f " % U[-1,1])

#
# -3- Et un joli plot des profils de vitesse
#     de la solution de similitude de Blasius
#     pour une couche limite laminaire
#

  from matplotlib import pyplot as plt
  import matplotlib
  matplotlib.rcParams['toolbar'] = 'None'
  plt.rcParams['figure.facecolor'] = 'lavender'
  plt.rcParams['axes.facecolor'] = 'lavender'

  fig = plt.figure("Blasius equation")
  plt.plot(X,U[:,1]*X - U[:,0],'-b',X,U[:,1],'-r')

  plt.text(1.4,0.8,"f'(x)",color='red',fontsize=12)
  plt.text(1.5,0.2,"f(x)' x - f(x)",color='blue',fontsize=12)
  plt.text(4.95,0.0,"x",color='black',fontsize=12)
  plt.show()
  

main()



