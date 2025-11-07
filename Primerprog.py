#Revisar si una condicion es mayor a 
balance = 0
if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')
    
#Likes 
likes = 200
if likes >= 200:
    print('Excelente, 200 Likes')
else:
    print('Casi llegas a los 200')

#if con texto
lenguaje = 'Python'
if not lenguaje == 'Python': #la condicion se cumple pero la estamos negando
    print('Excelente desicion')
    
#Evaluar un boolean
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')