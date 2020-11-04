# Generated by Django 3.1.2 on 2020-11-03 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fireStationApp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('leaving_time', models.DateTimeField(auto_now_add=True)),
                ('reaching_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2000)),
                ('pin', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('reporting_date', models.DateField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='complainer_id',
        ),
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='Complainer',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.AddField(
            model_name='complaint',
            name='reporter_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fireStationApp1.reporter'),
        ),
        migrations.AddField(
            model_name='act',
            name='complaint_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fireStationApp1.complaint'),
        ),
        migrations.AddField(
            model_name='act',
            name='staff_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fireStationApp1.staff'),
        ),
        migrations.AddField(
            model_name='act',
            name='vehicle_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fireStationApp1.vehicle'),
        ),
    ]
