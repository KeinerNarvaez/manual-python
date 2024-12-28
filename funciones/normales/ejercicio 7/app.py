def ortoedro(num1,num2):
    return num1*num2
def triangulo(num1,num2):
    return (num1*num2)/2
def definidor(num1,num2,operacion):
    if operacion=="cuadrado":
       return ortoedro(num1,num2)
    else: 
        if operacion=='rectangulo':
            return ortoedro(num1,num2)
        else:
            if operacion=='triangulo':
                return triangulo(num1,num2)
            else:
                return 'Lo siento, el programa no ha entendido lo que quieres hacer, puedes hacer hallar el area de un cuadrado poniendo la palabra cuadrado y demas como triangulo y rectangulo'
         
num1=int(input('Primer valor: '))
num2=int(input('Segundo valor: '))  
operacion=input('¿De que figura desea hallar el area? ')   
print(f'El resultado de la operacion es: {definidor(num1,num2,operacion)}')
usuario=input('¿Quieres hacerlo otra vez?\nsi/no: ')
while usuario=='si':
    num1=int(input('Primer valor: '))
    num2=int(input('Segundo valor: '))  
    operacion=input('¿De que figura desea hallar el area? ')   
    print(definidor(num1,num2,operacion))
    usuario=input('¿Quieres hacerlo otra vez?\nsi/no: ')

