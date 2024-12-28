def promedio(not1, not2,not3):
    return (not1+not2+not3)/3
not1=int(input('Primer nota: '))
not2=int(input('Segunda nota: '))
not3=int(input('tercer nota: '))
print(f'El promedio de las tres notas es: {promedio(not1, not2,not3)}')
