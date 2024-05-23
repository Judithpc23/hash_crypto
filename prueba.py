import hashlib

def generate_deterministic_salt(password, salt_length=16):
    # Genera una salt determinista basada en la contraseña
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha3_512(password_bytes).digest()
    return hash_object[:salt_length]

def hash_password(password, salt):
    # Convierte la contraseña y la salt a bytes y las combina
    password_bytes = password.encode('utf-8')
    salted_password = salt + password_bytes
    
    # Genera el hash usando SHA-3-512
    hash_object = hashlib.sha3_512(salted_password)
    return hash_object.hexdigest()

# Contraseña
password = "iloveu"

# Generar una salt determinista
salt = generate_deterministic_salt(password)

# Generar hash con la salt y la contraseña
hashed_password = hash_password(password, salt)

print(f"Salt (hex): {salt.hex()}")
print(f"Hashed Password: {hashed_password}")

# from Crypto.Hash import SHA3_512

# #Salt (hex): 274d2761ec78634f31d80760737cfb0b
# #Hashed Password: 3f342e41ca113f594db04e30b8fcc6536f2738a9d1ffb02f92bbeb7a6c2e8fa72ded07fe644b9860772ba85f1c587230a2a40b4c42940d5b1b0ed531e3d6f738

# username, salt, pwd = ['jiconde', '8c04e4fca93b3eaea67ad9b7f2d58b53','4ad1d7ac653be946ae01187622122a775b478d1f1163fe9e14247d1f6a7e4478cb4a5d5aa04d1fcbb906c2d97994b7ad62a1a65fb347403913c2c23ea5356173']
# #username, salt, pwd = ('edadul', '465589f0b3c7c73cab54ada02c1c9589', '9181591f2dc3a4ab5c547a8b0380c3c158ce116c735db8e33dca4fb22df117834812514fad6412091e88d933712b99231026648de1fdc953e3a7275637329576')
# #salt, pwd = ('274d2761ec78634f31d80760737cfb0b','3f342e41ca113f594db04e30b8fcc6536f2738a9d1ffb02f92bbeb7a6c2e8fa72ded07fe644b9860772ba85f1c587230a2a40b4c42940d5b1b0ed531e3d6f738')


# with open("rockyou.txt", encoding='latin-1') as archivo:
#    passwords = archivo.readlines()

# passwords = passwords[1949000:]
# sumar = 1949000
# # passwords_1 = passwords[(sumar + 4781465):5976829]
# # passwords_2 = passwords[(sumar + 5976829):7172194]
# # passwords_3 = passwords[(sumar +7172194):8367559]
# # passwords_4 = passwords[(sumar + 8367559):9562928]

# cont_pepper = 1
# cont_password = 1
# cont = sumar
# flag = False

# for pos_passwords in passwords:
    
#     cont += 1
    
#     if flag == True:
#         break
#     else:   
#         print(cont_pepper,' / ', cont_password,' / ',cont,' / ', pos_passwords)
        
#     for pepper in range(256):
#         H = SHA3_512.new()
        
#         password_b = bytes(pos_passwords, 'utf-8')
#         H.update(password_b)
        
#         pepper_b = pepper.to_bytes(1, 'big')
#         H.update(pepper_b)
        
#         salt_b = bytes.fromhex(salt)
#         H.update(salt_b)
        
#         pwd_h = H.hexdigest()
        
#         #print(cont_pepper,' / ', cont_password,' / ',cont,' / ', pos_passwords)
        
#         if pwd_h == pwd:
#             print(cont, ': ',pos_passwords, '<------ Fue encontrada -------->')
#             print('Hash: ', pwd_h)
#             print('Pepper: ', pepper)
#             print('Pepper(bytes): ', pepper_b)
#             print('Password: ', pos_passwords)
#             print('Salt: ', salt)
#             print ('<------ Fue encontrada -------->')
#             flag = True
#         else:
#             if cont_pepper <= 256:
#                 cont_pepper += 1
#             else:
#                 cont_pepper = 0
#                 cont_password += 1

from Crypto.Hash import SHA3_512

# Datos del usuario
#username, salt, pwd = ['jiconde', '8c04e4fca93b3eaea67ad9b7f2d58b53', '4ad1d7ac653be946ae01187622122a775b478d1f1163fe9e14247d1f6a7e4478cb4a5d5aa04d1fcbb906c2d97994b7ad62a1a65fb347403913c2c23ea5356173']
#username, salt, pwd = ['arangocarlos','79bd2c548d47b262ed374b69f10b43dc','8a14f955bb10cf2a82935e3b82d487e0b545c02c4bc2911d9d906f350bf4866688706654a83d88725ae1354b866f326281f067544b87a0131a02062057221a72']
#username, salt, pwd = ['edadul','465589f0b3c7c73cab54ada02c1c9589','9181591f2dc3a4ab5c547a8b0380c3c158ce116c735db8e33dca4fb22df117834812514fad6412091e88d933712b99231026648de1fdc953e3a7275637329576']
username, salt, pwd = ['adballesteros',	'afac6ca30d8850e9477f47c4b7bc822b',	'ac24caa8b39b7c4f521ce057f4f7e04dce7c2bea3a80ebcf642ce836db6ef743c4316401aa3f9762e6bc92b9af26908b30308b4af80231934494582562b0aa00']

# Leer contraseñas desde el archivo
with open("rockyou.txt", encoding='latin-1') as archivo:
    passwords = archivo.readlines()

# Comenzar desde una posición específica
start_position = 9546000
passwords = passwords[start_position:]

# Bandera para detener el bucle cuando se encuentre la contraseña
flag = False

# Procesar cada contraseña
for index, pos_password in enumerate(passwords, start=start_position + 1):
    if flag:
        break

    pos_password = pos_password.strip()  # Quitar espacios en blanco
    print(f"{index}")

    for pepper in range(256):
        H = SHA3_512.new()
        
        password_b = bytes(pos_password, 'utf-8')
        H.update(password_b)
        
        pepper_b = pepper.to_bytes(1, 'big')
        H.update(pepper_b)
        
        salt_b = bytes.fromhex(salt)
        H.update(salt_b)
        
        pwd_h = H.hexdigest()
        
        if pwd_h == pwd:
            print('<------ Fue encontrada -------->')
            print(f"{index}: {pos_password}")
            print(f"Hash: {pwd_h}")
            print(f"Pepper: {pepper}")
            print(f"Pepper(bytes): {pepper_b}")
            print(f"Password: {pos_password}")
            print(f"Salt: {salt}")
            print('<------ Fue encontrada -------->')
            flag = True
            break