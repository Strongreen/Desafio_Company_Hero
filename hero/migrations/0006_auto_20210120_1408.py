# Generated by Django 3.1.5 on 2021-01-20 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0005_auto_20210120_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='nome_fantasia',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='telefone_comercial',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='endereco',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='employeer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='hero.company'),
        ),
    ]
