from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

#importar vistas 
from myblog.views.auth import auth
app.register_blueprint(auth) 

from myblog.views.blog import blog
app.register_blueprint(blog)
app.add_url_rule('/', endpoint='index')

with app.app_context():
    db.create_all()