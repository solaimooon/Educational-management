# Generated by Django 4.2 on 2024-10-07 21:07

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0006_remove_presence_absence_was_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sum_emtiyazat',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date_for', django_jalali.db.models.jDateField()),
                ('sumed_emtiyaz', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'sum_emtiyazat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SUM_final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SUM', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'SUM_final',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='presence_absence',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='presence_absence',
            name='was_or_not_or',
            field=models.CharField(choices=[('present', 'حاضر'), ('absent_unwarranted', 'غایب/غیر موجه'), ('absent_warranted', 'غایب/موجه')], default='null', max_length=50),
            preserve_default=False,
        ),
    ]
