# FinEs Heat Map - AI Coding Guidelines

## Project Overview

Interactive web system for visualizing educational institution density for the FinEs program (adult secondary education) through heatmaps. Django backend with Leaflet.js frontend for geographic data visualization.

## Architecture & Structure

### Core Applications

- **`heatmap/`** - Main map visualization with Leaflet.js integration
- **`gestion_instituciones/`** - Institution management (models pending)
- **`gestion_comisiones/`** - Commission/class management (models pending)
- **`templates/`** - Centralized templates with component includes (`includes/`)

### URL Pattern

```python
# fines_heat_map/urls.py - Uses namespaced includes
path("mapa/", include(("heatmap.urls", "heatmap"), namespace="heatmap"))
path("instituciones/", include(("gestion_instituciones.urls", "gestion_instituciones"), namespace="instituciones"))
```

## Development Workflow

### Environment Setup

```bash
# Always work from fines_heat_map/ directory
cd fines_heat_map
python manage.py runserver  # Development server

# Tailwind CSS workflow
npm run build-css          # Development (watch mode)
npm run build-css-prod     # Production build
```

### Database & Models

- **Current**: SQLite3 with empty models (development stage)
- **Target**: PostgreSQL with geo-spatial data for institutions/commissions
- Models are placeholders - check `models.py` files before implementing features

## Frontend Architecture

### Template Structure

- **Base**: `templates/base.html` includes Leaflet, Tailwind, and heatmap libraries
- **Components**: `templates/includes/` for reusable elements (navbar, footer, map_scripts)
- **Apps**: Each app has its own template directory

### Map Implementation (Critical Pattern)

```javascript
// heatmap/mapa.html - Dual approach for reliability
// 1. Custom circle-based heatmap (primary)
// 2. Leaflet.heat plugin (fallback)
// Always include test data when real data is empty
```

### Styling System

- **Tailwind CSS**: Primary styling with custom FinEs color palette
- **Custom colors**: `fines-blue`, `fines-green`, `fines-mint`, `fines-encabezado-*`
- **Config**: `tailwind.config.js` scans all template paths

## Project-Specific Patterns

### Data Flow (When Models Are Ready)

```python
# Pattern for view-template data passing
context = {"places": []}  # Currently empty
{{ places|json_script:"places-data" }}  # Safe JS data transfer
```

### Admin Customization

- Custom admin templates in `templates/admin/` (base_site.html, login.html)
- Logout functionality integrated into map interface

### Static Files

- **CSS**: `static/css/output.css` (Tailwind build output)
- **Images**: `static/img/`
- **Source**: `src/input.css` (Tailwind input file)

## Key Integration Points

### Geographic Libraries

```html
<!-- base.html - Required in this order -->
<link
  rel="stylesheet"
  href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js"></script>
<script src="https://unpkg.com/leaflet.heat@0.2.0/dist/leaflet-heat.js"></script>
```

### Responsive Design

- Mobile-first approach for adult users with limited digital experience
- Sidebar filters (`w-80`) with main map area (`flex-1`)
- Full viewport height for map container (`h-screen`)

## Critical Development Notes

1. **Models Pending**: All `models.py` files are empty - implement geographic models first
2. **Data Integration**: Views have TODO comments for real database connections
3. **Localization**: `LANGUAGE_CODE = "es-AR"`, `TIME_ZONE = "America/Argentina/Buenos_Aires"`
4. **Security**: Development mode - update SECRET_KEY and DEBUG for production

## Common Tasks

### Adding New Geographic Features

1. Implement models in relevant app (`gestion_instituciones` or `gestion_comisiones`)
2. Update corresponding views to pass geographic data
3. Modify `mapa.html` to consume new data structure
4. Test with both custom heatmap and Leaflet.heat implementations

### UI Component Development

1. Use Tailwind classes with FinEs color palette
2. Follow `templates/includes/` pattern for reusability
3. Ensure mobile responsiveness for target demographic
4. Test filter interactions with map updates

### Deployment Preparation

1. Update `settings.py` security settings
2. Configure PostgreSQL database
3. Run Tailwind production build: `npm run build-css-prod`
4. Implement geographic data import commands
