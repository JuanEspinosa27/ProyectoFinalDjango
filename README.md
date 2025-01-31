# Gimnasio - Aplicación Web Django

Esta es una aplicación web para la gestión de un gimnasio desarrollada con Django, siguiendo el patrón MVT (Model-View-Template).

## Características

- Gestión de Miembros
- Gestión de Entrenadores
- Gestión de Clases
- Sistema de búsqueda integrado
- Interfaz responsive con Bootstrap

## Modelos

1. Member (Miembro)
   - Nombre
   - Email
   - Teléfono
   - Tipo de membresía
   - Fecha de ingreso

2. Trainer (Entrenador)
   - Nombre
   - Especialización
   - Experiencia
   - Teléfono
   - Email

3. Class (Clase)
   - Nombre
   - Entrenador (relación con modelo Trainer)
   - Horario
   - Capacidad
   - Descripción

## Orden de Prueba

1. Configuración Inicial:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

2. Prueba de Funcionalidades:

   a. Gestión de Entrenadores:
   - Ir a "/trainers/"
   - Agregar un nuevo entrenador
   - Verificar que aparezca en la lista

   b. Gestión de Clases:
   - Ir a "/classes/"
   - Agregar una nueva clase
   - Verificar que aparezca en la lista

   c. Gestión de Miembros:
   - Ir a "/members/"
   - Agregar un nuevo miembro
   - Verificar que aparezca en la lista

   d. Sistema de Búsqueda:
   - Ir a "/search/"
   - Realizar búsquedas por diferentes términos
   - Verificar que los resultados se muestren correctamente

## Ubicación de Funcionalidades

- Modelos: `gym_app/models.py`
- Vistas: `gym_app/views.py`
- Formularios: `gym_app/forms.py`
- URLs: `gym_app/urls.py`
- Plantillas: `gym_app/templates/gym_app/`
- Configuración principal: `gym_project/settings.py`

## Herencia de Templates

Todas las plantillas heredan de `base.html`, que incluye:
- Navbar responsiva
- Bootstrap CSS y JS
- Estructura básica HTML
- Bloques para título y contenido