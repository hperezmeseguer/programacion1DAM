articulo = input("Qué compras?:")
numero_ventas = int(input("Cuántas unidades se vendieron?:"))

if numero_ventas <= 100:
    print(f"El/La {articulo} es de baja necesidad")

elif numero_ventas > 100 and numero_ventas <= 500:
    print(f"El/La {articulo} es de media necesidad")

elif numero_ventas > 500 and numero_ventas <= 1000:
    print(f"El/La {articulo} es de alta necesidad")

elif numero_ventas > 1000:
    print(f"El/La {articulo} es de primera necesidad")

else:
    print("No existe ese artículo")

