import numpy as np                      #importujemy biblioteke numpy i nazywamy ja np
import matplotlib.pyplot as plt

num = 1000

x = np.linspace(0,15,num)               #tworzymy wektor od 0 do 15, 100 elementow (rosnacych liniowo)
x = 15*np.random.rand(num)              #tworzymy wektor od 0 do 15, 100 elementow (liczby pseudoloswe)
n = np.array([0.5, 1, 1.5, 2.0])        #tworzymy wektor, wpisujemy dane

y = np.zeros(num)                       #tworzymy wektor y, na poczatku wypelniony zerami

for i in range(num):                    #petla, i w zakresie of 0 do num co 1
    y[i] = x[i]**np.random.choice(n)
    
plt.plot(x,y,'.',label='E',color='tab:orange')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,15)
plt.ylim(0)
