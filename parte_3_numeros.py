import os
import readchar

def borrar_e_imprimir(contador):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(contador)

contador = 0

while contador < 50:
    print("Presiona la letra 'N'.")
    tecla = readchar.readchar()
    if tecla.lower() == 'n':
        contador += 1
        borrar_e_imprimir(contador)

print("Completado.")