def contador(num1,num2):
    while num1<=num2:
        print(num1)
        num1=num1+1
    return print('Finalizo')
    
num1=int(input('¿Desde donde quiere contar? '))
num2=int(input('¿Hasta que numero quiere contar? '))
contador(num1,num2)