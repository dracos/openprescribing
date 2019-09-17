# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-24 17:27


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0048_auto_20190522_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillog',
            name='message',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.EmailMessage'),
        ),
        migrations.AlterField(
            model_name='ncsoconcession',
            name='vmpp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dmd2.VMPP'),
        ),
        migrations.AlterField(
            model_name='ncsoconcessionbookmark',
            name='pct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PCT'),
        ),
        migrations.AlterField(
            model_name='ncsoconcessionbookmark',
            name='practice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.Practice'),
        ),
        migrations.AlterField(
            model_name='orgbookmark',
            name='pct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PCT'),
        ),
        migrations.AlterField(
            model_name='orgbookmark',
            name='practice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.Practice'),
        ),
        migrations.AlterField(
            model_name='pct',
            name='regional_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.RegionalTeam'),
        ),
        migrations.AlterField(
            model_name='pct',
            name='stp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.STP'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='ccg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PCT'),
        ),
        migrations.AlterField(
            model_name='practiceisdispensing',
            name='practice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='frontend.Practice'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='replaced_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.Presentation'),
        ),
        migrations.AlterField(
            model_name='qofprevalence',
            name='pct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PCT'),
        ),
        migrations.AlterField(
            model_name='qofprevalence',
            name='practice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.Practice'),
        ),
        migrations.AlterField(
            model_name='tariffprice',
            name='tariff_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dmd2.DtPaymentCategory'),
        ),
        migrations.AlterField(
            model_name='tariffprice',
            name='vmpp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dmd2.VMPP'),
        ),
    ]
