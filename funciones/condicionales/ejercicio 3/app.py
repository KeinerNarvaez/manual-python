def mayor(num1,num2):
    if num1==num2:
        return 'Son iguales'
    else:
        if num1>num2:
            respuesta=num1,' Es mayor'
            return respuesta
        else:
            respuesta=num2,' Es mayor'
num1=int(input('Primer valor: '))
num2=int(input('Segundo valor: '))
print (f'La respuesta de la maquina es: {mayor(num1,num2)}')

