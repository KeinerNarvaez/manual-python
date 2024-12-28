dias=int(input('Dias de trabajo: '))
salario=int(input("Valor de dia: "))
valorDia=salario/dias;
salario= dias*valorDia;
salarioMin=1300000
transporte=162000
print("salario de la persona es ", salario);

if salarioMin*2<salario:
    salario= salario+ transporte
else:
    salario= salario+0;


salud = salario*0.12;
pension = salario*0.16;
arl = salario*0.052;

print("la salud: " , salud)
print("la pension: " , pension)
print("el arl: " , arl)

if salarioMin*4<salario:
 salario= salario * 0.04
else:
   salario = salario + 0

deducible= salud+pension+arl
salario= salario-deducible

print("total de pagar: " ,salario)




