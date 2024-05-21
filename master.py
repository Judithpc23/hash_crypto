import socket
import sys

# Función para enviar una tarea a un esclavo y recibir el resultado
def enviar_tarea(socket_esclavo, tarea):
    socket_esclavo.send(tarea.encode())
    resultado = socket_esclavo.recv(1024).decode()
    return resultado

# Configurar el socket del maestro
master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_socket.bind(('localhost', 5000))
master_socket.listen(5)

# Aceptar conexiones de los esclavos
print("Esperando conexiones de esclavos...")
esclavos = []
while len(esclavos) < 2:  # Esperar al menos 2 esclavos
    conn, _ = master_socket.accept()
    esclavos.append(conn)
    print(f"Esclavo conectado: {conn.getpeername()}")

# Enviar tareas a los esclavos y recibir resultados
tareas = ["tarea1", "tarea2", "tarea3"]
for esclavo, tarea in zip(esclavos, tareas):
    resultado = enviar_tarea(esclavo, tarea)
    print(f"Resultado de {tarea}: {resultado}")

# Cerrar conexiones
for esclavo in esclavos:
    esclavo.close()
master_socket.close()