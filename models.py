from app import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    verfied = db.Column(db.Boolean, default=True) # adjust this default

    def __repr__(self):
        return f'<User {self.username}>'

    def get_role(self):
        return self.role

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<File {self.filename}>'
    

# user1 = User(username='shafi', email='shafi@gmail.com', password=bcrypt.generate_password_hash('shafi'), role='CLIENT')
# user2 = User(username='ghulam', email='ghulam@gmail.com', password=bcrypt.generate_password_hash('ghulam'), role='OPERATION')

# db.create_all()
# db.session.add(user1)
# db.session.add(user2)
# db.session.commit()