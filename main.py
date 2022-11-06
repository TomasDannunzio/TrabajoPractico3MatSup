import matplotlib.pyplot as plt
import numpy as np

f = open("D:\\Downloads\\Potencial de acción medido.txt", "r")

texto = f.read()

lista = texto.split("\n")

arregloMedidos = []

for i in range(1,len(lista),1):
    x = lista[i].partition(";")[2]
    arregloMedidos.append(float(x))

arregloMedidos.pop(0)

tiempo = np.arange(0, 6, 0.03333).tolist()

tiempo.pop()

print(len(tiempo), " ", len(arregloMedidos))

plt.plot(tiempo, arregloMedidos)
plt.xlabel("Tiempo - microsegundos")
plt.ylabel("Potencial Medido - mV")
plt.show()
