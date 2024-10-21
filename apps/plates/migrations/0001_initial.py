# Generated by Django 5.1.1 on 2024-10-01 10:59

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0, verbose_name='Precio')),
                ('image', models.ImageField(upload_to='plates/', verbose_name='Imagen')),
                ('category', models.ManyToManyField(related_name='category', to='categories.categories')),
                ('ingredients', models.ManyToManyField(related_name='ingredients', to='ingredients.ingredients')),
            ],
            options={
                'verbose_name': 'Plate',
                'verbose_name_plural': 'Plates',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PlatesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('descriptions', models.TextField(verbose_name='Descripcion')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='plates.plates')),
            ],
            options={
                'verbose_name': 'Plate Translation',
                'db_table': 'plates_plates_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
