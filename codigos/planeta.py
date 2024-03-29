import numpy as np
from matplotlib import pyplot as plt

G = 1
M = 1
m = 1


class Planeta(object):
    """
    La clase planeta, crea un planeta dadas su condiciones iniciales de
    posicion y velocidad ademas de un alpha opcional.Posee metodos para la
    ecuacion de movimiento de este, y los metodos de runge Kutta 4, Verlet
    y Beeman que avanzan un paso. Tambien se puede calcular la energía total
    del planeta en las condiciones actuales
    """

    def __init__(self, condicion_inicial, alpha=0):
        """
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.
        y_actual guarda posicion y velocidades en el tiempo actual de la forma
        [x, y, vx, vy]
        fuerza_actual_x guarda la fuerza en el eje x en el momento actual
        en la posicion [-1]
        fuerza_actual_y guarda la fuerza en el eje y en el momento actual
        en la posicion [-1]
        t_actual guarda el tiempo
        alpha guarda el valor alpha, el cual si no es especificado
        se toma como 0
        """
        self.y_actual = condicion_inicial
        self.fuerza_actual_x = []
        self.fuerza_actual_y = []
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self):
        """
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        """
        x, y, vx, vy = self.y_actual
        r = (x**2 + y**2)**(1/2)
        fx = - x * (G * M * m / r**3 - 2 * self.alpha * G * M * m / r**4)
        fy = - y * (G * M * m / r**3 - 2 * self.alpha * G * M * m / r**4)
        self.fuerza_actual_x.append(fx)
        self.fuerza_actual_y.append(fy)
        return [vx, vy, fx, fy]

    def avanza_rk4(self, dt):
        """
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de RK4. El método no
        retorna nada, pero modifica los valores de self.y_actual y de
        self.t_actual.
        """
        x, y, vx, vy = self.y_actual
        k1 = self.ecuacion_de_movimiento()
        self.y_actual = [x+k1[0]/2, y+k1[1]/2, vx+k1[2]/2, vy+k1[3]/2]
        k2 = self.ecuacion_de_movimiento()
        self.y_actual = [x+k2[0]/2, y+k2[1]/2, vx+k2[2]/2, vy+k2[3]/2]
        k3 = self.ecuacion_de_movimiento()
        self.y_actual = [x+k3[0], y+k3[1], vx+k3[2], vy+k3[3]]
        k4 = self.ecuacion_de_movimiento()
        x_n = x+(1/6)*dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        y_n = y+(1/6)*dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        vx_n = vx+(1/6)*dt*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
        vy_n = vy+(1/6)*dt*(k1[3]+2*k2[3]+2*k3[3]+k4[3])
        self.y_actual = [x_n, y_n, vx_n, vy_n]
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt):
        """
        Similar a avanza_rk4, pero usando Verlet.
        """
        x, y, vx, vy = self.y_actual
        vx, vy, fx, fy = self.ecuacion_de_movimiento()
        x_n = x+dt*vx+fx*(dt**2)/2
        y_n = y+dt*vy+fy*(dt**2)/2
        self.y_actual = [x_n, y_n, vx, vy]
        vx1, vy1, fx1, fy1 = self.ecuacion_de_movimiento()
        vx_n = vx+fx1*dt/2+fx*dt/2
        vy_n = vy+fy1*dt/2+fy*dt/2
        self.y_actual = [x_n, y_n, vx_n, vy_n]
        self.t_actual += dt
        pass

    def avanza_beeman(self, dt):
        """
        Similar a avanza_rk4, pero usando Beeman.
        """
        x, y, vx, vy = self.y_actual
        fx = self.fuerza_actual_x[-1]
        fy = self.fuerza_actual_y[-1]
        vx, vy, fx_mas1, fy_mas1 = self.ecuacion_de_movimiento()
        x_n = x+vx*dt+(1/6)*(4*fx_mas1-fx)*(dt**2)
        y_n = y+vy*dt+(1/6)*(4*fy_mas1-fy)*(dt**2)
        vx_mas, vy_mas, fx_mas2, fy_mas2 = self.ecuacion_de_movimiento()
        vx_n = vx+(1/12)*(5*fx_mas2+8*fx_mas1-fx)*dt
        vy_n = vy+(1/12)*(5*fy_mas2+8*fy_mas1-fy)*dt
        self.y_actual = [x_n, y_n, vx_n, vy_n]
        self.t_actual += dt
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        x, y, vx, vy = self.y_actual
        r = (x**2+y**2)**(1/2)
        energia_Cinetica = (1/2)*m*(vx**2+vy**2)
        energia_Potencial = -G*M*m/r + self.alpha*G*M*m/r**2
        return energia_Cinetica + energia_Potencial
