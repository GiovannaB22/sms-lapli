# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('commune', models.CharField(unique=True, max_length=45, verbose_name='Commune')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name='Code')),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('departement', models.CharField(max_length=40, verbose_name='Departement')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name='Code')),
            ],
        ),
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nomPersonne', models.CharField(max_length=45, verbose_name='Nom')),
                ('prenomPersonne', models.CharField(max_length=45, verbose_name='Prenom')),
                ('telephoneBureau', models.CharField(blank=True, max_length=45, verbose_name='Telephone (Bureau)')),
                ('telephonePersonnel', models.CharField(unique=True, max_length=45, verbose_name='Telephone (Personnel)')),
                ('emailPersonnel', models.CharField(blank=True, max_length=45, verbose_name='Email (Personnel)')),
                ('adressePersonnelle', models.CharField(blank=True, max_length=45, verbose_name='Adresse (Personnlle)')),
                ('nif', models.CharField(unique=True, max_length=45, verbose_name='NIF/CIN')),
                ('dateEmbauche', models.DateField(verbose_name="Date d'embauche")),
                ('isactif', models.BooleanField(verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nomPoste', models.CharField(verbose_name='Poste', unique=True, max_length=45, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=45, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='SectionCommunale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sectionCommunale', models.CharField(max_length=45, verbose_name='Section Communale')),
                ('nomOfficiel', models.CharField(blank=True, max_length=45, verbose_name='Nom officiel')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('id_code', models.CharField(unique=True, max_length=7, verbose_name='Code')),
                ('commune', models.ForeignKey(to='base.Commune', verbose_name='Commune')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('localite', models.CharField(max_length=45, verbose_name='Localite')),
                ('latitude', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Latitude', default=0)),
                ('longitude', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Longitude', default=0)),
                ('hauteur', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Hauteur', default=0)),
                ('sectionCommunale', models.ForeignKey(to='base.SectionCommunale', verbose_name='Section Communale')),
            ],
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='nomPoste',
            field=models.ForeignKey(to='base.Poste', verbose_name='Poste'),
        ),
        migrations.AddField(
            model_name='commune',
            name='departement',
            field=models.ForeignKey(to='base.Departement', verbose_name='Departement'),
        ),
    ]
