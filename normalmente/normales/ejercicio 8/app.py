dias_trabajados=int(input('Dias trabajados: '))
valor_dia= int(input('Valor de dia: '))
sueldo=dias_trabajados* valor_dia
salud= sueldo*0.12
pension=sueldo*0.16
arl=sueldo*.052
descuento=salud+pension+arl
pago_total=sueldo-descuento

print('el pago total es de: ',pago_total)