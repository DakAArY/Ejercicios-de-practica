#Crear un algoritmo que detecte si una palabra ingresada es un palindromo

def main():
    #Se define una funcion recursiva que verifica si una palabra es un palindromo
    def es_palindromo(palabra):
        #Se filtran los caracteres no alfanumericos y se convierten a minusculas
        palabra_fil = ''.join(char.lower() for char in palabra if char.isalnum())
        
        #Caso base: si la palabra tiene 1 o 0 caracteres, se retorna True
        if len(palabra_fil) <= 1:
            return True
        
        #Si el primer y ultimo caracter son iguales, se llama a la funcion con la palabra sin esos caracteres
        if palabra_fil[0] == palabra_fil[-1]:
            return es_palindromo(palabra_fil[1:-1])
        #Si los caracteres no son iguales, se retorna False
        else:
            return False
    #Se pide al usuario que ingrese una palabra
    word =  input("Ingrese una palabra: ")
    
    #Se verifica si la palabra ingresada es un palindromo
    if es_palindromo(word):
        print(f"{word} es un  palindromo")
    #Si no es un palindromo, se imprime un mensaje
    else:
        print(f"{word} no es un palindromo")

if __name__ ==  "__main__":
    main()