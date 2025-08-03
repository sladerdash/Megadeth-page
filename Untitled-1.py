import random
seguir = "si"
while seguir.lower() == "si" : #lower reduce a minuscula
    a = random.randint(1, 5)
    print("adivina el numero del 1 al 5")
    try:
        numero = int(input("escribi un numero: ")) 
        if numero in range (1, 6):
            3
            if numero == a  : 
                print("acertaste!!")
            else: 
                print(f"na, era el {a}")
        else: 
            print("numero fuera de rango")
    except ValueError:
        print("ese no es un numero entero valido")

    seguir = input("intentar denuevo? (Si/No): ") #input deja escribir al user, int es para que solo escriba numero
len() #cuenta las letras
print(type()) #type es el tipo de valor
variable.find("") #hace que busque en la variable que queramos algun valor
for i in variable: #hace que la variable seleccionada se ejecute secuenciamente de arriba a abajo