from django import forms


class MapFilterForm(forms.Form):
    """
    Formulario para filtros del mapa de calor.
    Centraliza las opciones y la lógica de filtrado.
    """

    # Choices para los campos de filtro
    PROVINCE_CHOICES = [
        ("", "Todas"),
        ("Buenos Aires", "Buenos Aires"),
        ("Córdoba", "Córdoba"),
        ("Santa Fe", "Santa Fe"),
        ("Mendoza", "Mendoza"),
        ("Tucumán", "Tucumán"),
    ]

    CITY_CHOICES = {
        "Buenos Aires": [
            ("", "Todas"),
            ("La Plata", "La Plata"),
            ("Mar del Plata", "Mar del Plata"),
            ("Bahía Blanca", "Bahía Blanca"),
            ("San Nicolás", "San Nicolás"),
        ],
        "Córdoba": [
            ("", "Todas"),
            ("Córdoba Capital", "Córdoba Capital"),
            ("Villa María", "Villa María"),
            ("Río Cuarto", "Río Cuarto"),
        ],
        "Santa Fe": [
            ("", "Todas"),
            ("Santa Fe Capital", "Santa Fe Capital"),
            ("Rosario", "Rosario"),
            ("Rafaela", "Rafaela"),
        ],
    }

    TURNO_CHOICES = [
        ("", "Todos"),
        ("mañana", "Mañana"),
        ("tarde", "Tarde"),
        ("noche", "Noche"),
    ]

    MODULES_CHOICES = [
        ("", "Todos"),
        ("Matemática", "Matemática"),
        ("Lengua", "Lengua"),
        ("Historia", "Historia"),
        ("Biología", "Biología"),
        ("Química", "Química"),
        ("Física", "Física"),
        ("Tecnología", "Tecnología"),
    ]

    ORIENTATION_CHOICES = [
        ("", "Todas"),
        ("Ciencias Sociales", "Ciencias Sociales"),
        ("Ciencias Naturales", "Ciencias Naturales"),
        ("Técnica", "Técnica"),
        ("Economía", "Economía"),
        ("Arte", "Arte"),
    ]

    # Campos del formulario
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ej: Escuela 3, Juan Pérez",
                "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            }
        ),
        label="Buscar por nombre o tutor",
    )

    province = forms.ChoiceField(
        choices=PROVINCE_CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            }
        ),
        label="Provincia",
    )

    city = forms.ChoiceField(
        choices=[("", "Todas")],  # Se poblará dinámicamente
        required=False,
        widget=forms.Select(
            attrs={
                "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            }
        ),
        label="Ciudad",
    )

    turno = forms.ChoiceField(
        choices=TURNO_CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            }
        ),
        label="Turno",
    )

    modules = forms.ChoiceField(
        choices=MODULES_CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            }
        ),
        label="Módulos",
    )

    orientation = forms.ChoiceField(
        choices=ORIENTATION_CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
            }
        ),
        label="Orientación",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Poblar opciones de ciudad basado en provincia seleccionada
        if self.data.get("province"):
            province = self.data.get("province")
            if province in self.CITY_CHOICES:
                self.fields["city"].choices = self.CITY_CHOICES[province]

    def get_filter_params(self):
        """
        Retorna un diccionario con los parámetros de filtro válidos.
        """
        if not self.is_valid():
            return {}

        filters = {}
        for field_name, value in self.cleaned_data.items():
            if value:  # Solo incluir valores no vacíos
                filters[field_name] = value

        return filters
