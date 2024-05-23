from Crypto.Hash import SHA3_512  # Importa la función de hash SHA3-512 de la biblioteca PyCryptodome

# <<<<<<<<<<<<<<<<<<<<<<< Importar desde el archivo `config.py` los datos a procesar >>>>>>>>>>>>>>>>>>>>>>>>
import config  # Importa configuraciones específicas desde el archivo `config`

# Define la función `hash_check` que será ejecutada por cada proceso
def hash_check(start, end, result_queue, stop_event):
    
    # Abre el archivo de contraseñas en modo lectura con codificación 'latin-1' (Por tener caracteres especiales)
    with open(config.file_path, 'r', encoding='latin-1') as file:
        # Lee las líneas del archivo en el rango especificado (de start a end)
        passwords = file.readlines()[start:end]

    # Convierte la sal (salt) de formato hexadecimal a bytes
    salt_b = bytes.fromhex(config.salt)

    # Itera sobre las contraseñas leídas del archivo
    for index, password in enumerate(passwords):
        # Verifica si se ha activado el evento de parada (stop_event), en cuyo caso se detiene.
        if stop_event.is_set():
            return  # Salir de la función si el evento de parada está activado.

        # Convierte la contraseña actual a bytes, eliminando cualquier espacio en blanco
        password_bytes = bytes(password.strip(), 'utf-8')

        # Prueba cada valor posible de pepper (0 a 255)
        for pepper in range(256):
            # Crea un nuevo objeto de hash SHA3-512
            H = SHA3_512.new()
            # Actualiza el objeto de hash con la contraseña en bytes
            H.update(password_bytes)
            # Añade el pepper convertido a bytes al hash
            H.update(pepper.to_bytes(1, 'big'))
            # Añade la sal al hash
            H.update(salt_b)

            # Comprueba si el hash resultante coincide con el hash objetivo
            if H.hexdigest() == config.pwd:
                # Si coincide, coloca un mensaje en la cola de resultados indicando que se encontró la contraseña
                result_queue.put(f"Found: {password.strip()} at position {start+index+1} with pepper {pepper+1}")
                # Activa el evento de parada para detener otros procesos
                stop_event.set()
                # Salir de la función después de encontrar la contraseña
                return
            else:
                pass
                # # Si no coincide, imprime un mensaje indicando que la contraseña con el pepper actual ha sido verificada
                #print(f"Position: {start+index}")

    # Si no se encuentra la contraseña en el rango dado, coloca un mensaje en la cola de resultados
    result_queue.put("Not found in the provided range.")
