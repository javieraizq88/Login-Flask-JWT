1) crear archivo Pipfile

2) para crear el entorno virtual
    $ pipenv shell
    $ python app.py runserver

3) instalar librerias
    $ pipenv install flask
    $ pipenv install flask-script
    $ pipenv install flask-migrate
    $ pipenv install flask-cors
    $ pipenv install flask-sqlalchemy
    $ pipenv install flask-bcrypt ( para encriptar la contraseña)
    $ pipenv install flask-jwt-extended

4) crear app.py y models.py
    models.py = hace el modelo de la BBDD

5) en models.py importar SQL alchemy

6) crear carpeta template con un html dentro

7) en app.py importar libreriras de flask y de models el db

8) configurar la app basica con sqlite

9) $ python app.py runserver, arreglar errores q salgan y abrir local host 5000

10) se va a usar 
    - JWT Manager = para vincular mi app con JWT 
    - jwt-required = directiva para decir q ruta es privada o no
    - create_access_token = fx q crea el token para identificar a cada usuario
    - get_jwt_identity = identifica el usuario q esta logeado 

11) iniciar migraciones
    $ python app.py db init
    $ python app.py db migrate
    $ python app.py db upgrade

12) crear la ruta para el proceso de registro

13) validación de username y password q son obligatorios

14) creacion de usuario creando una instancia en la BBDD

15) usar bcript para no guardar la clave como la manda el usuario 

16) crear q el usuario sea unico o si ya existe

17) crear el token con JWT_SECRET_KEY y create_access_token

18) probar en insmonmia si esta ok el registro