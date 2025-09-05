from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Contacto

contacto_bp = Blueprint('contactos', __name__)

@contacto_bp.route('/')
def listar_contactos():
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)

@contacto_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        correo = request.form['correo']
        nuevo = Contacto(nombre=nombre, telefono=telefono, correo=correo)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('contactos.listar_contactos'))
    return render_template('form.html')