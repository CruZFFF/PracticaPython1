# Abrir el archivo en modo lectura
devices=[]
file = open("devices.txt", "r")

# Imprimir cada línea del archivo
for item in file:
   item=item.strip()
   print(item.strip())  # strip() para quitar los saltos de línea extras
   devices.append(item)
# Cerrar el archivo
file.close()
print(devices)
