from flask import render_template, Blueprint,flash,g,redirect,request,url_for
from werkzeug.exceptions import abort
from myblog.models.user import User
from myblog.models.post import Post
from myblog.views.auth import login_required
from myblog import db
import time

blog = Blueprint('blog', __name__)

#obtener usuario

def get_user(id):
    user = User.query.get_or_404(id)
    return user

@blog.route('/index' )
def index():
    posts = Post.query.all()
    db.session.commit()
    return render_template('blog/index.html', posts = posts)

#registrar un post
@blog.route('/blog/create', methods = ('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        post = Post(g.user.id,title,body)     

        error = None
        if not title:
            error = 'se requiere un titulo para este post'
        
        if error is not None:
            flash(error)
        
        else:
            
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        
        flash(error )
    return render_template('blog/create.html')