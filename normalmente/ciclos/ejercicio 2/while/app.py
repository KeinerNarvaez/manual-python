comenzar=int(input('¿desde que numero quieres iniciar a contar? '))
finalizar=int(input('¿hasta que numero quieres contar? '))
while comenzar<=finalizar:
    if comenzar%2==0:
        print(comenzar,' Es par')
    else:
        print(comenzar,' Es impar')
    comenzar=comenzar+1