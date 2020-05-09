# Generated by Django 3.0.6 on 2020-05-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('fiscalData', models.TextField()),
                ('activityDomain', models.CharField(max_length=50)),
                ('revenueId', models.IntegerField()),
            ],
        ),
    ]
