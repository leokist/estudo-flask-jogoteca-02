
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

"""
DEFINIÇÃO DA APLICAÇÃO FLASK
"""
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views_games import *
from views_user import *


if __name__ == '__main__':
    app.run(debug=True)
# app.run(host='0.0.0.0', port=8080)
# definição manual de porta e host
# pode ser deixado em branco, o exemplo é para fins de desenvolvimento e não de produção

