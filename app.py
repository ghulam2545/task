from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeSerializer

app = Flask(__name__)
app.app_context().push()

ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}
SECRET_STRING = 'super strong secret string'
DATABASE_URL = 'mysql+pymysql://root:ghulam@localhost/app'
# UPLOAD_FOLDER = 'static'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = SECRET_STRING

serializer = URLSafeSerializer(SECRET_STRING)

jwt = JWTManager(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from routes import *

if __name__ == '__main__':
    app.run(debug=True)