def edad(año_nacimiento1,año_nacimiento2,año_nacimiento3,año_actual):
    edad1=año_actual-año_nacimiento1
    edad2=año_actual-año_nacimiento2
    edad3=año_actual-año_nacimiento3
    if edad1>17:
        print(f'{edad1} es mayor de edad')
    else:
        print(f'{edad1} es menor de edad')
    if edad2>17:
        print(f'{edad2} es mayor de edad')
    else:
        print(f'{edad2} es menor de edad')
    if edad3>17:
        print(f'{edad3} es mayor de edad')
    else:
        print(f'{edad3} es menor de edad')
    promedio= (edad1+edad2+edad3)/3
    if promedio>17:
        print(f'El promedio de edades {promedio} es mayor de edad')
    else:
        print(f'El promedio de edades {promedio} es menor de edad')

not1=int(input('Primer año de nacimiento: '))
not2=int(input('Segunda año de nacimiento: '))
not3=int(input('tercer año de nacimiento: '))
actual=int(input('Año actual: '))
print(f'La edades {edad(not1, not2,not3)}')
