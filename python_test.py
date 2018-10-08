"""
Program for calculating thermodynamic properties

Author : Sushrut 
Date : 03 Oct 2018

For Oxygen 

"""
#T>1000
import matplotlib.pyplot as plt

A1 = 3.28253784E+00 
A2 = 1.48308754E-03
A3 = -7.57966669E-07 
A4 = 2.09470555E-10
A5 = -2.16717794E-14 

#T<1000

a1 = 3.78245636E+00
a2 = -2.99673416E-03 
a3 = 9.84730201E-06
a4 = -9.68129509E-09 
a5 = 3.24372837E-12

T = 1500
R = 8.314

plot_interval = 100

for T in range(300,3500):

	if T > 1000:
		Cp = 32*R*(A1 + A2 *T + A3*pow(T,2) + A4*pow(T,3) + A5*pow(T,4))
			
		if T%plot_interval is 0:
				plt.plot(T,Cp, 'o',color='blue')
	
	if T<=1000:
		Cp = 32*R*(a1 + a2 *T + a3*pow(T,2) + a4*pow(T,3) + a5*pow(T,4))
				
		if T%plot_interval is 0:
				plt.plot(T,Cp, 'o',color='red')

plt.xlabel('Temperature')
plt.ylabel('Specific Heat')
plt.grid('on')
plt.show()