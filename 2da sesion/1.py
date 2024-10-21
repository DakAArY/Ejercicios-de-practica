"""
Suma de una lista de números:
Escribe una función recursiva que tome una lista de números y devuelva la suma
de todos los elementos de la lista.
"""

def main():
    def suma_lista(lista):
        #Caso base: si la lista está vacia, devolver 0
        if not lista:
            return 0
        
        #Caso recursivo: sumar el primer elemento al resultado de la suma del resto de la lista
        return lista[0] + suma_lista(lista[1:]) #Se hace slicing para obtener el resto de la lista, obteniendo todos menos el primer elemento
    
    #Solicitar al usuario que ingrese una lista de numeros
    numeros = input("Ingrese una lista de numeros separados por comas: ").split(',')
    
    #Convertir los numeros a enteros y almacenarlos en una lista mediante list comprehension
    numeros = [int(num) for num in numeros]
    
    resultado = suma_lista(numeros)
    
    print(f"La suma de los numeros es: {resultado}")

if __name__ == "__main__":
    main()