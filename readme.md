1) crear archivo Pipfile

2) $ pipenv shell
para crear el entorno virtual

3) instalar librerias

$ pipenv install flask
$ pipenv install flask-script
$ pipenv install flask-migrate
$ pipenv install flask-cors
$ pipenv install flask-sqlalchemy
$ pipenv install flask-bcrypt ( para encriptar la contraseña)
$ pipenv install flask-jwr-extended

4) crear app.py y models.py
    models.py = hace el modelo de la BBDD

5) en models.py importar SQL alchemy

6) crear carpeta template con un html dentro

7) en app.py importar libreriras de flask y de models el db

8) configurar la app basica con sqlite

9) $ python app.py runserver, arreglar errores q salgan y abrir local host 5000



