from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.oferta import Oferta

@app.route('/empleos')  # 1. Ruta para ver todas las ofertas de trabajo
def listar_empleos():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión.", "danger")
        return redirect('/')
    
    ofertas = Oferta.get_all()
    return render_template("empleos.html", ofertas=ofertas)

@app.route('/empleos/<int:id_oferta>')  # 2. Ruta para ver el detalle de una oferta
def ver_empleo(id_oferta):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión.", "danger")
        return redirect('/')
    
    oferta = Oferta.get_by_id(id_oferta)
    return render_template("detalle_empleo.html", oferta=oferta)
