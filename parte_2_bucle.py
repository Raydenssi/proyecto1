from readchar import readkey, key

while True:
    print("Presiona UP para detener el programa.")
    tecla = readkey()
    if tecla == key.UP:
        break

print("Listo!")