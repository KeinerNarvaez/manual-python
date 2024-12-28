finalizar=int(input('¿desde que numero quieres multiplicarlo? '))
numero=int(input('¿hasta que numero quieres que multiplique de 5 en 5? '))
par=0
impar=0
contar=1
while finalizar<=numero:

    contar=1
    while contar<=5:
        resultado=contar*finalizar
        if resultado%2==0:
            print(contar,' x ',finalizar,' = ',resultado,' es par')
            par=par+1
        else:
            print(contar,' x ',finalizar,' = ',resultado,' es impar')
            impar=impar+1
        contar=contar+1
    print('-----------------------')
    finalizar=finalizar+1
print(f'Veces de pares: {par} \nVeces impares: {impar}')
