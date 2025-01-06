par = []
impar = []
num3 = 1
matriz = []
matrizx = ""
for num1 in range(5):
    fila = []  
    for num2 in range(5):
        valor = num3 * 5
        fila.append(valor) 
        num3 += 1
        

        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)


        if num1 == num2 or num1 + num2 == 4:
            matrizx += str(valor) , "\t\t"
        else:
            matrizx += "\t\t"
    
    matriz.append(fila) 
    matrizx += "\n"
sumaspar = sum(par)
sumasimpar = sum(impar)
print("Matriz:")
for fila in matriz:
    print(fila)
print("Valores pares:", par)
print("Valores impares:", impar)
print("Suma de pares:", sumaspar)
print("Suma de impares:", sumasimpar)
print("Matris en x:")
print(matrizx)