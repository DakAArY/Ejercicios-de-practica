#Crear un algoritmo que detecte si una palabra ingresada es un palindromo

def main():
    def es_palindromo(palabra):
        palabra_fil = ''.join(char.lower() for char in palabra if char.isalnum())
        
        if len(palabra_fil) <= 1:
            return True
        
        if palabra_fil[0] == palabra_fil[-1]:
            return es_palindromo(palabra_fil[1:-1])
        else:
            return False
        
    word =  input("Ingrese una palabra: ")
    
    if es_palindromo(word):
        print(f"{word} es un  palindromo")
    else:
        print(f"{word} no es un palindromo")

if __name__ ==  "__main__":
    main()