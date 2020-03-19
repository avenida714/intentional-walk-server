# Generated by Django 3.0.3 on 2020-03-19 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('account_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('zip', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='IntentionalWalk',
            fields=[
                ('event_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('steps', models.IntegerField()),
                ('appuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.AppUser')),
            ],
            options={
                'ordering': ('-start',),
            },
        ),
        migrations.CreateModel(
            name='DailyWalk',
            fields=[
                ('event_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('steps', models.IntegerField()),
                ('appuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.AppUser')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
