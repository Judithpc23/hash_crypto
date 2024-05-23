import multiprocessing
import config
from worker import hash_check

def main():
    line_count = 14344392  # Número total de líneas en el archivo
    chunk_size = line_count // config.num_workers  # Tamaño de cada segmento de líneas que cada proceso manejará

    # Cola para almacenar los resultados de los procesos
    result_queue = multiprocessing.Queue()
    
    # Evento para indicar a los procesos que deben detenerse.
    stop_event = multiprocessing.Event()
    
    # Lista para almacenar los procesos
    processes = []  

    # Crear y comenzar los procesos
    for i in range(config.num_workers):
        
        start = i * chunk_size  # Línea de inicio del segmento
        
        # Calcula la línea final del segmento que este proceso manejará
        # Para todos los procesos excepto el último, `end` se establece como `start + chunk_size` para que cada proceso maneje exactamente `chunk_size` líneas
        # Para el último proceso, `end` se establece como `line_count` para que maneje todas las líneas restantes
        
        if i < config.num_workers - 1:
            end = start + chunk_size
        else:
            end = line_count
        
        #end = start + chunk_size if i < config.num_workers - 1 else line_count ----> Otra forma de hacerlo
        
        # <<<<<<<<<<<<<<<<<<<<<<< Crear y comenzar los procesos >>>>>>>>>>>>>>>>>>>>>>>>
        # Crear el proceso y asignarle la función `hash_check` con sus argumentos
        # `target=hash_check` especifica que la función a ejecutar en el nuevo proceso es `hash_check`
        # `args=(start, end, result_queue, stop_event)` proporciona los argumentos necesarios para la función `hash_check`:
        # - `start`: la línea inicial del archivo que este proceso debe leer
        # - `end`: la línea final del archivo que este proceso debe leer
        # - `result_queue`: una cola de resultados compartida entre los procesos para almacenar y comunicar los resultados
        # - `stop_event`: un evento que puede ser activado para detener todos los procesos una vez que se encuentra la contraseña
        
        p = multiprocessing.Process(target=hash_check, args=(start, end, result_queue, stop_event))
        
        # Agregar el proceso a la lista de procesos
        processes.append(p) 
        
        # Iniciar el proceso
        p.start()

    # Esperar a que todos los procesos terminen
    for p in processes:
        p.join()

    # Imprimir los resultados almacenados en la cola
    while not result_queue.empty():
        print(result_queue.get())

# Punto de entrada del script
if __name__ == '__main__':
    user = str(input('Ingrese el nombre de usuario: '))
    if config.search_user(user) == []:
        print('Usuario no encontrado')
    else:
        config.username, config.salt, config.pwd = config.search_user(user)
        print(f'Looking for password for user {config.username}.')
        print('Please wait a few minutes. This may take.')
        main()