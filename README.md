# Django Blog

## Descripción

Django Blog es una aplicación web desarrollada con Django para publicar artículos y facilitar discusiones. Permite a los usuarios publicar artículos con formato Markdown, comentar en ellos y filtrar por categorías.


## Objetivos
El objetivo principal de este proyecto es crear un blog completamente funcional donde los usuarios puedan:

- Publicar artículos con soporte para formato Markdown.
- Comentar en los artículos.
- Filtrar artículos por categorías.
- Incluir imágenes en los artículos.

## Instalación

1. **Clonar el Repositorio:**

    ```bash
    git clone https://github.com/belenAlcaraz/DjangoBlog.git
    ```

2. **Instalar las Dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Aplicar Migraciones:**

    ```bash
    python manage.py migrate
    ```

4. **Crear un Superusuario:**

    ```bash
    python manage.py createsuperuser
    ```

    Sigue las instrucciones para crear una cuenta de superusuario, que te permitirá acceder al panel de administración.

5. **Iniciar el Servidor de Desarrollo:**

    ```bash
    python manage.py runserver
    ```

El blog estará disponible en [http://localhost:8000/](http://localhost:8000/). Accede al panel de administración en [http://localhost:8000/admin/](http://localhost:8000/admin/) con las credenciales del superusuario para comenzar a gestionar artículos, categorías y usuarios.

¡Listo! Ahora el proyecto Django Blog está instalado y en funcionamiento. Puedes comenzar a explorar y utilizar la aplicación web.

