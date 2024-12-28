def contador(inicio,fin):
    for inicio in range(inicio,fin+1):
        resultado=inicio*9
        if resultado%2==0:
            print(f'{inicio} x 9 = {resultado} es par')
        else:           
            print(f'{inicio} x 9 = {resultado} es impar')
    return print('Finalizo')
num1=int(input('¿Desde donde quiere contar? '))
num2=int(input('¿Hasta que numero quiere contar? '))
contador(num1,num2)