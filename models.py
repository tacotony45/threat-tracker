from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    ip_address = db.Column(db.String(50))
    timestamp = db.Column(db.String(100))
    status_code = db.Column(db.String(10))

    def __repr__(self):
        return f'<Log {self.id}>'
