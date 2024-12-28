lado =int(input('Primer lado del primer cuadrado: '))
lado2 =int(input('Segundo lado del segundo cuadrado: '))
lado3= int(input('Tercer lado del tercer cuadrado: '))

area1= lado*lado
area2= lado2*lado2
area3=lado3*lado3
if area1==area2 and area2==area3 and area3==area1:
    print('las areas son iguales')
else:
    if area1>area2 and area1>area3:
        print(area1,' Es mayor')
    else:
        if area2>area1 and area2>area3:
            print(area2,' Es mayor')
        else:
            print(area3, " Es mayor")