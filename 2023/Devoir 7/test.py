from numpy import *
import numpy as np

def stabilityGear(x,y,order):
    # If order is greater than 6, return zero arrays
    if order > 6:
        return np.zeros(order+1), np.zeros_like(x)
    
    coeff = np.array([
    [1, 1],
    [2/3, 4/3, -1/3],
    [6/11, 18/11, -9/11, 2/11],
    [12/25, 48/25, -36/25, 16/25, -3/25],
    [60/137, 300/137, -300/137, 200/137, -75/137, 12/137],
    [60/147, 360/147, -450/147, 400/147, -225/147, 72/147, -10/147]][order-1])

    
    # Calculate the gain for each complex number in z
    z = x + 1j*y
    gain = np.zeros_like(z)
    for i in range(z.shape[0]):
        for j in range(z.shape[1]):
            # Calculate the roots of the polynomial
            roots_of_poly = np.roots([coeff[0]*z[i,j] - 1, *coeff[1:]])
            # Take the absolute value of the roots and find the maximum
            gain[i,j] = np.max(np.abs(roots_of_poly))
    
    return gain, coeff

def main() : 
  order = 3
  n = 100
  x,y = np.meshgrid(np.linspace(-8,8,n),np.linspace(-8,8,n))


  gain,coeff = stabilityGear(x,y,order)

#
# -2- Impression des coefficients de la méthode de Gear
#     Observer l'utilisation du module "fractions" qui permet
#     d'écrire des nombres en virgule flottante sous la forme de fractions !
#     
#     Retirer la ligne np.set_printoptions
#     Noter aussi les astuces dans les paramètres :-)
#     Merci à : https://stackoverflow.com/questions/42209365/numpy-convert-decimals-to-fractions
#
#

  import fractions
  np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
  print("==== Coefficients of Gear's method for order = %d ========== " % order)
  print("     ",end='')
  print(coeff)


#
# -3- Faire le joli plot
#

  import matplotlib.pyplot as plt
  import matplotlib
  matplotlib.rcParams['toolbar'] = 'None'
  plt.rcParams['figure.facecolor'] = 'lavender'
  plt.rcParams['axes.facecolor'] = 'lavender'
  plt.figure("Stability of Gear's method : order = %d" % order)
  plt.contourf(x,y,gain,np.arange(0,1.1,0.1),cmap=plt.cm.jet_r)
  plt.contour(x,y,gain,np.arange(0,1.1,0.1),colors='black',linewidths=0.5)
  ax = plt.gca()
  ax.axhline(y=0,color='r')
  ax.axvline(x=0,color='r')
  ax.yaxis.grid(color='gray',linestyle='dashed')
  ax.xaxis.grid(color='gray',linestyle='dashed')
  ax.set_aspect('equal', 'box')
  plt.show()
  
  
main() 