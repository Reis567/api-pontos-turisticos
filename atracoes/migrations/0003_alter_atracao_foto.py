# Generated by Django 4.2.7 on 2023-11-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]