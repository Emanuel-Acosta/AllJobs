from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.perfil import Perfil

@app.route('/perfil')  # 1. Ruta para ver el perfil del usuario
def ver_perfil():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión.", "danger")
        return redirect('/')
    
    perfil = Perfil.get_by_user_id(session['usuario_id'])
    return render_template("perfil.html", perfil=perfil)

@app.route('/perfil/editar', methods=['POST'])  # 2. Ruta para actualizar el perfil
def editar_perfil():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión.", "danger")
        return redirect('/')
    
    data = {
        'id_usuario': session['usuario_id'],
        'experiencia': request.form['experiencia'],
        'habilidades': request.form['habilidades'],
        'educacion': request.form['educacion'],
        'certificaciones': request.form['certificaciones']
    }

    Perfil.update(data)
    flash("Perfil actualizado correctamente.", "success")
    return redirect('/perfil')
