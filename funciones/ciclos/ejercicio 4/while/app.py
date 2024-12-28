def contador(inicio,fin):
    while inicio<=fin:
        resultado=inicio*9
        if resultado%2==0:
            print(f'{inicio} x 9 = {resultado} es par')
        else:
            print(f'{inicio} x 9 = {resultado} es impar')
        inicio=inicio+1
    return print('Finalizo')
    
inicio=int(input('¿Desde donde quiere contar? '))
fin=int(input('¿Hasta que numero quiere contar? '))
contador(inicio,fin)