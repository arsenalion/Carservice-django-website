# Generated by Django 4.1.3 on 2022-12-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('car_owner', models.CharField(max_length=100)),
                ('car_notes', models.CharField(max_length=100)),
                ('car_number', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('service_type', models.CharField(blank=True, choices=[('P', 'Platinum'), ('G', 'Gold')], max_length=1)),
                ('year_old', models.IntegerField(null=True)),
                ('submission_date', models.DateTimeField()),
                ('services', models.ManyToManyField(blank=True, to='servicing.service')),
            ],
        ),
    ]
