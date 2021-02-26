# Generated by Django 3.1.6 on 2021-02-25 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_userprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=256)),
                ('principal_name', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='first_app.schools')),
            ],
        ),
    ]