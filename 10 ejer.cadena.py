#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

nomb_producto = input("Ingrese el nombre de un producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
unidades = int(input("Ingrese la cantidad de unidades deseadas: "))
total = precio_producto * unidades

print(f"\nEl nombre del producto es: {nomb_producto}")

print(f"\nEl precio unitario del producto es de: {precio_producto}€")

print(f"\nNumero de unidades deseadas: {unidades}")

print(f"\nEl coste total del producto es de: {str(round(total, 2))}€")