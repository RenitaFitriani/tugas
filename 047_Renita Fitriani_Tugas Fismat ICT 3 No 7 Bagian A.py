print('Tugas ICT 3 No. 7 Bagian A')
print('Nama = Renita Fitriani')
print('Kelas = FRE 21')
print('NIM = 21030224047')

#library
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Solusi Manual
def f(y,x):
    return x-y**2

ya=lambda x:(5+(25+16*x*np.exp(2*x)-16*np.exp(2*x))**0.5)/(4*np.exp(x))

#Solusi Numerik atau Metode Euler
y0=[2.0]
xs=np.arange(0,0.12,0.02)
us=odeint(f,y0,xs)
ys=us[:,0]
print(us)

#Plotting
plt.plot(xs,ys,'ro', label = "Solusi Numerik")
plt.plot(xs,ya(xs), label="Solusi Manual")
plt.xlabel('nilai x')
plt.ylabel('nilai y')
plt.title('Plot X Sebenarnya dengan X Pendekatan')
plt.legend(loc='lower left', prop={'size':10})
plt.show()
