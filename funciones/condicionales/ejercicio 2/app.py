def edad(año_actual,año_nacimiento):
    Edad=año_actual-año_nacimiento
    if Edad>17:
        return "Eres mayor de edad tienes ",Edad
    else:
        return 'Eres menor de edad tienes ',Edad
num1=int(input('Di el año actual: '))
num2=int(input('Di tu año de nacimiento: '))
print(edad(año_actual=num1,año_nacimiento=num2))