import pandas as pd

#Ruta de los datos de usuarios
path = 'password_database_ED2.xlsx'

#Carga de los datos
data = pd.read_excel(path)

#Función para buscar y capturar los datos
def search_user(username:str, data:'pd.DataFrame' = data):
    list_data = data.loc[data['username'] == username]
    if list_data.empty:
        return []
    return list_data.iloc[0].tolist()

# Configuración de parámetros para la búsqueda de cada usuario.

# >>>>>>>>>>>>> Configuración de parámetros para la búsqueda de cada usuario. <<<<<<<<<<<<
# username, salt, pwd = ['jiconde', '8c04e4fca93b3eaea67ad9b7f2d58b53', '4ad1d7ac653be946ae01187622122a775b478d1f1163fe9e14247d1f6a7e4478cb4a5d5aa04d1fcbb906c2d97994b7ad62a1a65fb347403913c2c23ea5356173']
# username, salt, pwd = ['arangocarlos','79bd2c548d47b262ed374b69f10b43dc','8a14f955bb10cf2a82935e3b82d487e0b545c02c4bc2911d9d906f350bf4866688706654a83d88725ae1354b866f326281f067544b87a0131a02062057221a72']
# username, salt, pwd = ['edadul','465589f0b3c7c73cab54ada02c1c9589','9181591f2dc3a4ab5c547a8b0380c3c158ce116c735db8e33dca4fb22df117834812514fad6412091e88d933712b99231026648de1fdc953e3a7275637329576']
# username, salt, pwd = ['adballesteros', 'afac6ca30d8850e9477f47c4b7bc822b', 'ac24caa8b39b7c4f521ce057f4f7e04dce7c2bea3a80ebcf642ce836db6ef743c4316401aa3f9762e6bc92b9af26908b30308b4af80231934494582562b0aa00']


#Usuario buscado
username = ''
# Salt utilizada para fortalecer la contraseña antes de hashearla
salt = ''
# Hash objetivo de la contraseña que se busca en el archivo
pwd = ''

# Ruta del archivo de contraseñas a ser analizado.
file_path = "rockyou.txt"

# Número de procesos que se utilizarán para realizar la búsqueda en paralelo
num_workers = 10