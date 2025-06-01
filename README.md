# Tarea 1 - Graficación de señales continuas y discretas

**Nombre del alumno:** [Tu nombre aquí]  
**Fecha:** 31 de mayo de 2025  

## 🎯 Objetivos

El objetivo de esta tarea es representar gráficamente diferentes tipos de señales, tanto en su forma continua como discretizada. Las señales a graficar son:

- Una señal sinusoidal de frecuencia \( f = 2 \) Hz
- Una señal exponencial decreciente con escalón unitario
- Una señal triangular periódica
- Una señal cuadrada periódica

## 🧠 Descripción del proceso

Para cada señal se definió un intervalo de tiempo \( t \in [-1, 5] \) con al menos 1000 puntos para obtener una gráfica suave en la versión continua. Luego se definió un periodo de muestreo \( T_s = 0.01 \) s para obtener la versión discreta, la cual se superpuso sobre la señal continua.

### 🔧 Librerías utilizadas

- `numpy` para cálculos y generación de señales
- `matplotlib` para graficación
- `scipy.signal` para generar señales periódicas

## 🖼️ Gráficas

Las gráficas se encuentran en la figura generada por `tarea1.py`, con cada señal en su propio subplot.

## 🔗 Repositorio base

[https://github.com/CharlyMercury/pds_upv](https://github.com/CharlyMercury/pds_upv)