# Generated by Django 4.2 on 2024-07-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athentication', '0008_remove_extra_user_data_father_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra_user_data',
            name='type',
            field=models.CharField(blank=True, choices=[('اوپراتور', 'operator '), ('معلم', 'teacher '), ('student', 'دانش اموز'), ('free student', 'مستمع آزاد')], default='free student', max_length=50, null=True),
        ),
    ]
