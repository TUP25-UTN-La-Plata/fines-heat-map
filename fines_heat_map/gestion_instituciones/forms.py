from django import forms


class InstitucionFilterForm(forms.Form):
    """Formulario de filtros para la lista de instituciones"""
    
    search = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-fines-blue focus:border-fines-blue sm:text-sm",
                "placeholder": "Buscar por nombre de institución..."
            }
        ),
        label="Búsqueda"
    )
    
    province = forms.ChoiceField(
        choices=[("", "Todas las provincias")] + [
            ("Buenos Aires", "Buenos Aires"),
            ("CABA", "Ciudad Autónoma de Buenos Aires"),
            ("Córdoba", "Córdoba"),
            ("Santa Fe", "Santa Fe"),
            # Se pueden agregar más provincias según necesidad
        ],
        required=False,
        widget=forms.Select(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-fines-blue focus:border-fines-blue sm:text-sm"
            }
        ),
        label="Provincia"
    )
    
    city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-fines-blue focus:border-fines-blue sm:text-sm",
                "placeholder": "Ciudad..."
            }
        ),
        label="Ciudad"
    )
    
    turno = forms.ChoiceField(
        choices=[("", "Todos los turnos")] + [
            ("Mañana", "Mañana"),
            ("Tarde", "Tarde"),
            ("Noche", "Noche"),
        ],
        required=False,
        widget=forms.Select(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-fines-blue focus:border-fines-blue sm:text-sm"
            }
        ),
        label="Turno"
    )
    
    orientation = forms.ChoiceField(
        choices=[("", "Todas las orientaciones")] + [
            ("Ciencias Sociales", "Ciencias Sociales"),
            ("Ciencias Naturales", "Ciencias Naturales"),
            ("Economía y Administración", "Economía y Administración"),
            ("Arte", "Arte"),
            ("Comunicación", "Comunicación"),
        ],
        required=False,
        widget=forms.Select(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-fines-blue focus:border-fines-blue sm:text-sm"
            }
        ),
        label="Orientación"
    )
    
    def get_filter_params(self):
        """Retorna los parámetros de filtrado válidos"""
        if not self.is_valid():
            return {}
            
        filters = {}
        
        if self.cleaned_data.get('search'):
            filters['search'] = self.cleaned_data['search']
            
        if self.cleaned_data.get('province'):
            filters['province'] = self.cleaned_data['province']
            
        if self.cleaned_data.get('city'):
            filters['city'] = self.cleaned_data['city']
            
        if self.cleaned_data.get('turno'):
            filters['turno'] = self.cleaned_data['turno']
            
        if self.cleaned_data.get('orientation'):
            filters['orientation'] = self.cleaned_data['orientation']
            
        return filters
