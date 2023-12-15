# Django Blog

## Descripción

Django Blog es una aplicación web desarrollada con Django para publicar artículos y facilitar discusiones. Permite a los usuarios publicar artículos con formato Markdown, comentar en ellos y filtrar por categorías.


## Objetivos
El objetivo principal de este proyecto es crear un blog completamente funcional donde los usuarios puedan:

- Publicar artículos con soporte para formato Markdown.
- Comentar en los artículos.
- Filtrar artículos por categorías.
- Incluir imágenes en los artículos.

## Vistas y URLs

A continuación se describen las principales vistas y URLs de la aplicación DjangoBlog:

| URL                                  | Descripción                   |
|--------------------------------------|-------------------------------|
| [/](#inicio)                         | Página de inicio              |
| [/articulo/{id}](#articulos)         | Detalles de un artículo       |
| [/agregar_publicacion/](#agregar-publicacion)  | Agregar una nueva publicación |
| [/articulo/actualizar/{id}](#actualizar-publicacion) | Actualizar una publicación existente |
| [/articulo/eliminar_publicacion/{id}](#eliminar-publicacion) | Eliminar una publicación existente |
| [/articulo/agregar_comentario/{id}](#agregar-comentario) | Agregar un comentario a una publicación |
| [/articulo/eliminar_comentario/{id}](#eliminar-comentario) | Eliminar un comentario |
| [/articulo/actualizar_comentario/{id}](#actualizar-comentario) | Actualizar un comentario existente |
| [/agregar_categoria/](#agregar-categoria) | Agregar una nueva categoría   |
| [/categorias/](#categorias)           | Lista de categorías           |
| [/categorias/{id}/](#publicaciones-por-categoria) | Publicaciones por categoría  |
| [/usuarios/](#usuarios)               | URLs de autenticación de usuarios |

**Nota:** Sustituye `{id}` con el identificador numérico correspondiente a cada elemento (por ejemplo, el ID de una publicación, comentario o categoría).

### Descripciones Detalladas:

- **Inicio:** Página principal de la aplicación.
- **Artículos:** Detalles de un artículo específico.
- **Agregar Publicación:** Página para agregar una nueva publicación.
- **Actualizar Publicación:** Página para actualizar una publicación existente.
- **Eliminar Publicación:** Página para eliminar una publicación existente.
- **Agregar Comentario:** Página para agregar un comentario a una publicación.
- **Eliminar Comentario:** Página para eliminar un comentario existente.
- **Actualizar Comentario:** Página para actualizar un comentario existente.
- **Agregar Categoría:** Página para agregar una nueva categoría.
- **Categorías:** Lista de todas las categorías.
- **Publicaciones por Categoría:** Lista de publicaciones filtradas por categoría.
- **Usuarios:** URLs relacionadas con la autenticación de usuarios.

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

