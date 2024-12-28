def notas(nota,porcentaje):
    return (nota*(porcentaje/100))/100
def porcentaje(num1,num2,num3):
    suma=num1+num2+num3
    if suma>4.5:
        return 'Superior'
    else: 
        if suma<=4.4 and suma>3.5:
            return 'buena'
        else:
            if suma <=3.5 and suma>=3.0:
                return 'medio'
            else:
                return 'mala'
     
not1=float(input('Primer nota: '))
not2=float(input('Segunda nota: '))
not3=float(input('tercer nota: '))

print(f'La suma de los porcentajes es: {porcentaje(notas(not1,0.2), notas(not2,.35),notas(not3,.45))}')

