año_nacimiento1=int(input('Primer año de nacimiento: '))
año_nacimiento2=int(input('Segunda año de nacimiento: '))
año_nacimiento3=int(input('Tercer año de nacimiento: '))
año_actual= int(input('Pon el año actual: '))
edad1=año_actual-año_nacimiento1
edad2=año_actual-año_nacimiento2
edad3=año_actual-año_nacimiento3
if edad1 >17:
    print(edad1,' Es mayor de edad')
else:
    print(edad1,' Es menor de edad')
if edad2 >17:
    print(edad2,' Es mayor de edad')
else:
    print(edad2,' Es menor de edad')
if edad3 >17:
    print(edad3,' Es mayor de edad')
else:
    print(edad3,' Es menor de edad')

suma = edad1+ edad2+ edad3
promedio = suma/3
if promedio>17:
    print('El promedio cumple con la mayoria de edad')
else:
    print('el promedio no cumple la mayoria de edad')
