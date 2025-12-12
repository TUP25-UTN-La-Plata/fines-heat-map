# Generated manually to allow null horario and add 'I' turno option

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_comisiones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='horario',
            field=models.CharField(blank=True, help_text='Días y horarios', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comision',
            name='turno',
            field=models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('V', 'Vespertino'), ('N', 'Noche'), ('I', 'Intermedio')], max_length=1),
        ),
    ]

