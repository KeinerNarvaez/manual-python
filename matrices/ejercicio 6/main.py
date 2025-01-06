listaBusqueda=[]
tienda=[
        {'producto':'Arroz',
        'tipoProducto':'fruver',
        'tipoUnidad':'granos',
        'cantidad':'500',
        'precio':'2450'},

        {'producto':'papa',
        'tipoProducto':'fruver',
        'tipoUnidad':'granos',
        'cantidad':'500',
        'precio':'1000'},
        
        {'producto':'mora',
        'tipoProducto':'fruver',
        'tipoUnidad':'gramos',
        'cantidad':'500',
        'precio':'1500'},

        {'producto':'trucha',
        'tipoProducto':'carnes',
        'tipoUnidad':'gramos',
        'cantidad':'1000',
        'precio':'9000'},

        {'producto':'pollo entero',
        'tipoProducto':'carnes',
        'tipoUnidad':'gramos',
        'cantidad':'500',
        'precio':'4500'}
        ]

nuevoProducto={'producto':'Res',
        'tipoProducto':'carnes',
        'tipoUnidad':'gramos',
        'cantidad':1000,
        'precio':7500}
tienda.append(nuevoProducto)
for iteracion in range(len(tienda)):
    print(tienda[iteracion])
    print('---------------------------------------------------------------------------------------------------------------\n')
for iteracion in range(len(tienda)):
    if tienda[iteracion]['tipoProducto']=='fruver':
        listaBusqueda.append(tienda[iteracion])
    else:
        pass
print('Solo tipo de producto fruver:')
for iteracion in range(len(listaBusqueda)):
    print(listaBusqueda[iteracion])
    print('---------------------------------------------------------------------------------------------------------------\n')
