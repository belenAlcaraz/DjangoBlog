# DjangoBlog
Es un proyecto personal para desarrollar una aplicación web con Django que nos permita publicar artículos en un blog. 
## Configuración del Entorno

Asegúrate de tener Python y pip instalados en tu sistema.

```bash
pip install -r requirements.txt


Configuración de la Base de Datos
Realiza las migraciones iniciales:
bash
Copy code
python manage.py migrate
Crea un superusuario para administrar el blog:
bash
Copy code
python manage.py createsuperuser
Ejecución del Servidor
Inicia el servidor de desarrollo:

bash
Copy code
python manage.py runserver
Visita http://127.0.0.1:8000/ en tu navegador.

Uso
Este blog permite a los usuarios:

Crear, actualizar y eliminar publicaciones.
Comentar en publicaciones.
Filtrar publicaciones por categorías.
Contribución
Si quieres contribuir, sigue estos pasos:

Crea un fork del repositorio.
Clona el fork en tu máquina local.
Crea una nueva rama para tu contribución.
Realiza los cambios y haz commit.
Envía un pull request.

