#Configuración del Personaje 
nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

#Inicialización de Estadísticas 
vida_gladiador = 100        
vida_enemigo = 100           
pociones = 3                 
ataque_pesado_base = 15      
ataque_enemigo = 12         
juego_activo = True          

print("\n=== INICIO DEL COMBATE ===")

# El Ciclo de Combate
while vida_gladiador > 0 and vida_enemigo > 0:
    # Mostrar estado actual
    print(f"\n{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    # Validación del Menú
    opcion = ""
    while True:
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            if opcion in ["1", "2", "3"]:
                break
            else:
                print("Error: Elija 1, 2 o 3.")
    
    opcion = int(opcion)

    # Lógica de las Acciones del Jugador
    if opcion == 1: 
        # Ataque Pesado
        daño_final = float(ataque_pesado_base)
        if vida_enemigo < 20:
            # Golpe Crítico (float)
            daño_final = ataque_pesado_base * 1.5 
            print("¡GOLPE CRÍTICO!")
        
        vida_enemigo -= int(daño_final)
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")

    # Ráfaga Veloz
    elif opcion == 2: 
        print(">> ¡Inicias una ráfaga de golpes!")
        # Bucle for de 3 repeticiones
        for i in range(3): 
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # Curar
    elif opcion == 3: 
        if pociones > 0:
            vida_gladiador += 30
            # No exceder máximo
            if vida_gladiador > 100: vida_gladiador = 100 
            pociones -= 1
            print(f"Te has curado. Vida actual: {vida_gladiador}")
        else:
            print("¡No quedan pociones! Pierdes el turno intentando buscar una.")

    # Turno del Enemigo (Solo si sigue vivo tras el ataque del jugador)
    if vida_enemigo > 0:
        vida_gladiador -= ataque_enemigo
        print(f">> ¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")
    
    print("=== NUEVO TURNO ===")

# Fin del Juego 
print("\n--- RESULTADO FINAL ---")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
