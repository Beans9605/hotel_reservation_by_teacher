# Generated by Django 3.0.7 on 2020-06-26 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('how_many_accept', models.IntegerField(default=2)),
                ('discription', models.TextField()),
                ('price', models.IntegerField(default=50000)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_start_day', models.DateField(auto_now=True)),
                ('reservation_end_day', models.DateField(auto_now=True)),
                ('reservation_request_day', models.DateField(auto_now_add=True)),
                ('night_num', models.IntegerField(default=1)),
                ('users_num', models.IntegerField(default=2)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Room')),
            ],
        ),
    ]