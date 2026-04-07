# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
# Contador para la regla anti-spam
forzar_seguidos = 0  

# Validación del nombre del agente
nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del agente (solo letras): ")
    if not nombre.isalpha():
        print("Error: El nombre debe contener solo letras.")

print(f"\n--- BIENVENIDO AGENTE {nombre.upper()} ---")

# Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO POR ALARMA! La bóveda se selló permanentemente.")
        break

    # Mostrar estado actual
    print(f"\nESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'⚠️ ACTIVADA' if alarma else 'OK'} | Código: [{codigo_parcial}]")

    print("\n1. Forzar cerradura (-20E, -2T)")
    print("2. Hackear panel (-10E, -3T)")
    print("3. Descansar (+15E, -1T)")
    
    opcion = input("Elija una acción: ")
    while not opcion.isdigit():
        opcion = input("Error: Ingrese un número válido (1-3): ")
    
    opcion = int(opcion)

    if opcion == 1:
        # Costo base
        energia -= 20
        tiempo -= 2
        forzar_seguidos += 1

        # Regla Anti-Spam
        if forzar_seguidos == 3:
            print("¡LA CERRADURA SE TRABÓ! Has forzado demasiado seguido.")
            alarma = True
        else:
            # Riesgo de alarma por baja energía
            if energia < 40:
                print("RIESGO DE ALARMA: Energía baja, tus manos tiemblan.")
                n_riesgo = input("Elija un número de seguridad (1, 2 o 3): ")
                while not n_riesgo.isdigit() or n_riesgo not in ["1", "2", "3"]:
                    n_riesgo = input("Error: Elija 1, 2 o 3: ")
                
                if n_riesgo == "3":
                    alarma = True
                    print("¡Activaste los sensores térmicos!")

            # Si no saltó la alarma por ninguna razón, abre cerradura
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con éxito!")

    elif opcion == 2:
        # Corta la racha
        forzar_seguidos = 0 
        energia -= 10
        tiempo -= 3
        
        print("Hackeando...")
        for i in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {i}/4 - Progreso: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            # Se resetea el código al abrir una
            codigo_parcial = "" 
            print("¡Hackeo exitoso! Una cerradura se desbloqueó.")

    elif opcion == 3:
        # Corta la racha
        forzar_seguidos = 0 
        recuperacion = 15
        if alarma:
            # Penalización por alarma activa
            recuperacion -= 10 
            print("El ruido de la alarma no te deja descansar bien...")
        
        energia += recuperacion
        # Límite máximo
        if energia > 100: energia = 100 
        tiempo -= 1
        print(f"Descanso finalizado. Energía actual: {energia}")

    else:
        print("Opción no válida.")

# Condiciones de fin de juego
print("\n--- RESULTADO FINAL ---")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El agente {nombre} ha abierto la bóveda.")
elif energia <= 0:
    print("DERROTA: Te quedaste sin energía y te desmayaste.")
elif tiempo <= 0:
    print("DERROTA: Se acabó el tiempo, la policía llegó.")
else:
    print("JUEGO TERMINADO.")

