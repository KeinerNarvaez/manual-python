def areas(lado1,lado2,lado3):
    area1=lado1* lado1
    area2=lado2*lado2
    area3=lado3*lado3
    if area1==area2 and area2==area3 and area3==area1:
        return 'Son iguales'
    else:
        if area1>area2 and area3<area1:
            respuesta=area1,' el primer cuadro es mayor'
            return respuesta
        else:
            if area2>area1 and area3<area2:
                respuesta=area2, ' el segundo es mayor'
                return respuesta
            else:
                return area3, ' el tercer cuadro es mayor'
num1=int(input('Primer cuadro, pon el lado: '))
num2=int(input('Segundo cuadro, pon el lado: '))
num3=int(input('Tercer cuadro, pon el lado: '))
print (f'La respuesta de la maquina es: {areas(num1,num2,num3)}')