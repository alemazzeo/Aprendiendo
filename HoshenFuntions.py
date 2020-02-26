"""


"""


import matplotlib.pyplot as plt

def _hoshen():
    m, n = b.shape
    x = 2

    def etiquetar(e, s1, s2, clases, x):
        if e == 1:
            if s2 != 0 and s1 != 0:
                while clases[s2] < 0:
                    s2 = -clases[s2]
                while clases[s1] < 0:
                    s1 = -clases[s1]
                if s1 < s2:
                    clases[s2] = -s1
                    return s1, x
                elif s1 > s2:
                    clases[s1] = -s2
                    return s2, x
                else:
                    return s2, x
            elif s2 != 0:
                return s2, x
            elif s1 != 0:
                return s1, x
            else:
                return x, x + 1
        else:
            return 0, x


    def recorrer(b, clases):
        # primer elemento, primera fila
        b[0, 0], x = etiquetar(e=b[0, 0], s1=0, s2=0, clases=clases, x=x)

        for i in range(1, n):
            # resto de la primer fila
            b[0, i], x = etiquetar(e=b[0, i], s1=b[0, i - 1], s2=0, clases=clases, x=x)

        for i in range(1, m):
            # primeros elementos del resto de las filas
            b[i, 0], x = etiquetar(e=b[i, 0], s1=0, s2=b[i - 1, 0], clases=clases, x=x)
            for j in range(1, n):
                # resto de los elementos de las filas
                b[i, j], x = etiquetar(e=b[i, j], s1=b[i - 1, j], s2=b[i, j - 1], clases=clases, x=x)

    recorrer()
    corregir_vector()
    corregir_imagen()

if __name__ == '__main__':
    # parametros de entrada
    M = 8  # filas
    N = 8  # columnas
    p = 0.7  # probabilidad

    # imagen de entrada
    a = (np.random.rand(M, N)) < p

    # Hoshen
    matriz = np.array(a, dtype=int)  # genero copia de tipo entero
    vector = np.arange((M * N) // 2)  # vector de clases

    recorrer(b=matriz, clases=vector)

    print(matriz)
    print(vector)
