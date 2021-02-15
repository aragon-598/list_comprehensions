#código normal
# numeros = [1,2,3,4,5]

# pares = list()

# for i in numeros:
#     if i%2 == 0:
#         pares.append(i)

# print(pares)

'''código con list comprehensions'''
# numeros = [1,2,3,4,5]

# pares = [i for i in numeros if i%2 ==0]
# print(pares)

"""código para capitalizar palabras"""

# words = ['papá','mamá','hijo','wendy','dayana']

# cap = [word.title() for word in words]
# print(cap)

"""código para calcular cuadrado de un número par del 0-9"""

# cuadrados_pares = [cp**2 for cp in range(10) if cp%2 ==0]
# print(cuadrados_pares)

"""código para agregar un numero, su doble y su cuadrado"""

# nums = [(num, num*2, num**2) for num in range(10)]
# print(nums)

""" Doble bucle for"""

saludos = ['hola', 'saludos', 'hi']
nombres = ['j2logo', 'antonio', 'vega']
frases = ['{} {}'.format(saludo.title(), nombre.title()) for saludo in saludos for nombre in nombres]
print(frases)