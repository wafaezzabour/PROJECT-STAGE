# Generated by Django 3.2.3 on 2022-06-23 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20220623_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('cin', models.CharField(max_length=10)),
                ('adresse', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('handicap', models.CharField(choices=[('Moteur', 'Moteur'), ('Mental', 'Mental'), ('Visuel', 'Visuel'), ('Auditif', 'Auditif')], max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='demande',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='cin',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='handicap',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='telephone',
        ),
        migrations.AddField(
            model_name='demande',
            name='beneficiaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.beneficiaire'),
            preserve_default=False,
        ),
    ]
