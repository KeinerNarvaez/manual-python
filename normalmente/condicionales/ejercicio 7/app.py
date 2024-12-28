not1= float(input("Escribe tu primer nota: "))
not2= float(input("Escribe tu segunda nota: "))
not3= float(input("Escribe tu tercer nota: "))

porcentaje1= not1*.2
porcentaje2= not2*.35
porcentaje3= not3*.45
suma= porcentaje1 + porcentaje2 + porcentaje3
if suma>4.5:
    print('Es superior')
else:
    if suma<=4.5 and suma>3.5:
        print('Es bueno')
    else:
        if suma<=3.5 and suma >=3.0:
            print('Es media')
        else:
            print('Es mala')

print('primer porcentaje: ', porcentaje1,"\nSegundo porcentaje: ", porcentaje2,'\nTercer porcentaje: ',porcentaje3,'\nSuma de los porcentajes: ', suma)
