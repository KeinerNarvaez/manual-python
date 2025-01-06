iteracion1=0
iteracion2=0
acumulador=1
bingo=[]
matriz1=[]
matriz2=[]
matriz3=[]
numero=1

for iteracion1 in range(5):
    fila=[]
    for iteracion2 in range(5):
        fila.append(acumulador*2)
        acumulador=acumulador+1
    bingo.append(fila)
print(bingo)
print('Letra B')
for iteracion1 in range(len(bingo)):
    print(bingo[iteracion1][0])
print('Letra I')
for iteracion1 in range(len(bingo)):
    print(bingo[iteracion1][1])
print('Letra N')
for iteracion1 in range(len(bingo)):
    print(bingo[iteracion1][2])
print('Letra G')
for iteracion1 in range(len(bingo)):
    print(bingo[iteracion1][3])
print('Letra O')
for iteracion1 in range(len(bingo)):
    print(bingo[iteracion1][4])
for fila in range(3):
    for columna in range(3):
        if fila==columna or fila+columna==2:
            matriz1.append(bingo[fila][columna])
fila=2
for fila in range(5):
    for columna in range(3):
        if fila+columna==(columna+1)*2 or fila+columna==4:
            matriz2.append(bingo[fila][columna])
fila=0
columna=2    
for fila in range(3):
    for columna in range(5):
        if fila+columna==(fila+1)*2 or fila+columna==4:
            matriz3.append(bingo[fila][columna])
print(matriz1)
print(matriz2)
print(matriz3)

    
