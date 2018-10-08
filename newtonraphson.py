"""
Program to solve equation using newton raphson
"""

import matplotlib.pyplot as plt

def f(x):
	return pow(x,3) + 3*pow(x,2) + 2*x +100

def f_d(x):
	return 3*pow(x,2) + 6*x + 2 

X_array = []
F = []

for i in range(1,100):
	X_array.append(i)
	F.append(f(i))
	
plt.plot(X_array,F)
plt.xlabel('Points')
plt.ylabel('Value of Function')
plt.show()

fac_relax = 0.5
tol = 1e-6

for x_guess in range(1,100):	
	x_guess_n = x_guess - fac_relax*(f(x_guess)/f_d(x_guess))
	x_guess_n = x_guess
	print(x_guess)

