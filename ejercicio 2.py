#EJERCICIO 2

#Defino las credenciales iniciales (variables constantes) 
usuario_correcto = "alumno"
clave_correcta = "python123"

# Inicialización de variables de control
intentos = 0        # Contador para limitar el acceso a 3 veces
acceso = False      # Bandera  para saber si el login fue exitoso

# 2. Sistema de Login (Bucle con máximo 3 intentos)
while intentos < 3:
    intentos += 1   # Incrementamos el contador en cada vuelta
    print(f"Intento {intentos }/3")
    # Captura de datos del usuario
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    # Validación de credenciales
    if usuario == usuario_correcto and clave == clave_correcta:
        #si son correctas imprimo acceso concedido
        print("Acceso concedido.\n")
        acceso = True   # Cambiamos el estado a "permitido"
        break           # Salimos del bucle inmediatamente al acertar
    else:
        print("Error: credenciales inválidas.\n")
        

# Si la variable 'acceso' sigue siendo False tras agotar los intentos, 
# imprimo cuenta bloqueada.          
if not acceso:
    print("Cuenta bloqueada.")
else:
    #menu de acciones
    while True:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opcion: ")

        # Validación: .isdigit() comprueba que el texto sea un número entero
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue # Salta el resto del código y vuelve a pedir la opción

        # Convertimos el texto a número para poder comparar rangos
        opcion = int(opcion)

        # Validación: Comprobar que el número esté entre 1 y 4
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        # Lógica de las opciones del menú
        if opcion == 1:
            print("Estado: Inscripto")
        
        elif opcion == 2:
            # Bucle infinito que solo se rompe con una clave válida
            while True:
                nueva_clave = input("Nueva clave (mínimo 6 caracteres): ")
                
                # Validación de longitud
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres. Intente de nuevo.")
                    # No hay 'break', por lo que el while vuelve a pedir la clave
                else:
                    confirmacion = input("Confirme nueva clave: ")
                    
                    # Validación de coincidencia
                    if nueva_clave == confirmacion:
                        CLAVE_CORRECTA = nueva_clave
                        print("Clave cambiada con éxito.")
                        break  # <--- Rompe el while de la clave y vuelve al menú principal
                    else:
                        print("Error: las claves no coinciden. Recomience el proceso.")

        elif opcion == 3:
            print("Frase del dia: 'Abandonar no es una opcion.'")
        elif opcion == 4:
            print("Saliendo del sistema...") 
            break               