comenzar=int(input('¿Que numero quiere multiplicar? '))
finalizar=int(input('¿desde que numero quieres multiplicarlo? '))
for finalizar in range(finalizar,6):
    resultado=finalizar*comenzar
    if resultado%2==0:
        print(finalizar,' x ',comenzar,' = ',resultado,' es par')
    else:
        print(finalizar,' x ',comenzar,' = ',resultado,' es impar')
    
