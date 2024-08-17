# Generated by Django 4.2 on 2024-08-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_alter_link_table_result_of_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link_table',
            name='result_of_class',
            field=models.CharField(choices=[('studing', 'در حال تحصیل'), ('pass', 'قبول'), ('fail', 'مردود')], default='studing', max_length=30),
        ),
    ]
