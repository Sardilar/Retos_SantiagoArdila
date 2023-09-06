def Palindromo(palabra):
   
    palabra = palabra.replace(" ", "").lower()
    
    if palabra == palabra[::-1]:
        return True
    else:
        return False
        
palabra_usuario = input("Por favor, ingresa una palabra: ")

if Palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' Esta palabra es un palíndromo.")
else:
    print(f"'{palabra_usuario}' Esta palabra no es un palíndromo.")
