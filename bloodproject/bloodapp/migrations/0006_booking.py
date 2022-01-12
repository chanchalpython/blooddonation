# Generated by Django 3.2.11 on 2022-01-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0005_delete_bgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('age', models.IntegerField()),
                ('address', models.TextField(blank=True)),
                ('bgroup', models.CharField(max_length=250)),
                ('mob', models.IntegerField()),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
    ]
