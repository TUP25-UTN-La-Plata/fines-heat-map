# Mapify Mapa Interactivo

Sistema web para visualizar sedes y comisiones del programa FinEs, con mapa interactivo, filtros y panel de administración.

![Django](https://img.shields.io/badge/Django-5.2.7-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Leaflet](https://img.shields.io/badge/Leaflet-1.9.4-brightgreen)
![DRF](https://img.shields.io/badge/DRF-3.16.1-red)

## Intergrantes y principales responsabilidades:
- Rodrigo Benítez: Frontend, test y validaciones de datos.
- Manuel Guzmán: Frontend, test y validaciones de datos.
- Santiago Matheu: Diseño UX/UI y Frontend.
- Joaquín Miró: Mapa interactivo y Frontend.
- Martín Ramallo: Backend y Backoffice.

Estas son las áreas funcionales y responsabilidades que nos divimos en el equipo, si bien, fuimos compartiendo y colaborando en el código en todo el proyecto.

## Estado actual del proyecto

- Backend con Django 5.2.7 y Django REST Framework.
- Base de datos configurada para PostgreSQL via `DATABASE_URL`.
- Mapa en `mapa/` con endpoints JSON para sedes y filtros.
- Gestión de instituciones/comisiones con vistas y APIs.
- Admin personalizado con `django-unfold`.
- Páginas estáticas para políticas de privacidad y accesibilidad.

## Stack real

- Python, Django 5.2.7, DRF 3.16.1.
- PostgreSQL (`psycopg2-binary` + `dj-database-url`).
- `django-unfold` para el panel de administración.
- `django-import-export` para carga/exportación de datos.
- Leaflet 1.9.4 + Leaflet MarkerCluster + Leaflet.heat.
- Templates Django + JavaScript.

## Estructura del repositorio

```text
fines-heat-map/
├── requirements.txt
├── tailwind.config.js
├── src/input.css
└── fines_heat_map/
    ├── manage.py
    ├── fines_heat_map/              # settings, urls, wsgi, vistas base
    ├── heatmap/                     # mapa + API de sedes
    ├── gestion_instituciones/       # instituciones, modelos y comandos
    ├── gestion_comisiones/          # comisiones, modelos y APIs
    ├── templates/
    └── static/
```

## Instalacion y puesta en marcha

### Prerrequisitos

- Python 3.10 o superior.
- pip.
- Git.
- Una base PostgreSQL accesible mediante URL.

### 1) Clonar

```bash
git clone https://github.com/TUP25-UTN-La-Plata/fines-heat-map.git
cd fines-heat-map
```

### 2) Crear y activar entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3) Instalar dependencias Python

```bash
pip install -r requirements.txt
```

### 4) Configurar variables de entorno

Crear un archivo `.env` en la raiz del proyecto con:

```env
DATABASE_URL=postgresql://usuario:password@host:puerto/dbname
```

> Nota: el proyecto usa `dj_database_url` con `ssl_require=True`.

### 5) Migrar y crear usuario admin

```bash
cd fines_heat_map
python manage.py migrate
python manage.py createsuperuser
```

### 6) Ejecutar servidor

```bash
python manage.py runserver
```

## Rutas principales

- `/` Home.
- `/inicio/` Alias de inicio para compatibilidad con templates legacy.
- `/mapa/` Mapa interactivo.
- `/mapa/api/sedes/` API de sedes con filtros.
- `/mapa/api/sedes/buscar/?nombre=...` Busqueda de sedes por nombre.
- `/instituciones/` Listado de instituciones.
- `/instituciones/<id>/` Detalle de institucion.
- `/comisiones/` Listado de comisiones.
- `/comisiones/api/modulos/` API de modulos.
- `/comisiones/api/orientaciones/` API de orientaciones.
- `/politica-privacidad/` Política de privacidad.
- `/politica-accesibilidad/` Política de accesibilidad.
- `/admin/` Panel administrativo.
- `/errores/404/` y `/errores/500/` Previsualización de páginas de error.

## Comandos utiles

Desde `fines_heat_map/`:

```bash
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py cargar_partidos
python manage.py cargar_localidades
python manage.py test
```

## Testing

- Comando local: `python manage.py test` (desde `fines_heat_map/`).
- CI: se ejecuta en cada push y pull request mediante `.github/workflows/django-tests.yml`.

## Manejo de errores

- Existen templates personalizados `404.html` y `500.html`.
- En producción (`DEBUG=False`) Django usa estos templates mediante `handler404` y `handler500`.

## Nota sobre Tailwind CSS

Actualmente `base.html` carga Tailwind desde CDN (`https://cdn.tailwindcss.com`), por lo que la app funciona sin paso de build CSS local.

Existen archivos de configuracion (`tailwind.config.js`, `src/input.css`, `static/css/output.css`) para un flujo de compilacion local, pero en este estado del repo no hay `package.json` versionado con scripts npm.

## Dependencias Python (requirements.txt)

- Django==5.2.7
- djangorestframework==3.16.1
- django-unfold==0.30.0
- django-import-export==4.3.14
- psycopg2-binary==2.9.11
- dj-database-url==3.0.1
- python-dotenv==1.2.1

## Observaciones

- `settings.py` tiene `DEBUG = True` en el estado actual.
- `ALLOWED_HOSTS` esta orientado a entorno local.
- Para produccion, ajustar variables sensibles y configuracion de seguridad.
