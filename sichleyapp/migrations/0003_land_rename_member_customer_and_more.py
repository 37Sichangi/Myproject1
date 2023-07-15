# Generated by Django 4.1.7 on 2023-03-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sichleyapp', '0002_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=1500)),
                ('soil_type', models.CharField(max_length=550)),
                ('land_shape', models.CharField(max_length=233)),
                ('land_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Member',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='countyname',
            new_name='county_name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='subcountyname',
            new_name='nearest_Town',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='regionname',
            new_name='region_name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='wardname',
            new_name='subcounty_name',
        ),
        migrations.AddField(
            model_name='region',
            name='ward_name',
            field=models.CharField(default='Kibabii', max_length=233),
        ),
    ]