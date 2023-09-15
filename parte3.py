import os
import readchar 

def quitar_enseñar_numero(i):
    os.system('cls' if os.name == 'nt' else 'clear')
    if i==50:
         print("Fin del programa")
    else:
         print(f"numero: {i}")
i= 0
while i <= 50:

    key = readchar.readkey()
    print (key)
    if key == 'n':
    
        quitar_enseñar_numero(i)
        i += 1
