año_nacimiento = int(input('Año de nacimiento: ')) 
año_actual = int(input('Año actual: '))
edad=año_actual-año_nacimiento
if edad >17:
    print('Es mayor de edad, tienes',edad)
else:
    print('Es menor de edad, tienes',edad)
