comenzar=int(input('¿Que numero quiere multiplicar? '))
finalizar=int(input('¿desde que numero quieres multiplicarlo? '))
while finalizar<=5:
    resultado=comenzar *finalizar
    if resultado%2==0:
        print(comenzar,' x ',finalizar,' = ',resultado,' es par')
    else:
        print(comenzar,' x ',finalizar,' = ',resultado,' es impar')
    finalizar=finalizar+1

