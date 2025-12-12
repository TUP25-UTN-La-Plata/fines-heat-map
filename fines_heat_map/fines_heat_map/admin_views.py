from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse
from django.contrib import admin
from .dashboard import dashboard_callback


@staff_member_required
def dashboard_view(request):
    """
    Vista del dashboard como página separada.
    """
    # Obtener datos del dashboard
    try:
        dashboard_data = dashboard_callback(request)
    except Exception as e:
        import traceback
        print(f"Error al cargar dashboard: {e}")
        traceback.print_exc()
        dashboard_data = None
    
    context = admin.site.each_context(request)
    context.update({
        'title': 'Dashboard',
        'subtitle': 'Estadísticas y Gráficos',
        'dashboard_data': dashboard_data,
    })
    
    return TemplateResponse(request, 'admin/dashboard.html', context)

