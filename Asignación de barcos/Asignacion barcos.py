"""
Solucion problema de asignacion mediante la libreria CVXPY
Andres Felipe Martinez Rodriguez
"""

import cvxpy as cp
import numpy as np

# Matriz de costos
Matriz_costo = np.array([[5,4,6,7],
                  [6,6,7,5],
                  [7,5,7,6],
                  [5,4,6,6]])

#Definir varibales de desicion las cuales son binarias
numero_filas = Matriz_costo.shape[0] #Numero de filas, como es cuadrada solo se requiere este valor
x_ij = cp.Variable((numero_filas,numero_filas), boolean= True)

#Funcion Objetivo
Funcion_Objetivo = cp.sum(cp.multiply(Matriz_costo, x_ij))

#Restricciones
Restricciones = []#Se crea lista vacia para las restricciones

# Cada barco debe asignarse a exactamente un puerto
for i in range(numero_filas):
    Restricciones.append(cp.sum(x_ij[i, :]) == 1)  # La suma en cada fila debe ser 1

# Cada puerto debe recibir exactamente un barco
for j in range(numero_filas):
    Restricciones.append(cp.sum(x_ij[:, j]) == 1)  # La suma en cada columna debe ser 1

#La restriccion de las variables de tipo binarias ya estan inmersas cuando se definieron las variables de decision

#Solucion del problema por medio de cp.Problem( min o max funcion obejtivo, restricciones)
Problema = cp.Problem(cp.Minimize(Funcion_Objetivo), Restricciones)

#Se usa solve() para encontrar os valores optimos que minimizan la funcion obejtivo
Problema.solve()

# Resultados
print("Matriz de asignación:")
print(x_ij.value) #Asignacion optima
print('Costo total:',Problema.value) #Valor al evaluar la funcion objetivo 
