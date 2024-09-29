# Generated by Django 4.2 on 2024-08-30 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enroll', '0005_level_class_klass_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avalable', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('method', models.CharField(choices=[('kosha_ravankhani', 'kosha_ravankhani'), ('kosha_tajvid', 'kosha_tajvid'), ('noramal', 'noramal')], max_length=50)),
                ('enroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.link_table')),
            ],
        ),
        migrations.CreateModel(
            name='presence_absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('was', models.BooleanField()),
                ('enroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.link_table')),
            ],
        ),
        migrations.CreateModel(
            name='amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.score')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='score.type')),
            ],
        ),
    ]
