#Ejemplo con elif
ocupacion = 'Desempleado'


if ocupacion == 'Estudiante':
    print('Tienes 50% de Descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de Descuento')
elif ocupacion == 'Desempleado':
    print('Tienes 10% de Descuento')
else: 
    print('Debes pagar el 100%')
    
