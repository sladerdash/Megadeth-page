print("calculadora de precio final con descuento")
numero 1 = int(input("numero 1: "))
ecuacion= int("ecuacion: ")
numero 2 = int(input("numero 2: ") )

def calcular_descuento(precio, descuento):
    precio_final = precio - (precio *  descuento / 100)
    print(f"en total el precio final es: {precio_final}")

calcular_descuento(precio, descuento)