"""
Implementa una función que convierta un número decimal a su representación en
cualquier base entre 2 y 16. Incluye la capacidad de manejar la representación
de dígitos mayores a 9 usando letras (A-F).
"""

def main():
    def decimal_a_base(numero, base):
        #Se valida que la base esté entre 2 y 16
        if base < 2 or base > 16:
            #Raise es una instrucción que permite lanzar una excepción
            #Se puede tambien usar return unicamente
            raise ValueError("La base debe estar entre 2 y 16")
        
        digitos = "0123456789ABCDEF"
        #Se crea una lista vacía para almacenar los dígitos
        resultado = ""
        
        #Convertir el numero decimal a la base deseada
        while numero > 0:
            #Se obtiene el residuo de la división
            resto = numero % base
            #Se añade el dígito correspondiente al resultado
            resultado = digitos[resto] + resultado
            #Se actualiza el valor de numero
            numero = numero // base
        
        #Se retorna el resultado o "0" si el número es 0
        return resultado or "0"
    
    numero = int(input("Ingrese un número decimal: "))
    base = int(input("Ingrese la base a la que desea convertirlo (entre 2 y 16): "))
    
    print(f"El número {numero} en base {base} es: {decimal_a_base(numero, base)}")

if __name__ == "__main__":
    main()