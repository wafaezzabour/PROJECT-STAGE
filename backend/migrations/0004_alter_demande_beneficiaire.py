# Generated by Django 3.2.3 on 2022-06-23 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20220623_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='beneficiaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.beneficiaire'),
        ),
    ]
