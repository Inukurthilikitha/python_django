# Generated by Django 3.1.6 on 2021-02-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('added_date', models.DateField()),
                ('added_by', models.CharField(max_length=264)),
            ],
        ),
    ]
