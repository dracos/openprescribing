# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 13:12


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dmd2', '0002_auto_20181007_1443'),
        ('frontend', '0045_auto_20190508_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='TariffPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('price_pence', models.IntegerField()),
                ('tariff_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmd2.DtPaymentCategory')),
                ('vmpp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmd2.VMPP')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tariffprice',
            unique_together=set([('date', 'vmpp')]),
        ),
    ]
