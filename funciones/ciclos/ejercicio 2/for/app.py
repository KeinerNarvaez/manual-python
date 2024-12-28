def contador(inicio,fin):
    for inicio in range(inicio,fin+1):
        if inicio%2==0:
            print(f'{inicio} es par')
        else: 
            print(f'{inicio} es impar')            

    return print('Finalizo')
num1=int(input('¿Desde donde quiere contar? '))
num2=int(input('¿Hasta que numero quiere contar? '))
contador(num1,num2)