#EJERCICIO 1

#pido el nombre del cliente
nombre = input("Cliente: ").strip()

#valido que el nombre no este vacio y solo contenga letras
while nombre == "" or not nombre.isalpha():
    print("Error: ingresa un nombre no vacio y solo con letras")
    nombre = input("Cliente: ").strip()

#pido la cantidad de productos como string
cantidad_str = input("Ingresa la cantidad de productos: ").strip()

#valido que la cantidad sea un entero positivo
while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: ingresa un numero entero positivo mayor a cero")
    cantidad_str = input("Ingresa la cantidad de productos: ").strip

#convierto la cantidad a entero una vez validado
cantidad_int = int(cantidad_str)

#defino variables 
total_sin_descuento = 0
total_con_descuento = 0

#creo un bucle para recorrer los productos
for i in range(1,cantidad_int+1):
    #pido precio como string
    precio_str = input(f"Producto {i} - Precio: ").strip()

    #valido que el precio fuera un entero positivo
    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Error: el precio debe ser un entero positivo")
        precio_str = input(f"Producto {i} - Precio: ").strip()
    
    #convierto a int una vez validado
    precio_int = int(precio_str)

    #pregunto si aplica descuento
    desc = input("Descuento (S/N): ").strip().lower()

    #valido que solo ingreso s o n
    while desc != "s" and desc != "n":
        print("Error: Ingrese S para si o N para no")
        desc = input("Descuento (S/N): ").strip().lower()

    #sumatoria de los precios sin descuento
    total_sin_descuento += precio_int

    #si la respuesta es si aplico el 10% de descuento
    #sino dejo el precio original
    if desc == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int
    
    #hago la sumatoria de los precios con descuento si es que los tienen
    #sino la sumatoria es sin descuento
    total_con_descuento += precio_final


#calculo del ahorro
ahorro = total_sin_descuento - total_con_descuento

#calculo del promedio
promedio = total_con_descuento / cantidad_int

#impresion de los resultados
print()
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")


