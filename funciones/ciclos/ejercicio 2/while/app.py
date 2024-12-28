def contador(inicio,fin):
    while inicio<=fin:
        if inicio%2==0:
            print(f'{inicio} es par')
        else: 
            print(f'{inicio} es impar')     
        inicio=inicio+1
        
    return print('Finalizo')
    
inicio=int(input('¿Desde donde quiere contar? '))
fin=int(input('¿Hasta que numero quiere contar? '))
contador(inicio,fin)