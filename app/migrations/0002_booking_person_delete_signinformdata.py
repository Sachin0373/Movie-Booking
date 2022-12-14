# Generated by Django 4.0.4 on 2022-07-28 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Phno', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=30)),
                ('Number_of_people', models.IntegerField()),
                ('Date_of_Movie', models.DateField(blank=True, null=True)),
                ('Booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.booking')),
            ],
        ),
        migrations.DeleteModel(
            name='SignInformdata',
        ),
    ]
