from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


# Condiciones iniciales
condicion_inicial = [10, 0, 0, 0.26]
# ------------------------------------------------------------
''' Metodo Runge-Kutta'''

mercurio = Planeta(condicion_inicial)  # Creacion del planeta
pasos_rk4 = 800
dt_rk4 = 800/pasos_rk4
T_rk4 = np.linspace(0, 800, pasos_rk4)  # Arreglo con los tiempo
x_rk4 = [10]  # Arreglos con posiciones en x
y_rk4 = [0]  # Arreglo con posiciones en y
energia_rk4 = [mercurio.energia_total()]  # Arreglo con las energías

N = 1
while N < pasos_rk4:
    mercurio.avanza_rk4(dt_rk4)
    N += 1
    x_rk4.append(mercurio.y_actual[0])
    y_rk4.append(mercurio.y_actual[1])
    energia_rk4.append(mercurio.energia_total())
# Plots
fig = plt.figure(1)
fig.clf()
plt.plot(x_rk4, y_rk4)
plt.plot(0, 0, 'o', linewidth=10.0, label='Sol')
plt.title('Trayectoria vs Tiempo \n RK4 ')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

fig2 = plt.figure(2)
fig2.clf()
plt.plot(T_rk4, energia_rk4)
plt.title('Energia vs Tiempo \n RK4 ')
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.show()

# ------------------------------------------------------------

''' Metodo Verlet'''

mercurio_verlet = Planeta(condicion_inicial)  # Creacion del planeta
mercurio_verlet.fuerza_actual_x = []
mercurio_verlet.fuerza_actual_y = []

paso_verlet = 8000
dt_verlet = 800/paso_verlet
T_verlet = np.linspace(0, 800, paso_verlet)  # Arreglo con los tiempo
x_verlet = [10]  # Arreglos con posiciones en x
y_verlet = [0]  # Arreglos con posiciones en y
energia_verlet = [mercurio_verlet.energia_total()]  # Arreglos con las energias

N = 1
while N < paso_verlet:
    mercurio_verlet.avanza_verlet(dt_verlet)
    N += 1
    x_verlet.append(mercurio_verlet.y_actual[0])
    y_verlet.append(mercurio_verlet.y_actual[1])
    energia_verlet.append(mercurio_verlet.energia_total())
# Plots
fig = plt.figure(3)
plt.plot(x_verlet, y_verlet)
plt.plot(0, 0, 'o', linewidth=10.0, label='Sol')
plt.title('$Trayectoria$ $vs$ $Tiempo$ \n $Verlet$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

fig2 = plt.figure(4)
plt.plot(T_verlet, energia_verlet)
plt.title('Energia vs Tiempo \n Verlet ')
plt.xlabel('$Tiempo$')
plt.ylabel('$Energia$')
plt.show()

# ------------------------------------------------------------

''' Metodo Beeman'''
condicion_inicial = [10, 0, 0, 0.3]
mercurio_beeman = Planeta(condicion_inicial)  # Creacion del planeta
mercurio_beeman.fuerza_actual_x = []
mercurio_beeman.fuerza_actual_y = []
paso_beeman = 8000
dt_beeman = 800/paso_beeman
T_beeman = np.linspace(0, 800, paso_verlet)  # Arreglo con los tiempo
x_beeman = [10]  # Arreglo posiciones en x
y_beeman = [0]  # Arreglo posiciones en y
energia_beeman = [mercurio_beeman.energia_total()]  # Arreglo con energias

N = 1
mercurio_beeman.avanza_rk4(dt_beeman)
N += 1
while N < paso_beeman+1:
    mercurio_beeman.avanza_beeman(dt_beeman)
    N += 1
    x_beeman.append(mercurio_beeman.y_actual[0])
    y_beeman.append(mercurio_beeman.y_actual[1])
    energia_beeman.append(mercurio_beeman.energia_total())

# Plots
fig = plt.figure(5)
plt.plot(x_beeman, y_beeman)
plt.plot(0, 0, 'o', linewidth=10.0, label='Sol')
plt.title('$Trayectoria$ $vs$ $Tiempo$ \n Beeman')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

fig2 = plt.figure(6)
plt.plot(T_beeman, energia_beeman)
plt.title('Energia vs Tiempo \n Beeman ')
plt.xlabel('$Tiempo$')
plt.ylabel('$Energia$')
plt.show()

# ------------------------------------------------------------

''' Metodo Beeman con alpha = 10**(-2.572)'''
condicion_inicial = [10, 0, 0, 0.2]
# Creacion del planeta
mercurio_beeman_alpha = Planeta(condicion_inicial, 10**(-2.572))
mercurio_beeman_alpha.fuerza_actual_x = []
mercurio_beeman_alpha.fuerza_actual_y = []
paso_beeman_alpha = 600000
dt_beeman_alpha = 4500/paso_beeman_alpha
# Arreglo con los tiempo
T_beeman_alpha = np.linspace(0, 4500, paso_beeman_alpha)
x_beeman_alpha = [10]  # Arreglo posiciones en x
y_beeman_alpha = [0]  # Arreglo posiciones en y
# Arreglo con las energias
energia_beeman_alpha = [mercurio_beeman_alpha.energia_total()]

N = 1
mercurio_beeman_alpha.avanza_rk4(dt_beeman_alpha)
N += 1
while N < paso_beeman_alpha+1:
    mercurio_beeman_alpha.avanza_beeman(dt_beeman_alpha)
    N += 1
    x_beeman_alpha.append(mercurio_beeman_alpha.y_actual[0])
    y_beeman_alpha.append(mercurio_beeman_alpha.y_actual[1])
    energia_beeman_alpha.append(mercurio_beeman_alpha.energia_total())

# Plots
fig = plt.figure(7)
plt.plot(x_beeman_alpha, y_beeman_alpha)
plt.plot(0, 0, 'o', linewidth=10.0, label='Sol')
plt.title('$Trayectoria$ $vs$ $Tiempo$ \n Beeman con alpha=$10^{-2.572}$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

fig2 = plt.figure(8)
plt.plot(T_beeman_alpha, energia_beeman_alpha)
plt.title('Energia vs Tiempo \n Beeman con alpha=$10^{-2.572}$ ')
plt.xlabel('$Tiempo$')
plt.ylabel('$Energia$')
plt.show()


# Calculo de afelio y velocidad angular de presecion
r = []  # Arreglo con los radios
rMax = []  # Afelio
Angulos = []
Tiempos = []
W = []  # Arreglo con velocidades angulares
Wtot = 0
for a in range(len(x_beeman_alpha)):
    r.append(np.sqrt(x_beeman_alpha[a]**2+y_beeman_alpha[a]**2))
for a in range(len(x_beeman_alpha)-2):
    if r[a+1] > r[a] and r[a+1] > r[a+2]:
        rMax.append(r[a+1])
        alfa = np.arctan((abs(y_beeman_alpha[a+1]))/abs(x_beeman_alpha[a+1]))
        Angulos.append(alfa)

        Tiempos.append((a+1)*4500/600000)

for a in range(len(Angulos)-1):
    omega = (Angulos[a+1]-Angulos[a])/(Tiempos[a+1]-Tiempos[a])
    W.append(omega)
for a in W:
    Wtot += a
print('La velocidad angular promedio es: '+str(round(Wtot/len(W), 8)))
