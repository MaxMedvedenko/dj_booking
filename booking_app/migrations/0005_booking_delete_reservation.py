# Generated by Django 5.0.2 on 2024-03-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0004_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=20)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
