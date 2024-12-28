comenzar=int(input('¿Que numero quiere multiplicar? '))
finalizar=int(input('¿desde que numero quieres multiplicarlo? '))
for finalizar in range(finalizar,comenzar+1):
    resultado=finalizar*comenzar
    print(finalizar,' x ',comenzar,' = ',resultado)
    
