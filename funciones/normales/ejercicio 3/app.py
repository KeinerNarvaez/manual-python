def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def division(num1,num2):
    return num1/num2
def multiplicacion(num1,num2):
    return num1*num2
def definidor(num1,num2,operacion):
    if operacion=="suma":
       return suma(num1,num2)
    else: 
        if operacion=='division':
            return division(num1,num2)
        else:
            if operacion=='multiplicacion':
                return multiplicacion(num1,num2)
            else:
                if operacion=='resta':
                    return resta(num1,num2)
                else:
                    return 'Lo siento, el programa no ha entendido lo que quieres hacer, puedes hacer sumas poniendo la palabra suma, restas con la palabra resta y demas como division y multiplicacion'
         
num1=int(input('Primer valor: '))
num2=int(input('Segundo valor: '))  
operacion=input('¿Que operacion desea realizar? ')   
print(f'El resultado de la operacion es: {definidor(num1,num2,operacion)}')
usuario=input('¿Quieres hacerlo otra vez?\nsi/no: ')
while usuario=='si':
    num1=int(input('Primer valor: '))
    num2=int(input('Segundo valor: '))  
    operacion=input('¿Que operacion desea realizar? ')   
    print(definidor(num1,num2,operacion))
    usuario=input('¿Quieres hacerlo otra vez?\nsi/no: ')

