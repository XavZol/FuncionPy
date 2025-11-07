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
    
#Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('No no esta en la lista')
    
    
#if anidados
usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')