from flask import jsonify, request, send_file
from werkzeug.utils import secure_filename
from app import ALLOWED_EXTENSIONS, app, db
from flask_jwt_extended import create_access_token, get_jwt_identity
from models import File, User
from decorators import check_access


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')
    
    if not username or not email or not password or not role:
        return jsonify({"message": "Missing username, email, password, or role"}), 400
    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400
    
    new_user = User(username=username, email=email, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({"message": "Invalid username or password"}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify({"message": "Login Successful", "access_token": access_token}), 200


@app.route('/upload', methods=['POST'])
@check_access('CLIENT')
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No file selected for uploading"}), 400
    
    if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        filename = secure_filename(file.filename)
        db.session.add(File(filename=filename))
        db.session.commit()
        file.save(filename)
        return jsonify({"message": "File uploaded successfully"}), 201
    else:
        return jsonify({"message": "File type not allowed. Please upload pptx, docx, or xlsx files."}), 400

@app.route('/download/<filename>', methods=['GET'])
@check_access('CLIENT')
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/files', methods=['GET'])
def get_files():
    files = File.query.all()
    file_list = [{"filename": file.filename} for file in files]
    return jsonify(file_list)

# sample endpoints
# @app.route('/hello', methods=['GET'])
# def hello():
#     return jsonify({"message": "hello world"})

# @app.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     user_list = [{"username": user.username, "email": user.email, "password": user.password, "role": user.role} for user in users]
#     return jsonify(user_list)

# @app.route('/client', methods=['GET'])
# @check_access('CLIENT')
# def client():
#     return jsonify({"message": "Client User Access"})

# @app.route('/operation', methods=['GET'])
# @check_access('OPERATION')
# def operation():
#     return jsonify({"message": "Operation User Access"})