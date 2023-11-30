# Entorno de desarrollo

## Requisitos
- Ubuntu==20.04
- Python==3.8
- virtualenvwrapper==4.8.4
- postgreSQL==12.8
- pgAdmin4==6.0
- Git


### Python en Ubuntu 20.04
- Comprobar que python está instalado:
    
    `$ python --version`

    `$ python3 --version`

- Si python no está instalado o su versión es menor a la 3.8, continuar con los pasos siguientes. Actualizar paquetes de Ubuntu:
    
    `$ sudo apt update`

    `$ sudo apt upgrade`

- Instalar software-properties-common. Ofrece mejor control sobre el manejo de paquetes y permite agregar repositorios:

    `$ sudo apt install software-properties-common`

- Deadsnakes es un PPA (Personal Package Manager) que contiene las versiones mas recientes de python para Ubuntu:

    `$ sudo add-apt-repository ppa:deadsnakes/ppa`

- Actualizar la lista de paquetes nuevamente:

    `$ sudo apt update`

- Ahora puede iniciar la instalación de Python 3.8 con el comando:

    `$ sudo apt sudo apt install python3.8`

- Comprobar que se instaló la versión correcta de Python:

    `$ python3 --version`

- Para acceder a la consola de Python ingrese: 
    `$ python3`
---
### Pip en ubuntu

- Pip es el instalador de paquetes de Python. Instalar pip desde los repositorios de Ubuntu:

    `$ sudo apt update`

    `$ sudo apt install python3-pip`

Documentación: https://pip.pypa.io/en/stable/

---
### Virtualenvwrapper
- Virtualenvwrapper es un conjunto de extensiones para virtualenv que hace que sea mucho más fácil administrar entornos virtuales de Python. Para instalarlo debe ejecutar:

    `$ pip install virtualenvwrapper`

- Para poder utilizar entornos virtuales con Virtualenvwrapper se deben agregar algunas variables de entorno y comandos al archivo `~/.bashrc`

    ```
        # Virtualenvwrapper
        export WORKON_HOME=~/envs
        export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
        export VIRTUALENVWRAPPER_VIRTUALENV=/home/programacion/.local/bin/virtualenv
        source /home/programacion/.local/bin/virtualenvwrapper.sh
    ```

    WORKON_HOME será el directorio donde se guardarán todos los entornos virtuales creados.
    VIRTUALENVWRAPPER_PYTHON será el directorio donde se encuentra instalado python3.
    VIRTUALENVWRAPPER_VIRTUALENV será el directorio donde se encuentra el ejecutable `virtualenv`.
    Para activar virtualenvwrapper se debe ejecutar el archivo `/home/programacion/.local/bin/virtualenvwrapper.sh`

- Crear un nuevo entorno virtual:

    `$ mkvirtualenv my_env`

- Una vez creado el entorno virtual, se accede a el automaticamente. Comprobar que la consola se muestra de la siguiente manera:

    `(my_env)$ `

- Es posible crear tantos entorno viertuales como se necesiten con `mkvirtualenv`. Para cambiar entre entornos o acceder a uno se utiliza:

    `$ workon env_name`

- Para salir de un entorno virtual se utiliza el siguiente comando:

    `(my_env)$ deactivate`

- Actualmente el entorno utilizado para el desarrollo se llama `mantenimiento_env` y se encuentra en ~/Envs/.

Documentación: https://virtualenvwrapper.readthedocs.io/en/latest/

---
### PostgreSQL en Ubuntu 20.04

- PostgreSQL, o Postgres, es un sistema de administración de bases de datos relacionales que proporciona una implementación del lenguaje de consulta SQL. Los repositorios predeterminados de Ubuntu contienen paquetes de Postgres. Si no lo hizo recientemente, actualice el índice del paquete local de su servidor:

    `$ sudo apt update`

- Instale el paquete de Postgres junto con un paquete -contrib, que agrega algunas utilidades y funcionalidades adicionales:

    `$ sudo apt install postgresql postgresql-contrib`

- Pruebe acceder a una línea de comandos de Postgres:

    `$ sudo -u postgres psql`
    `$ postgres=# \q` (salir)

- Cambie a la cuenta postgres en el servidor:

    `$ sudo -i -u postgres`

- Crear nuevo rol (usuario) según la configuración del proyecto en mantenimiento.config.settings.local.DATABASES. Ingresar el siguiente comando y seguir las instrucciones:

    `$ postgres@server:~$ createuser --interactive`

- Asignar contraseña al usuario creado:

    ```
    $ sudo -i -u postgres psql
    $ postgres=# alter user programacion password 'programacion';
    ```

- Una supósición que la autenticación de Postgres realiza por defecto es que para cualquier rol utilizado en el inicio de sesión habrá una base de datos con el mismo nombre al que este podrá acceder. Cree la base de datos a con el mismo nombre del usuario:

    `$ postgres@server:~$ createdb programacion`

- Acceder a postgres desde la cuenta del usuario creado:

    `$ sudo -i -u programacion`

- Crear una nueva base de datos según la configuración del proyecto en mantenimiento.config.settings.local.DATABASES.

    `programacion@server:~$ createdb name_db`

Documentación: https://www.postgresql.org/docs/

---
### PgAdmin 4 en Ubuntu 20.04
- pgAdmin es una plataforma de desarrollo y administración de código abierto para PostgreSQL. Para instalar pgAdmin ya debemos tener instalado Postgres. Comenzar instalando la clave pública para comprobar las firmas de los paquetes de pgAdmin:

    `$ wget -qO- https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -`

- Crear el archivo de repositorio:

    `$ sudo nano /etc/apt/sources.list.d/pgadmin.list`

- Añadir la línea siguiente: 

    `deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/focal pgadmin4 main`

- Guardar el archivo y actualizar la información de los repositorios del sistema:

    `$ sudo apt update`

- Para instalar pgAdmin en Ubuntu 20.04 LTS una vez configurado el repositorio oficial, se debe instalar el paquete pgadmin4-web con apt:

    `$ sudo apt install -y pgadmin4-web`

- Tras la descarga e instalación de los paquetes necesarios, se debe lanzar el configurador de pgAdmin para Ubuntu 20.04. Este script interactivo nos pedirá los datos para crear el usuario administrador de la aplicación (una dirección de correo y una contraseña) y solicitará confirmación para modificar la configuración del servicio web de Ubuntu 20.04 (configura Apache automáticamente):

    `$ sudo /usr/pgadmin4/bin/setup-web.sh`

- Para acceder a pgAdmin en Ubuntu 20.04 LTS desde un navegador utilizaremos la dirección IP o nombre DNS del servicio y el alias /pgadmin4. En el caso de trabajar en local se debe ingresar a `http://localhost/pgadmin4`

    1. Instroducir el usuario y contraseña indicado en el punto anterior.
    2. Crear un nuevo servidor para la conexión indicando:
        `Nombre: programacion`
        `Dirección del servidor: localhost`
        `Puerto: 5432`
        `Nombre de usuario: programacion`
        `Contraseña (la misma que se ingresó en el paso anterior)`
    3. Guardar cambios
    4. Crear base de datos de acuerdo a las configuraciones del proyecto en mantenimiento.config.settings.local.DATABASES.

Documentación: https://www.pgadmin.org/docs/pgadmin4/6.0/index.html

---
---

# Configuración del proyecto
Una vez que están instalados y configurados todos los requisitos, es posible proceder a levantar el proyecto e integrar todas las herramientas.

### 1. Clonar repositorio en Gitlab
`$ git clone https://gitlab.com/tecnicos.computrol/mantenimiento_interno.git ~/proyectos/`

### 2. Crear entorno virtual
- Creación de entorno virtual:
    `$ mkvirtualenv mantenimiento_env`

- Acceder al antorno virtual:
    `$ workon mantenimiento_env`

### 3. Crear base de datos PostgreSQL
A través de pgAdmin se debe crear una base de datos según las configuraciones del proyecto en mantenimiento.config.settings.local.DATABASE.

### 4. Instalar dependencias
Una vez dentro del entorno virtual se debe proceder a instalar las dependencias del proyecto. El archivo de dependencias se encuentra en `mantenimiento/requirements/local.txt`. Para ello se debe ejecutar el siguiente comando:

`(mantenimiento_env) $ pip install -r mantenimiento/requirements/local.txt`


### 5. Ejecutar migraciones
Si se creó la base de datos Postgres de acuerdo a las configuraciones, ya debería ser posible ejecutar las migraciones. Esta acción creará las tablas en la base de datos necesarias para el proyecto.

- ALTERNATIVA: para restaurar una base de datos utilizando el .sql del backup se utiliza el siguiente comando:

    `psql -U username -d dbname < filename.sql`

- Crear archivos de migraciones para incluir los últimos cambios realizados en los modelos:

    `(mantenimiento_env) $ python mantenimiento/manage.py makemigrations`

- Ejecutar migraciones:

    `(mantenimiento_env) $ python mantenimiento/manage.py migrate`

### 6. Ejecutar servidor de desarrollo
El framework Django trae incluido su propio servidor web para implementar en la etapa de desarrollo.

- Correr servidor de desarrollo:

    `(mantenimiento_env) $ python mantenimiento/manage.py runserver`

- Si el comando no arroja ningún error, la aplicación se podrá visualizar en la dirección `http://localhost:8000/`

Documentación Django: https://docs.djangoproject.com/en/3.2/
