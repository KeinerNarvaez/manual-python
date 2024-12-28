def contador(inicio,fin):
    par=0
    impar=0
    contar=1
    for inicio in range(inicio,fin+1):
        contar=1
        for contar in range(contar,6):
            resultado=contar*inicio
            if resultado%2==0:
                print(contar,' x ',inicio,' = ',resultado,' es par')
                par=par+1
            else:
                print(contar,' x ',inicio,' = ',resultado,' es impar')
                impar=impar+1
        print('-----------------------')
    print( f'Veces de pares: {par} \nVeces impares: {impar}')
inicio=int(input('¿desde que numero quieres multiplicarlo? '))
fin=int(input('¿hasta que numero quieres que multiplique de 5 en 5? '))
contador(inicio,fin)
