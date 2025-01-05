from config import db
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)  
    password_hash = db.Column(db.String(128), nullable=False)  
    gender = db.Column(db.String(10))


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Tasks(db.Model):
    __tablename__ = "tasks"
    task_id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(100), nullable=False)
    task_description = db.Column(db.String(255), nullable=True)  
    task_status = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {
            "id": self.task_id,
            "task_title": self.task_title,
            "task_description": self.task_description,
            "task_status": self.task_status
        }
