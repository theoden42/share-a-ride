# Generated by Django 4.2 on 2024-05-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_initiator', models.CharField(max_length=100)),
                ('src_location', models.CharField(max_length=100)),
                ('dst_location', models.CharField(max_length=100)),
                ('total_fare', models.IntegerField()),
                ('num_passengers', models.IntegerField()),
                ('start_datetime', models.DateTimeField()),
            ],
        ),
    ]
