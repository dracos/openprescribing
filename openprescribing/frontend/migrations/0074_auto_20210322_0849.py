# Generated by Django 2.2.16 on 2021-03-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0073_remove_unused_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pct',
            name='code',
            field=models.CharField(help_text='Primary care trust code', max_length=5, primary_key=True, serialize=False),
        ),
    ]