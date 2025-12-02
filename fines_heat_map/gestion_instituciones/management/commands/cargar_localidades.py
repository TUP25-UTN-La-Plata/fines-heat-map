from django.core.management.base import BaseCommand
from gestion_instituciones.models import Partido, Localidad

class Command(BaseCommand):
    help = 'Carga localidades y códigos postales vinculados a los Partidos'

    def handle(self, *args, **kwargs):
        # Estructura: "Nombre Exacto del Partido": [("Nombre Localidad", "CP"), ...]
        datos_geograficos = {
            "La Plata": [
                ("La Plata (Casco Urbano)", "1900"),
                ("Tolosa", "1900"),
                ("Ringuelet", "1901"),
                ("Gonnet", "1897"),
                ("City Bell", "1896"),
                ("Villa Elisa", "1894"),
                ("Los Hornos", "1909"),
                ("Villa Elvira", "1904"),
                ("Altos de San Lorenzo", "1903"),
                ("San Carlos", "1906"),
            ],
            "La Matanza": [
                ("San Justo", "1754"),
                ("Ramos Mejía", "1704"),
                ("Gregorio de Laferrere", "1757"),
                ("González Catán", "1759"),
                ("Virrey del Pino", "1763"),
                ("Isidro Casanova", "1765"),
                ("Ciudad Evita", "1778"),
                ("Tapiales", "1770"),
            ],
            "General Pueyrredón": [
                ("Mar del Plata", "7600"),
                ("Batán", "7601"),
                ("Sierra de los Padres", "7601"),
            ],
            "Bahía Blanca": [
                ("Bahía Blanca", "8000"),
                ("Ingeniero White", "8103"),
                ("General Daniel Cerri", "8105"),
            ],
            "Lomas de Zamora": [
                ("Lomas de Zamora", "1832"),
                ("Banfield", "1828"),
                ("Temperley", "1834"),
                ("Llavallol", "1836"),
            ],
            "Quilmes": [
                ("Quilmes", "1878"),
                ("Bernal", "1876"),
                ("San Francisco Solano", "1881"),
                ("Ezpeleta", "1882"),
            ],
            "Avellaneda": [
                ("Avellaneda", "1870"),
                ("Sarandí", "1872"),
                ("Villa Domínico", "1874"),
                ("Wilde", "1875"),
            ],
            "Lanús": [
                ("Lanús", "1824"),
                ("Remedios de Escalada", "1826"),
                ("Gerli", "1823"),
                ("Monte Chingolo", "1825"),
            ],
            "San Isidro": [
                ("San Isidro", "1642"),
                ("Boulogne", "1609"),
                ("Martínez", "1640"),
                ("Beccar", "1643"),
            ],
             "Vicente López": [
                ("Olivos", "1636"),
                ("Florida", "1602"),
                ("Vicente López", "1638"),
                ("Villa Martelli", "1603"),
            ],
             "Tandil": [
                ("Tandil", "7000"),
                ("María Ignacia (Vela)", "7003"),
            ],
             "San Nicolás": [
                ("San Nicolás de los Arroyos", "2900"),
                ("General Rojo", "2905"),
            ],
        }

        contador_creadas = 0
        partidos_no_encontrados = []

        self.stdout.write("Iniciando carga de localidades...")

        for nombre_partido, localidades in datos_geograficos.items():
            try:
                # Buscamos el partido. Debe existir previamente.
                partido_obj = Partido.objects.get(nombre=nombre_partido)
                
                for nombre_loc, cp in localidades:
                    # Usamos get_or_create para evitar duplicados si corres el script 2 veces
                    loc_obj, created = Localidad.objects.get_or_create(
                        partido=partido_obj,
                        nombre=nombre_loc,
                        defaults={'codigo_postal': cp}
                    )
                    
                    if created:
                        contador_creadas += 1
                        # self.stdout.write(f" -> Creada: {nombre_loc}") 
                    else:
                        # Si ya existe, actualizamos el CP por si cambió
                        if loc_obj.codigo_postal != cp:
                            loc_obj.codigo_postal = cp
                            loc_obj.save()

            except Partido.DoesNotExist:
                partidos_no_encontrados.append(nombre_partido)
                self.stdout.write(self.style.WARNING(f"⚠ Partido no encontrado: {nombre_partido}"))

        self.stdout.write(self.style.SUCCESS('-----------------------------------'))
        self.stdout.write(self.style.SUCCESS('¡Proceso finalizado!'))
        self.stdout.write(self.style.SUCCESS(f'Localidades nuevas creadas: {contador_creadas}'))
        
        if partidos_no_encontrados:
            self.stdout.write(self.style.ERROR(f'Partidos ignorados (revisar nombres): {partidos_no_encontrados}'))