# Generated by Django 4.2 on 2024-08-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klass',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
