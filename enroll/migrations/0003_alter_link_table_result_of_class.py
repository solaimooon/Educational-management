# Generated by Django 4.2 on 2024-08-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_klass_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link_table',
            name='result_of_class',
            field=models.BooleanField(choices=[('studing', 'در حال تحصیل'), ('pass', 'قبول'), ('fail', 'مردود')], default='studing'),
        ),
    ]
