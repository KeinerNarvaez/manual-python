def edad(edad):
    if edad>17:
        return "Eres mayor de edad"
    else:
        return 'Eres menor de edad'
Edad=int(input("Di tu edad: "))
print(edad(Edad))