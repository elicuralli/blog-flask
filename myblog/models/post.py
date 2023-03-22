from myblog import db
from datetime import datetime

class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    title = db.Column(db.String(50))
    body = db.Column(db.Text(50))
    created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) #esto es una libreria para generar fechas automaticas 



    def __init__(self, author,tittle,body) -> None:
        self.author = author
        self.body = body
        self.tittle = tittle
    
    def __repr__(self) -> str:
        return f'Post: {self.tittle}'


        