# Generated by Django 3.0.6 on 2020-05-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Inserisci il nome di una lingua, es. inglese, italiano...', max_length=100)),
            ],
        ),
    ]