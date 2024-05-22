from Crypto.Hash import SHA3_512
import config

def hash_check(start, end, result_queue, stop_event):
    with open(config.file_path, 'r', encoding='latin-1') as file:
        passwords = file.readlines()[start:end]

    salt_b = bytes.fromhex(config.salt)

    for index, password in enumerate(passwords):
        if stop_event.is_set():
            return
        password_bytes = bytes(password.strip(), 'utf-8')
        for pepper in range(256):
            H = SHA3_512.new()
            H.update(password_bytes)
            H.update(pepper.to_bytes(1, 'big'))
            H.update(salt_b)
            if H.hexdigest() == config.pwd:
                result_queue.put(f"Found: {password.strip()} at position {start+index} with pepper {pepper}")
                stop_event.set()  # Detener otros procesos una vez que se encuentra la contraseña
                return  # Salir de la función después de encontrar la contraseña
            else:
                print(f"position {start+index} Checked: {password.strip()} with pepper {pepper}")
    
    result_queue.put("Not found in the provided range.")
