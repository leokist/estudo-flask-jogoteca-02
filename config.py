import random
import os

"""
CONFIGURAÇÕES DA APLICAÇÃO
"""

def secret_key():
    """Cria a chave secreta para a session"""
    lista_parte_chave=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z']
    lista_parte_chave2=['!','@','#','$','%','&','*','?']
    a = random.choice(lista_parte_chave)
    b = random.randint(1000000000, 9000000000)
    c = random.choice(lista_parte_chave)
    d = random.choice(lista_parte_chave2)
    key = str(a) + str(d) + str(b) + str(c)
    return key

SECRET_KEY = secret_key()

# configuração do SQLAlchemy
SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca',
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
