# Generated by Django 3.2.18 on 2023-04-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountbooks', '0002_lineitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbook',
            name='category',
            field=models.CharField(choices=[('A', '  '), ('B', '  '), ('C', '  '), ('D', '  ')], max_length=20),
        ),
    ]