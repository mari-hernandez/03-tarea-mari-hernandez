from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

#Condiciones iniciales
condicion_inicial=[10, 0, 0, 0.26]  
mercurio=Planeta(condicion_inicial)
pasos_rk4=800                            
dt_rk4=800/pasos_rk4                         
T_rk4=np.linspace(0,800, pasos_rk4)   
x_rk4=[10]
y_rk4=[0]
energia_rk4=[mercurio.energia_total()]

N=1        
while N<pasos_rk4:               
    mercurio.avanza_rk4(dt_rk4)
    N+=1
    x_rk4.append(mercurio.y_actual[0])
    y_rk4.append(mercurio.y_actual[1])
    energia_rk4.append(mercurio.energia_total())
#Plots
fig=plt.figure(1)
fig.clf()
plt.plot(x_rk4,y_rk4)
plt.title('Trayectoria vs Tiempo \n RK4 con v_{y}(0)=0.26$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

fig2=plt.figure(2)
fig2.clf()
plt.plot(T_rk4, energia_rk4)
plt.title('Energia vs Tiempo \n RK4 con v_{y}(0)=0.26')
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.show()

#-------------------------------------------------------------#

mercurio_verlet=Planeta(condicion_inicial)

paso_verlet=8000                          #Aca la cantidad de pasos no influye mucho, pero
dt_verlet=800/paso_verlet                         #se observo que con tiempo de 800 da las 5 vueltas
T_verlet=np.linspace(0,800, paso_verlet)
x_verlet=[10]
y_verlet=[0]
energia_verlet=[mercurio_verlet.energia_total()]

N=1            #Variable auxiliar para interar
while N<paso_verlet:         #Aplica el metodo de verlet definido en la clase planeta.
    mercurio_verlet.avanza_verlet(dt_verlet)
    N+=1
    x_verlet.append(mercurio_verlet.y_actual[0])
    y_verlet.append(mercurio_verlet.y_actual[1])
    energia_verlet.append(mercurio_verlet.energia_total())
#Plots
fig=plt.figure()
fig.add_subplot(211)
plt.plot(x_verlet,y_verlet)
plt.title('$Trayectoria$ $y$ $Energia$ $vs$ $Tiempo$ \n $Verlet$ $Con$ $v_{y}(0)=0.27$')
plt.xlabel('$x$')
plt.ylabel('$y$')
fig.add_subplot(212)
plt.plot(T_verlet, energia_verlet)
plt.xlabel('$Tiempo$')
plt.ylabel('$Energia$')
plt.show()
