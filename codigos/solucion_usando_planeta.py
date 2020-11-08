from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

#Condiciones iniciales
condicion_inicial=[10, 0, 0, 0.26]  
mercurio=Planeta(condicion_inicial)
pasos=800                            
dt=800/pasos                          
T=np.linspace(0,800, pasos)   
x=[10]
y=[0]
energia=[mercurio.energia_total()]

N=1        
while N<pasos:               
    mercurio.avanza_rk4(dt)
    N+=1
    x.append(mercurio.y_actual[0])
    y.append(mercurio.y_actual[1])
    energia.append(mercurio.energia_total())
#Plots
fig=plt.figure(1)
fig.clf()
plt.plot(x,y)
plt.title('Trayectoria vs Tiempo \n RK4 con v_{y}(0)=0.26$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

fig2=plt.figure(2)
fig2.clf()
plt.plot(T, energia)
plt.title('Energia vs Tiempo \n RK4 con v_{y}(0)=0.26')
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.show()

