# Generated by Django 3.1.5 on 2021-02-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitation', '0005_auto_20210207_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitation',
            name='enviado_por',
            field=models.UUIDField(null=True),
        ),
    ]
