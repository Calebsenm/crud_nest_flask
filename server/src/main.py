from flask_cors import CORS
from src.db.database import get_connection
from src.routes.empresas import empresas
from flask import Flask

app = Flask(__name__)
CORS(app)
app.register_blueprint(empresas)

# Rutas de al api 

@app.route("/")
def home():
    return {"message": "API Flask funcionando"}


if __name__ == "__main__":
    app.run(debug=True)
