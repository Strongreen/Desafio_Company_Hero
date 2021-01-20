# Generated by Django 3.1.5 on 2021-01-20 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.company')),
            ],
        ),
    ]