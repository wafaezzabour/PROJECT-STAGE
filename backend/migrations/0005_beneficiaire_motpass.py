# Generated by Django 3.2.3 on 2022-06-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_demande_beneficiaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiaire',
            name='motpass',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]
