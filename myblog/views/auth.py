from flask import render_template,Blueprint,flash,g,redirect, request,session,url_for
from myblog.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from myblog import db
import functools


auth = Blueprint('auth',__name__) #registrar vistas de la app 

#registrar un usuario

@auth.route('/register', methods= ('GET','POST')) 
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username, generate_password_hash(password))
        
        error = None
        if not username:
            error = 'se requiere nombre de usuario'
        elif not password:
            error = 'se requiere contraseña'
        
        user_name = User.query.filter_by(username =username).first()
        if user_name==None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error =f'el usuario {username} ya esta registrado'
            flash(error )
    return render_template('auth/register.html')


# inicio de sesion 

@auth.route('/login', methods= ('GET','POST')) 
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = None
        user = User.query.filter_by(username =username).first()

        if user == None:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.password, password): #aqui comparamos la clave que tiene  mi objeto usuario (user.password) con la clave que acaban de ingresar 
            error = 'contraseña incorrecta '

        if error is None:
            session.clear()
            session['user_id'] = user.id 
            return redirect(url_for('blog.index'))

        flash(error )
    return render_template('auth/login.html')


#verificar si un usuario inicio sesion o no 
@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

#cerrar sesion
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.index'))

# Se requiere haber iniciado sesion para ver algunas vistas
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view