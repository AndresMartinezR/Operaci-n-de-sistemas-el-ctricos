# Problema de Asignación con CVXPY

Este repositorio resuelve el problema clásico de asignación mediante el uso de la librería **CVXPY** en Python. El objetivo es asignar un conjunto de barcos a puertos de manera que se minimicen los costos de asignación, respetando las restricciones de que cada barco debe ser asignado a un solo puerto y cada puerto debe recibir exactamente un barco.

## Descripción del problema

El problema de asignación consiste en encontrar una asignación óptima de recursos (en este caso, barcos) a tareas (en este caso, puertos) que minimice el costo total, dado que:
- Cada barco debe ser asignado a un solo puerto.
- Cada puerto debe recibir exactamente un barco.

En este caso, el **costo de asignación** entre barcos y puertos está representado por una matriz, donde cada elemento \( c_{ij} \) indica el costo de asignar el barco \( i \) al puerto \( j \).

## Enfoque

Este problema se resuelve utilizando **programación lineal entera**, un enfoque clásico para problemas de asignación. La formulación del problema se realiza utilizando la librería **CVXPY**, que permite expresar y resolver problemas de optimización de manera eficiente.

### Variables de decisión

Las variables de decisión son binarias (\( x_{ij} \)), donde:
- \( x_{ij} = 1 \) si el barco \( i \) es asignado al puerto \( j \).
- \( x_{ij} = 0 \) si no lo es.

### Función objetivo

La función objetivo es minimizar el costo total de asignación, que se calcula como la suma de los productos de los costos de asignación y las variables de decisión \( x_{ij} \).

### Restricciones

Las restricciones son las siguientes:
1. Cada barco debe ser asignado a exactamente un puerto:
   - \( \sum_{j} x_{ij} = 1 \) para todo \( i \).
2. Cada puerto debe recibir exactamente un barco:
   - \( \sum_{i} x_{ij} = 1 \) para todo \( j \).

### Solución

La solución del problema se obtiene utilizando **CVXPY** para resolver el problema de optimización y encontrar la asignación óptima.

## Código

El código está implementado en Python y utiliza las siguientes librerías:
- `cvxpy`: Para definir y resolver el problema de optimización.
- `numpy`: Para trabajar con matrices y operaciones matemáticas.

