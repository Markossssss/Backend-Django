# Generated by Django 2.1.3 on 2019-09-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricaoProduto', models.TextField(max_length=500)),
                ('unidadeCompra', models.CharField(max_length=10)),
                ('qtdPrevistoMes', models.FloatField()),
                ('preco', models.FloatField()),
                ('precoMaximo', models.FloatField()),
            ],
        ),
    ]
