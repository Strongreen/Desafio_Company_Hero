# Generated by Django 3.1.5 on 2021-01-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_auto_20210120_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='inscricao_municipal_estadual',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
    ]
