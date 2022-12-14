import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

f = open("C:\\Users\\tomid\\Downloads\\Potencial de acción medido.txt", "r")

texto = f.read()

lista = texto.split("\n")

arregloMedidos = []

for i in range(1,len(lista),1):
    x = lista[i].partition(";")[2]
    arregloMedidos.append(float(x))

arregloMedidos.pop(0)

tiempo = np.arange(0, 6, 0.03333)

tiempoLista = tiempo.tolist()

tiempoLista.pop()

print(len(tiempoLista), " ", len(arregloMedidos))

plt.plot(tiempoLista, arregloMedidos)
plt.xlabel("Tiempo - microsegundos")
plt.ylabel("Potencial Medido - mV")
plt.show()

a, b, c, d, e, f, x, y = sp.symbols('a,b,c,d,e,f,x,y')

cubica = sp.sympify(a*x**3+b*x**2+c*x+d)

#print(cubica)

# Utilizaremos una cubica hasta el punto -86.9

primerTramo = []

for i in range(len(arregloMedidos)):
    if arregloMedidos[i] != -86.9:
        primerTramo.append(arregloMedidos[i])
    else:
        primerTramo.append(arregloMedidos[i])
        break

segundoTramo = []

for i in range(len(arregloMedidos)):
    if arregloMedidos[len(arregloMedidos)-1-i] != -86.9:
        segundoTramo.append(arregloMedidos[len(arregloMedidos)-1-i])
    else:
        break

segundoTramo.reverse()

tiempoPrimerTramo = np.arange(0, len(primerTramo)*0.03333, 0.03333)
tiempoSegundoTramo = np.arange(len(primerTramo)*0.03333, len(primerTramo)*0.03333+len(segundoTramo)*0.03333, 0.03333)


#dCda = a*np.sum(tiempo**6) + b*np.sum(tiempo**5) + c*np.sum(tiempo**4) + d*np.sum(tiempo**6) \
#       - np.sum(primerTramo*tiempo**3)
#dCdb = a*np.sum(tiempo**5) + b*np.sum(tiempo**4) + c*np.sum(tiempo**3) + d*np.sum(tiempo**5) \
#       - np.sum(primerTramo*tiempo**2)
#dCdc = a*np.sum(tiempo**4) + b*np.sum(tiempo**3) + c*np.sum(tiempo**2) + d*np.sum(tiempo) \
#    - np.sum(primerTramo*tiempo)
#dCdd = a*np.sum(tiempo**3) + b*np.sum(tiempo**2) + c*np.sum(tiempo) + d \
#    - np.sum(primerTramo)

ecuaciones = np.array([[np.sum(tiempoPrimerTramo**6), np.sum(tiempoPrimerTramo**5), np.sum(tiempoPrimerTramo**4),
                        np.sum(tiempoPrimerTramo**3)],
          [np.sum(tiempoPrimerTramo**5), np.sum(tiempoPrimerTramo**4), np.sum(tiempoPrimerTramo**3),
           np.sum(tiempoPrimerTramo**2)],
          [np.sum(tiempoPrimerTramo**4), np.sum(tiempoPrimerTramo**3), np.sum(tiempoPrimerTramo**2),
           np.sum(tiempoPrimerTramo)],
          [np.sum(tiempoPrimerTramo**3), np.sum(tiempoPrimerTramo**2), np.sum(tiempoPrimerTramo),
           len(tiempoPrimerTramo)]])
vectorB = np.array([np.sum(primerTramo*tiempoPrimerTramo**3), np.sum(primerTramo*tiempoPrimerTramo**2),
                    np.sum(primerTramo*tiempoPrimerTramo), np.sum(primerTramo)])
solucion = np.linalg.solve(ecuaciones,vectorB)

funcionAproximantePrimerTramo = cubica.subs({a: solucion[0], b: solucion[1], c: solucion[2], d: solucion[3]})

aproximantePrimerTramo = []

for i in range(len(tiempoPrimerTramo)):
    aproximantePrimerTramo.append(funcionAproximantePrimerTramo.subs(x,tiempoPrimerTramo[i]))

plt.plot(tiempoPrimerTramo,primerTramo)
plt.plot(tiempoPrimerTramo, aproximantePrimerTramo)
plt.xlabel("Tiempo - [ms]")
plt.ylabel("Voltaje - mV")
plt.show()

recta = sp.sympify(e*x + f)

ecuaciones2 = np.array([[np.sum(tiempoSegundoTramo**2), np.sum(tiempoSegundoTramo)],
                        [np.sum(tiempoSegundoTramo), len(tiempoSegundoTramo)]])
vectorB2 = np.array([np.sum(tiempoSegundoTramo*segundoTramo), np.sum(segundoTramo)])

solucion2 = np.linalg.solve(ecuaciones2, vectorB2)

funcionAproximanteSegundoTramo = recta.subs({e: solucion[1], f: solucion[0]})

print(funcionAproximanteSegundoTramo)

aproximanteSegundoTramo = []

for i in range(len(tiempoSegundoTramo)):
    aproximanteSegundoTramo.append(funcionAproximanteSegundoTramo.subs(x, tiempoSegundoTramo[i]))

plt.plot(tiempoSegundoTramo, segundoTramo)
plt.plot(tiempoSegundoTramo, aproximanteSegundoTramo)
plt.xlabel("Tiempo - [ms]")
plt.ylabel("Voltaje - mV")
plt.show()