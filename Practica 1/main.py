"""
Escribe el codigo necesario para capturar varios numeros y almacenarlos en una
lista de valores numericos
1.- De la lista capturada, imprime una sublista de 2 elementos que corresponda
    a la mitad de la lista original, independientemente de la cantidad de elementos
    capturados
2.- De la lista original, imprime en una sola linea de codigo el primer elemento y
    el utlimo
3.- En la lista original, agrega los elementos de la lista al final de la misma
    e imprime el resultado
4.- De la lista obtenida, ordena los elementos de menor a mayor e imprime el
    resultado
5.- Vuelve a ordenar sus elementos de mayor a menor e imprime su resultado
6.- Escribe una funcion que devuelva el cubo de los elementos de la lista e
    imprime el resultado
"""

def findMiddleElements(listNums, middle):
    if len(listNums) > 1:
        left = listNums[:middle]
        right = listNums[middle:]
        leftElement = left[len(left) - 1: len(left)] if len(left) > 1 else left
        rightElement = right[0: 1] if len(right) > 1 else right
        print(f"""
        List:         {listNums}
        Middle:       {middle}
        Left:         {left}
        Right:        {right}
        Left element: {leftElement}
        Right element:{rightElement}
        """)
    else:
        print(f"""
        El arreglo es demasiado corto, por lo tanto no fue posible obtener 2 elementos que correspondan 
        a la mitad de la lista original
              returned value: [void, {listNums[0]}]""")

def listManager():
    listNums = list()
    listSize = int(input('Ingrese el largo del arreglo: '))
    for i in range(listSize):
        listNums.append(int(input(f'Valor {i+1}: ')))

    #Punto 1
    middle = len(listNums) // 2
    print(findMiddleElements(listNums, middle))

    #Punto 2
    print(listNums[0::len(listNums)-1] if len(listNums) > 1 else f'[{listNums[0]}, void]')

    #Punto 3
    listNumsTemp = []
    for i in range(len(listNums)-1, -1, -1):
        listNumsTemp.append(listNums[i])
    print(f'Lista: {listNumsTemp}')

    #Punto 4 - menor a mayor
    listNumsTemp.sort()
    print(f'Sorted List: {listNumsTemp}')

    #Punto 5 - mayor a menor
    listNumsTemp.sort(reverse=True)
    print(f'Reversed List: {listNumsTemp}')

    #Punto 6 - Cubo de los elementos
    square = []
    for i in range(len(listNumsTemp)):
        square.append(listNumsTemp[i] ** 3)
    for i in range(len(listNumsTemp)):
        print(f'El cuadrado de {listNumsTemp[i]} es {square[i]}')

if __name__ == '__main__':
    listManager()
