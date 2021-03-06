# Generated by Django 2.0 on 2017-12-18 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='vane no te duermas', max_length=80, verbose_name='Titulo')),
                ('cuerpo', models.CharField(max_length=200, verbose_name='Cuerpo del mensaje')),
                ('usuarioDesteinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario_Desteinatario', to=settings.AUTH_USER_MODEL)),
                ('usuarioRemitente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Usuario_Remitente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
