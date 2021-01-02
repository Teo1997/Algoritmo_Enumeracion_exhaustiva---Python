#Enumeración exhaustiva
objetivo = int(input('Escoge un entero: ')) #Encontrar la raiz cuadrada de un numero
respuesta = 0

while respuesta**2 < objetivo: #Mientras el cuadrado de un numero sea menor que el objetivo
    print(respuesta) #Di el numero actual
    respuesta += 1 #Agregale uno al numero actual

if respuesta**2 == objetivo: #Si se encuentra raiz cuadrada exacta
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')  #Imprime la oracion siguiente con las variables objetivo y respuesta
else: #Si no tiene variable exacta
    print(f'{objetivo} no tiene una raiz cuadrada exacta') #Imprime lo anterior```