comenzar=int(input('¿Que numero quiere multiplicar? '))
finalizar=int(input('¿desde que numero quieres multiplicarlo? '))
while finalizar<=comenzar:
    resultado=finalizar *comenzar
    print(finalizar,' x ',comenzar,' = ',resultado)
    finalizar=finalizar+1

