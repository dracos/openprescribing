# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-24 12:48
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('bnf_code', models.CharField(
                    max_length=9, primary_key=True,
                    serialize=False, validators=[
                        django.core.validators.RegexValidator(
                            b'^[\\w]*$', code=b'Invalid name',
                            message=b'name must be alphanumeric')])),
                ('chem_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.CharField(max_length=40,
                                        primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('why_it_matters', models.TextField(blank=True, null=True)),
                ('numerator_description', models.CharField(
                    blank=True, max_length=500, null=True)),
                ('denominator_description', models.CharField(
                    blank=True, max_length=500, null=True)),
                ('numerator_short', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('denominator_short', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('is_percentage', models.NullBooleanField()),
                ('is_cost_based', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MeasureGlobal',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('numerator', models.FloatField(blank=True, null=True)),
                ('denominator', models.FloatField(blank=True, null=True)),
                ('calc_value', models.FloatField(blank=True, null=True)),
                ('num_items', models.IntegerField(blank=True, null=True)),
                ('denom_items', models.IntegerField(blank=True, null=True)),
                ('num_cost', models.FloatField(blank=True, null=True)),
                ('denom_cost', models.FloatField(blank=True, null=True)),
                ('num_quantity', models.FloatField(blank=True, null=True)),
                ('denom_quantity', models.FloatField(blank=True, null=True)),
                ('percentiles', django.contrib.postgres.fields.jsonb.JSONField(
                    blank=True, null=True)),
                ('cost_savings',
                 django.contrib.postgres.fields.jsonb.JSONField(
                     blank=True, null=True)),
                ('measure', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.Measure')),
            ],
        ),
        migrations.CreateModel(
            name='MeasureValue',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('month', models.DateField()),
                ('numerator', models.FloatField(blank=True, null=True)),
                ('denominator', models.FloatField(blank=True, null=True)),
                ('calc_value', models.FloatField(blank=True, null=True)),
                ('num_items', models.IntegerField(blank=True, null=True)),
                ('denom_items', models.IntegerField(blank=True, null=True)),
                ('num_cost', models.FloatField(blank=True, null=True)),
                ('denom_cost', models.FloatField(blank=True, null=True)),
                ('num_quantity', models.FloatField(blank=True, null=True)),
                ('denom_quantity', models.FloatField(blank=True, null=True)),
                ('percentile', models.FloatField(blank=True, null=True)),
                ('cost_savings',
                 django.contrib.postgres.fields.jsonb.JSONField(
                    blank=True, null=True)),
                ('measure', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.Measure')),
            ],
        ),
        migrations.CreateModel(
            name='PCT',
            fields=[
                ('code', models.CharField(help_text=b'Primary care trust code',
                                          max_length=3, primary_key=True,
                                          serialize=False)),
                ('ons_code', models.CharField(blank=True, max_length=9,
                                              null=True)),
                ('name', models.CharField(blank=True, max_length=200,
                                          null=True)),
                ('org_type', models.CharField(
                    choices=[(b'CCG', b'CCG'), (b'PCT', b'PCT'), (
                        b'H', b'Hub'), (b'Unknown', b'Unknown')],
                    default=b'Unknown', max_length=9)),
                ('boundary', django.contrib.gis.db.models.fields.GeometryField(
                    blank=True, null=True, srid=4326)),
                ('open_date', models.DateField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=400,
                                             null=True)),
                ('postcode', models.CharField(
                    blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('code', models.CharField(help_text=b'Practice code',
                                          max_length=6, primary_key=True,
                                          serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address1', models.CharField(blank=True, max_length=200,
                                              null=True)),
                ('address2', models.CharField(blank=True, max_length=200,
                                              null=True)),
                ('address3', models.CharField(blank=True, max_length=200,
                                              null=True)),
                ('address4', models.CharField(blank=True, max_length=200,
                                              null=True)),
                ('address5', models.CharField(blank=True, max_length=200,
                                              null=True)),
                ('postcode', models.CharField(blank=True, max_length=9,
                                              null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(
                    blank=True, null=True, srid=4326)),
                ('setting', models.IntegerField(choices=[
                    (-1, b'Unknown'),
                    (0, b'Other'),
                    (1, b'WIC Practice'),
                    (2, b'OOH Practice'),
                    (3, b'WIC + OOH Practice'),
                    (4, b'GP Practice'),
                    (8, b'Public Health Service'),
                    (9, b'Community Health Service'),
                    (10, b'Hospital Service'),
                    (11, b'Optometry Service'),
                    (12, b'Urgent & Emergency Care'),
                    (13, b'Hospice'),
                    (14, b'Care Home / Nursing Home'),
                    (15, b'Border Force'),
                    (16, b'Young Offender Institution'),
                    (17, b'Secure Training Centre'),
                    (18, b"Secure Children's Home"),
                    (19, b'Immigration Removal Centre'),
                    (20, b'Court'),
                    (21, b'Police Custody'),
                    (22, b'Sexual Assault Referral Centre (SARC)'),
                    (24, b'Other - Justice Estate'),
                    (25, b'Prison')], default=-1)),
                ('open_date', models.DateField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('join_provider_date', models.DateField(blank=True,
                                                        null=True)),
                ('leave_provider_date', models.DateField(blank=True,
                                                         null=True)),
                ('status_code', models.CharField(blank=True, choices=[
                    (b'U', b'Unknown'),
                    (b'A', b'Active'),
                    (b'B', b'Retired'),
                    (b'C', b'Closed'),
                    (b'D', b'Dormant'),
                    (b'P', b'Proposed')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeIsDispensing',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('date', models.DateField()),
                ('practice', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.Practice')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('date', models.DateField()),
                ('male_0_4', models.IntegerField()),
                ('female_0_4', models.IntegerField()),
                ('male_5_14', models.IntegerField()),
                ('female_5_14', models.IntegerField()),
                ('male_15_24', models.IntegerField()),
                ('female_15_24', models.IntegerField()),
                ('male_25_34', models.IntegerField()),
                ('female_25_34', models.IntegerField()),
                ('male_35_44', models.IntegerField()),
                ('female_35_44', models.IntegerField()),
                ('male_45_54', models.IntegerField()),
                ('female_45_54', models.IntegerField()),
                ('male_55_64', models.IntegerField()),
                ('female_55_64', models.IntegerField()),
                ('male_65_74', models.IntegerField()),
                ('female_65_74', models.IntegerField()),
                ('male_75_plus', models.IntegerField()),
                ('female_75_plus', models.IntegerField()),
                ('total_list_size', models.IntegerField()),
                ('astro_pu_cost', models.FloatField()),
                ('astro_pu_items', models.FloatField()),
                ('star_pu', django.contrib.postgres.fields.jsonb.JSONField(
                    blank=True, null=True)),
                ('pct', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.PCT')),
                ('practice', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.Practice')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('presentation_code', models.CharField(
                    max_length=15,
                    validators=[
                        django.core.validators.RegexValidator(
                            b'^[\\w]*$', code=b'Invalid name',
                            message=b'name must be alphanumeric')])),
                ('presentation_name', models.CharField(max_length=1000)),
                ('total_items', models.IntegerField()),
                ('net_cost', models.FloatField()),
                ('actual_cost', models.FloatField()),
                ('quantity', models.FloatField()),
                ('processing_date', models.DateField()),
                ('price_per_unit', models.FloatField()),
                ('chemical', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.Chemical')),
                ('pct', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.PCT')),
                ('practice', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.Practice')),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('bnf_code', models.CharField(
                    max_length=15, primary_key=True,
                    serialize=False, validators=[
                        django.core.validators.RegexValidator(
                            b'^[\\w]*$', code=b'Invalid name',
                            message=b'name must be alphanumeric')])),
                ('name', models.CharField(max_length=200)),
                ('is_generic', models.NullBooleanField(default=None)),
                ('active_quantity', models.FloatField(blank=True, null=True)),
                ('adq', models.FloatField(blank=True, null=True)),
                ('adq_unit', models.CharField(blank=True, max_length=10,
                                              null=True)),
                ('percent_of_adq', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('bnf_code', models.CharField(
                    max_length=11, primary_key=True,
                    serialize=False, validators=[
                        django.core.validators.RegexValidator(
                            b'^[\\w]*$', code=b'Invalid name',
                            message=b'name must be alphanumeric')])),
                ('name', models.CharField(max_length=200)),
                ('is_generic', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='QOFPrevalence',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('indicator_group', models.CharField(max_length=10)),
                ('register_description', models.CharField(max_length=100)),
                ('disease_register_size', models.IntegerField()),
                ('pct', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.PCT')),
                ('practice', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='frontend.Practice')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('bnf_id', models.CharField(
                    max_length=8,
                    primary_key=True,
                    serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('number_str', models.CharField(max_length=12)),
                ('bnf_chapter', models.IntegerField()),
                ('bnf_section', models.IntegerField(blank=True, null=True)),
                ('bnf_para', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['bnf_id'],
            },
        ),
        migrations.CreateModel(
            name='SHA',
            fields=[
                ('code', models.CharField(
                    help_text=b'Strategic health authority code',
                    max_length=3, primary_key=True, serialize=False)),
                ('ons_code', models.CharField(
                    blank=True, max_length=9, null=True)),
                ('name', models.CharField(
                    blank=True, max_length=200, null=True)),
                ('boundary',
                 django.contrib.gis.db.models.fields.MultiPolygonField(
                    blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='sha',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='frontend.SHA'),
        ),
        migrations.AddField(
            model_name='practice',
            name='area_team',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='frontend.SHA'),
        ),
        migrations.AddField(
            model_name='practice',
            name='ccg',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='frontend.PCT'),
        ),
        migrations.AddField(
            model_name='pct',
            name='managing_group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='frontend.SHA'),
        ),
        migrations.AddField(
            model_name='measurevalue',
            name='pct',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='frontend.PCT'),
        ),
        migrations.AddField(
            model_name='measurevalue',
            name='practice',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='frontend.Practice'),
        ),
        migrations.AlterUniqueTogether(
            name='chemical',
            unique_together=set([('bnf_code', 'chem_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='practiceisdispensing',
            unique_together=set([('practice', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='measurevalue',
            unique_together=set(
                [('measure', 'practice', 'month'),
                 ('measure', 'pct', 'practice', 'month')]),
        ),
        migrations.AlterUniqueTogether(
            name='measureglobal',
            unique_together=set([('measure', 'month')]),
        ),
    ]
