#EJERCICIO 3

#Definición de variables individuales con espacios vacíos ""
lun1 = ""; lun2 = ""; lun3 = ""; lun4 = ""
mar1 = ""; mar2 = ""; mar3 = ""

#pido el nombre del operador
operador = input("Ingrese el nombre del operador: ").strip()

#Pedir nombre del operador (solo letras)
while  not operador.isalpha():
    operador = input("Error: ingresa un nombre no vacio y solo con letras:").strip()

#Menu repetitivo    
while True:
    print("1. Reservar | 2. Cancelar | 3. Ver Agenda | 4. Resumen | 5. Salir")
    opcion = input("Selecciona una opcion: ")

    if not opcion.isdigit():
        print("Error: ingrese un numero valido.")
        continue
        
    opcion = int(opcion)

    #opcion reservar
    if opcion == 1:
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente: ")

        #verifico que solo tenga letras
        if not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            continue
        
        #opcion dia lunes
        if dia == "1":
            #Verifico si ya está repetido en Lunes
            if paciente == lun1 or paciente == lun2 or paciente == lun3 or paciente == lun4:
                print("Error: El paciente ya tiene turno el lunes.")
            #guardo en el primer espacio libre
            elif lun1 == "":
                lun1 = paciente
                print("Reservado en turno 1 (Lunes)")
            elif lun2 == "":
                lun2 = paciente
                print("Reservado en turno 2 (Lunes)")
            elif lun3 == "":
                lun3 = paciente
                print("Reservado en turno 3 (Lunes)")
            elif lun4 == "":
                lun4 = paciente
                print("Reservado en turno 4 (Lunes)")
            else:
                print("Sin cupos para el lunes.")
        
        #opcion dia martes
        elif dia == "2":
            #verifico si ya esta repetido el martes
            if paciente == mar1 or paciente == mar2 or paciente == mar3:
                print("Error: El paciente ya tiene turno el martes.")
            elif mar1 == "":
                mar1 = paciente
                print("Reservado en turno 1 (Martes)")
            elif mar2 == "":
                mar2 = paciente
                print("Reservado en turno 2 (Martes)")
            elif mar3 == "":
                mar3 = paciente
                print("Reservado en turno 3 (Martes)")    
            else:
                print("Sin cupos para el Martes.")
    
    #opcion cancelar
    elif opcion == 2:
        dia = input("Elegir dia (1=lunes, 2=martes): ")
        paciente = input("Nombre del paciente a cancelar: ")

        if dia == "1":
            if paciente == lun1:
                lun1 = ""
                print("Turno 1 cancelado.")
            elif paciente == lun2:
                lun2 = ""
                print("Turno 2 cancelado")
            elif paciente == lun3:
                lun3 = ""
                print("Turno 3 cancelado")
            elif paciente == lun4:
                lun4 = ""
                print("Turno 4 cancelado")
            else:
                print("Paciente no encontrado.")

    #ver agenda del dia
    elif opcion == 3:
        dia = input("Ver dia (1=lunes, 2=martes): ")
        #dia lunes
        if dia == "1":
            #turno 1
            if lun1 != "":
                print("Turno 1:", lun1)
            else:
                print("Turno 1: (libre)")
            #turno 2
            if lun2 != "":
                print("Turno 2:", lun2)
            else:
                print("Turno 2: (libre)")
            #turno 3
            if lun3 != "":
                print("Turno 3:", lun3)
            else:
                print("Turno 3: (libre)")
            #turno 4
            if lun4 != "":
                print("Turno 4:", lun4)
            else:
                print("Turno 4: (libre)")
        #dia martes
        elif dia == "2":
            #turno 1
            if mar1 != "":
                print("Turno 1:", mar1)
            else:
                print("Turno 1: (libre)")
            #turno 2
            if mar2 != "":
                print("Turno 2:", mar2)
            else:
                print("Turno 2: (libre)")
            #turno 3
            if mar3 != "":
                print("Turno 3:", mar3)
            else:
                print("Turno 3: (libre)")

    #Resumen general
    elif opcion == 4:
        #cuento los ocupado de lunes
        ocu_l = 0

        if lun1 != "":
            ocu_l += 1
        if lun2 != "":
            ocu_l += 1
        if lun3 != "":
            ocu_l += 1
        if lun4 != "":
            ocu_l += 1
        
        #cuento los ocupados de martes
        ocu_m = 0

        if mar1 != "":
            ocu_l += 1
        if mar2 != "":
            ocu_l += 1
        if mar3 != "":
            ocu_l += 1
        
        print(f"Lunes: {ocu_l} ocupados / {4 - ocu_l} disponibles")
        print(f"Martes: {ocu_m} ocupados / {3 - ocu_m} disponibles")

        if ocu_l > ocu_m:
            print("El lunes tiene mas turnos ocupados.")
        elif ocu_m > ocu_l:
            print("El martes tiene mas turnos ocupados.")
        else:
            print("Empate: ambos dias tienen las misma ocupacion.")
    
    #Cerrar el sistema
    elif opcion == 5:
        print("Cerrando agenda...")
        break