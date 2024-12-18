# Generated by Django 4.2.7 on 2024-11-24 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
                ('processing_progress', models.FloatField(default=0)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('results_data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('vehicle_type', models.CharField(choices=[('car', 'Car'), ('truck', 'Truck'), ('bus', 'Bus'), ('motorcycle', 'Motorcycle'), ('bicycle', 'Bicycle')], max_length=50)),
                ('confidence', models.FloatField(default=0.0)),
                ('bbox_x1', models.FloatField()),
                ('bbox_y1', models.FloatField()),
                ('bbox_x2', models.FloatField()),
                ('bbox_y2', models.FloatField()),
                ('count', models.IntegerField(default=0)),
                ('frame_number', models.IntegerField(default=0)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic_analyzer.videoanalysis')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='DetectionZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coordinates', models.JSONField()),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic_analyzer.videoanalysis')),
            ],
        ),
    ]
