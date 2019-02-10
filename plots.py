import numpy as np
import matplotlib.pyplot as plt

M = np.array([[1,1],[-2,2],[4,-7]])

print("Vector 1")
#pinta el vector 0 de M des de l'inici fins al final
print(M[0,:])
print("vector:2")
# el mateix que abans però amb el segon vector
print(M[1,:])
# Retorna una tupla amb els valors dels elements de les files i les columnes.
rows,cols = M.T.shape
print(M.T.shape)

for i,l in enumerate(range(0,cols)):
    print("Iteration: {}-{}".format(i,l))
    print("vector:{}".format(i))
    print(M[i,:])
    # Crea un vector nou en funció de els valors i de M. Hi afegeix el punt [0,0]
    # M[i,0], és la posicio 0 del vector i de M.
    v1 = [0,0],[M[i,0],M[i,1]]
    # v1 = [M[i,0]],[M[i,1]]
    print(v1)
    # Genera la figura numero i
    plt.figure(i)
    # Crea la gràfica referent a v1
    plt.plot(v1)
    plt.show()
