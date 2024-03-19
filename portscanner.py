import socket
import sys
import time

ip = input("Ingrese la dirección IP a escanear: ")

#animacion de puntos suspensivos

print("Escaneando puertos en progreso", end='', flush=True)#end para que se escriba en la misma linea
#flush true para que la salida sea inmediata


for _ in range(10):  # 10 puntos suspensivos
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(0.5)  # Espera de 0.5 segundos entre cada punto
    
print("\n")

print("Espere un momento")

print("\n")

for puerto in range(1, 65535):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print(f"Puerto Abierto: {puerto}")
        sock.close()
        break  # Detiene el escaneo cuando se encuentra un puerto abierto

    else:
        sock.close()
