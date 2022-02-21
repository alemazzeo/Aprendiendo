import numpy as np
import matplotlib.pyplot as plt


# Ale estuvo aqui

# parametros de entrada
m = 80  # filas
n = 80  # columnas
p = 0.7  # probabilidad

# imagen de entrada
a = (np.random.rand(m, n)) < p

# Hoshen
b = np.array(a, dtype=int)  # genero copia de tipo entero
clases = np.arange((m * n) // 2)  # vector de clases
x = 2  # próxima etiqueta

# Recorro los elementos de la imagen

if b[0, 0] == 1:  # primer elemento, primera fila
    b[0, 0] = x
    x += 1

for i in range(1, n):  # resto de la primer fila
    if b[0, i] == 1:
        if b[0, i - 1] > 0:
            b[0, i] = b[0, i - 1]
        else:
            b[0, i] = x
            x += 1

for i in range(1, m):  # primeros elementos del resto de las filas
    if b[i, 0] == 1:
        if b[i - 1, 0] > 0:
            b[i, 0] = b[i - 1, 0]
        else:
            b[i, 0] = x
            x += 1
    for j in range(1, n):  # resto de los elementos de las filas
        if b[i, j] == 1:
            if b[i, j - 1] != 0 and b[i - 1, j] != 0:
                while clases[b[i, j - 1]] < 0:
                    b[i, j - 1] = -clases[b[i, j - 1]]
                while clases[b[i - 1, j]] < 0:
                    b[i - 1, j] = -clases[b[i - 1, j]]
                if b[i - 1, j] < b[i, j - 1]:
                    b[i, j] = b[i - 1, j]
                    clases[b[i, j - 1]] = -b[i - 1, j]
                elif b[i - 1, j] > b[i, j - 1]:
                    b[i, j] = b[i, j - 1]
                    clases[b[i - 1, j]] = -b[i, j - 1]
                else:
                    b[i, j] = b[i, j - 1]
            elif b[i, j - 1] != 0:
                b[i, j] = b[i, j - 1]
            elif b[i - 1, j] != 0:
                b[i, j] = b[i - 1, j]
            else:
                b[i, j] = x
                x += 1

for i in range(2, x):  # corregir vector
    s = i
    while clases[s] < 0:
        s = -clases[s]
    clases[i] = s

for i, j in np.ndindex((m, n)):  # corregir imagen
    b[i, j] = clases[b[i, j]]

# graficar en consola
print(f"{a.astype(int)}\n\n{b}\n\nclase: {clases[0:x]}")

# graficar con plt
fig, ax = plt.subplots(2, 1)
ax[0].imshow(a)
ax[1].imshow(b, cmap="jet")
ax[0].set_title("Original", fontsize=30)
ax[1].set_title("Labeled", fontsize=30)
plt.show()
