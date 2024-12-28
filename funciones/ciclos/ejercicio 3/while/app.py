def contador(inicio,fin):
    while inicio<=fin:
        resultado=inicio*fin
        print(f'{inicio} x {fin} = {resultado}')
        inicio=inicio+1
        
    return print('Finalizo')
    
inicio=int(input('¿Desde donde quiere contar? '))
fin=int(input('¿Hasta que numero quiere contar? '))
contador(inicio,fin)