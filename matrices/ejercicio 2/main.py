lista=[1,2,3,4,5,6,7,8,9,10]
par=[]
impar=[]
x=0
for x in range(x,len(lista)):
    if lista[x]%2==0:
        print(f'{lista[x]} es par')
        par.append(lista[x])

    else:
        print (f'{lista[x]} es impar')
        impar.append(lista[x])
print(f'los valores pares son: {par}')
print(f'los valores impares son: {impar}')
