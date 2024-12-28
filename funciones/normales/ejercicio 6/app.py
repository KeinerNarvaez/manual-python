def notas(nota,porcentaje):
    return (nota*(porcentaje/100))/100
def porcentaje(nota1,nota2,nota3):
    return nota1+nota2+nota3
not1=int(input('Primer nota: '))
not2=int(input('Segunda nota: '))
not3=int(input('tercer nota: '))

print(f'La suma de los porcentajes es: {porcentaje(notas(not1,30), notas(not2,30),notas(not3,40))}')