#!/usr/bin/env python
import scipy
import numpy as np
import pylab as plt

#Condiciones iniciales
yo=-3.
xo=0.5
yf=3.

#QUEREMOS x(y) desde y=0 hasta y=3.

def mi_f(y,x):
  return -x*y

Npasos=40.
h=(yf-yo)/Npasos
x_euler,y=np.array([xo,]),np.array([yo,])
x_mdpt=np.array([xo,])
x_rk4=np.array([xo,])
for n in np.arange(0,Npasos,1):
  #Metodo de Euler
  y_n_mas_1=y[-1]+h
  x_euler_n_mas_1=x_euler[-1] + h*mi_f(y[-1],x_euler[-1]) 
  x_euler=np.append(x_euler,x_euler_n_mas_1)
  #Metodo de Mid-point
  print len(y), len(x_mdpt)
  k1=h*mi_f(y[-1],x_mdpt[-1])
  k2=h*mi_f(y[-1]+h/2.,x_mdpt[-1]+k1/2.)
  x_mdpt_n_mas_1=x_mdpt[-1]+k2
  x_mdpt=np.append(x_mdpt,x_mdpt_n_mas_1)
  #Runge-kutta 4to orden
  kk1=h*mi_f(y[-1],x_rk4[-1])
  kk2=h*mi_f(y[-1]+h/2.,x_rk4[-1]+kk1/2.)
  kk3=h*mi_f(y[-1]+h/2.,x_rk4[-1]+kk2/2.)
  kk4=h*mi_f(y[-1]+h,x_rk4[-1]+kk3/2.)
  x_rk4_n_mas_1=x_rk4[-1]+(1/6.)*(kk1+2*kk2+2*kk3+kk4)
  x_rk4=np.append(x_rk4,x_rk4_n_mas_1)
  y=np.append(y,y_n_mas_1)


plt.plot(y,x_euler,'b-',label='Euler')
plt.plot(y,x_mdpt,'r-',label='Mid-pt')
plt.plot(y,x_rk4,'g-',label='RK4')
plt.plot(y,np.exp(-0.5*y**2),'k-',label='Analytic')
plt.legend()
plt.show()

