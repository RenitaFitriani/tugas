print('Nama : Renita Fitriani')
print('Kelas : FRE 21')
print('NIM : 21030224047')
print('Transformasi Koordinat Nomor 7')

#Library
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import*

#Input nilai r, t, dan z
r = 4
t = 4*np.pi/3
z = 2

#Perhitungan koordinat kartesius x, y, dan z
x = r*np.cos(t)
print('x = ', x)
y = r*np.sin(t)
print('y = ', y)
z = z
print('z = ', z)

#Plot grafik
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting Grafik 3D')
t = np.linspace (0, t, 100)
z = np.linspace (0, z, 100)
T,Z = np.meshgrid(t,z)

X = r*np.cos(T)
Y = r*np.sin(T)
Z = Z

ax.plot_surface(X, Y, Z)
plt.show()
