def contador(inicio,fin):
    for inicio in range(inicio,fin+1):
        resultado=inicio*fin
        print(f'{inicio} x {fin} = {resultado}')           
    return print('Finalizo')
num1=int(input('¿Desde donde quiere contar? '))
num2=int(input('¿Hasta que numero quiere contar? '))
contador(num1,num2)