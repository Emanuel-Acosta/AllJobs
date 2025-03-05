from flask import request, redirect, session, flash
from flask_app import app
from flask_app.models.favorito import Favorito

@app.route('/favoritos')  # 1. Ruta para ver ofertas guardadas
def ver_favoritos():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión.", "danger")
        return redirect('/')
    
    favoritos = Favorito.get_by_user_id(session['usuario_id'])
    return render_template("favoritos.html", favoritos=favoritos)

@app.route('/favoritos/agregar/<int:id_oferta>')  # 2. Ruta para agregar una oferta a favoritos
def agregar_favorito(id_oferta):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión.", "danger")
        return redirect('/')
    
    data = {
        'id_usuario': session['usuario_id'],
        'id_oferta': id_oferta
    }
    
    Favorito.save(data)
    flash("Oferta guardada en favoritos.", "success")
    return redirect('/empleos')

@app.route('/favoritos/eliminar/<int:id_favorito>')  # 3. Ruta para eliminar un favorito
def eliminar_favorito(id_favorito):
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión.", "danger")
        return redirect('/')
    
    Favorito.delete(id_favorito)
    flash("Oferta eliminada de favoritos.", "success")
    return redirect('/favoritos')
