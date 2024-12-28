finalizar=int(input('¿desde que numero quieres multiplicarlo? '))
numero=int(input('¿hasta que numero quieres que multiplique de 5 en 5? '))
par=0
impar=0
contar=1
for finalizar in range(finalizar,numero+1):
    contar=1
    for contar in range(contar,6):
        resultado=contar*finalizar
        if resultado%2==0:
            print(contar,' x ',finalizar,' = ',resultado,' es par')
            par=par+1
        else:
            print(contar,' x ',finalizar,' = ',resultado,' es impar')
            impar=impar+1
    print('-----------------------')
print(f'Veces de pares: {par} \nVeces impares: {impar}')
