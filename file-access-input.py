# Abrir el archivo en modo "a" (append - agregar)
file = open("devices.txt", "a")

# Iniciar bucle para pedir nuevos dispositivos
while True:
    newitem = input("Enter device name: ")

    if newitem.lower() == "exit":
        print("¡Todo hecho!")
        break

    # Escribir el nuevo dispositivo en el archivo
    file.write(newitem + "\n")

# Cerrar el archivo al finalizar
file.close()
