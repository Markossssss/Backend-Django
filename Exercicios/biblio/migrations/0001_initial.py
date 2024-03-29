# Generated by Django 2.1.3 on 2019-09-04 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=10)),
                ('autor', models.CharField(max_length=100)),
                ('assunto', models.TextField()),
                ('editora', models.CharField(max_length=50)),
                ('ISBN', models.IntegerField()),
                ('ano_publicacao', models.DateField()),
            ],
        ),
    ]
