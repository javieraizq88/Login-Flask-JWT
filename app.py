from flask import Flask, jsonify, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from models import db, User

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["ENV"] = "development"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

db.init_app(app)#une la BBDD con la app
Migrate(app, db)
bcrypt = Bcrypt(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

CORS(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/register", methods=["POST"])# debe ser POST pq voy a mandar info en el body del mensaje a la API
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON request"}), 400# valido q se esta mandando la info


    username = request.json.get("username", None)# le doy un valor por defecto en caso q no venga la variable
    password = request.json.get("password", None)# le doy un valor por defecto en caso q no venga la variable
    name = request.json.get("name", " ")# valor opcional
    lastname = request.json.get("lastname", " ")# valor opcional

    # VALIDACION DEL USERNAME Y PASSWORD Q SON OBLIGATORIOS
    if not username or username == "":
        return jsonify({"msg": "Missing username request"}), 400
    if not password or password == "":
        return jsonify({"msg": "Missing passwword request"}), 400

    #CREACION DE USUARIO
    user = User.query.filter_by(username=username).first()# confirma q el usuario sea unico o si ya existe
    if user:
        return jsonify({"msg" : "Username all ready exist"}), 400# el usuario ya existe

    user = User()
    user.username = username
    user.password = bcrypt.generate_password_hash(password)# genera un TOKEN de la contraseña del usuario para no guardarla textual en la BD
    user.name = name
    user.lastname = lastname

    db.session.add(user)
    db.session.commit()# crea un registro del usuario en la BBDD

    access_token = create_access_token(identity=user.username)# crea un access token y devuelvo un objeto con la info del usuario (username, name y lastname)
    data = {
        "access_token": access_token,
        "user": user.serialize()
    }

    return jsonify(data), 201# dice q hizo un registro exitoso


if __name__ == "__main__":
    manager.run()

