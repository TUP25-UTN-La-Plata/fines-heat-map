# 🗺️ FinEs Mapa Interactivo

Sistema web de visualización de densidad educativa para instituciones del programa FinEs mediante mapas de calor interactivos.

![Django](https://img.shields.io/badge/Django-5.2.7-green)
![Python](https://img.shields.io/badge/Python-3.13.5-blue)
![Leaflet](https://img.shields.io/badge/Leaflet-1.9.4-brightgreen)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Latest-blue)

## 🎯 Características Principales

- **📊 Mapa de Calor**: Visualización de densidad de instituciones educativas
- **🎨 Admin Moderno**: Panel administrativo personalizado con Tailwind CSS
- **🔍 Filtros Avanzados**: Búsqueda por ubicación, tipo y características
- **📱 Responsive**: Diseño adaptable para todos los dispositivos
- **🔐 Seguro**: Autenticación y protección CSRF integrada

## 🚀 Instalación Rápida

### Prerrequisitos

- Python 3.9+
- pip
- Git

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/TUP25-UTN-La-Plata/fines-heat-map.git
cd fines-heat-map
```

2. **Crear entorno virtual**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**

```bash
cd fines_heat_map
python manage.py migrate
python manage.py createsuperuser
```

5. **Ejecutar servidor**

```bash
python manage.py runserver
```

6. **Acceder a la aplicación**

- **Mapa Principal**: http://127.0.0.1:8000/mapa/
- **Panel Admin**: http://127.0.0.1:8000/admin/

### Requisitos previos

- Python >= 3.10
- Node.js >= 16.x
- npm (viene con Node.js)
- Git

1. **Clona el repositorio:**

   ```bash
   git clone <url-del-repositorio>
   cd fines-heat-map
   ```

2. **Crea y activa el entorno virtual:**

   **En Windows (PowerShell):**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **En Windows (Command Prompt):**

   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```

   **En Linux/macOS:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Tailwind CSS:**
   ```bash
   npm install
   npm run build-css-prod
   ```

---

## 🎯 Funcionalidades principales

- **Mapa interactivo** con pines por comisión (usando Leaflet/OpenStreetMap).
- **Popups con información de cada comisión**: nombre de sede, número de comisión, tutor responsable (solo nombre, ver posibilidad de teléfono), turno, módulos y orientación.
- **Filtros dinámicos** por turno, módulo y orientación.
- **Mapa de calor (heatmap)** opcional para ver concentración de comisiones.
- **CRUD de comisiones** (solo para usuarios admin/coordinadores).
- **Panel de administración** para gestionar sedes y comisiones.
- **Responsive design**: funcional en escritorio y dispositivos móviles.
- **Accesibilidad**: texto legible, botones grandes y microcopy positivo.

---

## 🧑‍🤝‍🧑 Público objetivo

- Estudiantes adultos (>18 años) que buscan completar su secundaria.
- Familiares y tutores que ayudan en la búsqueda de comisiones.
- Coordinadores FinEs que administran sedes y comisiones.

---

## 🎨 Estilo y experiencia

- Minimalista y moderno, con **paleta positiva y educativa** (agua, verde menta, celeste, acentos cálidos).
- Tipografía legible y amigable (Inter, Nunito o Poppins).
- Diseño motivador, inclusivo y optimista.
- Interfaz centrada en accesibilidad y usabilidad para adultos con poca experiencia digital.

---

## 🛠 Stack tecnológico

- **Backend:** Python 3.x + Django + Django REST Framework
- **Base de datos:** PostgreSQL (integrada con Django, usando ArrayField para módulos)
- **Frontend:** Templates Django + Leaflet + Leaflet.heat + JavaScript
- **Autenticación:** Django admin para usuarios coordinadores/admin
- **Contenedores:** Docker + Docker Compose (opcional para desarrollo)
- **Importación de datos:** CSV mediante management command en Django

---

## ⚙ Requerimientos técnicos

- Python >= 3.10
- Django >= 4.2
- Django REST Framework >= 3.14
- psycopg2-binary (para PostgreSQL)
- Leaflet.js y Leaflet.heat para la visualización de mapas
- Navegador moderno (Chrome, Firefox, Edge, Safari)
- Docker y Docker Compose (opcional, recomendado para desarrollo local)

### Requerimientos funcionales

- CRUD de comisiones (solo para administradores)
- Visualización de mapa interactivo con filtros
- Mapa de calor opcional
- Popups con información detallada de la comisión
- Panel de administración seguro y accesible

### Requerimientos no funcionales

- Responsive y usable en dispositivos móviles
- Accesibilidad: texto claro, contraste suficiente, botones grandes
- Rendimiento: carga rápida del mapa con muchas comisiones
- Seguridad: autenticación para admin, HTTPS en producción

---

## 🏗 Infraestructura recomendada

- **Base de datos:** PostgreSQL alojada en la misma app (desarrollo) o en servicio cloud (producción: Render, Heroku, Digital Ocean).
- **Backend:** Django + REST Framework (API + templates)
- **Frontend:** Leaflet en templates Django
- **Contenedores (opcional):** Docker Compose para DB y backend
- **Hosting producción:** Render, Heroku, AWS, o Digital Ocean.

---
