from flask_app import app
from flask_app.controllers import peliculas, usuarios, comentarios

if __name__ == "__main__":
    app.run(debug=True, port=5000)
