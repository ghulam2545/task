from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ghulam@localhost/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super strong secret key'

jwt = JWTManager(app)
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)