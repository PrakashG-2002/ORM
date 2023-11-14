# Generated by Django 4.2.7 on 2023-11-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Player_Name', models.CharField(max_length=50)),
                ('Jersy_No', models.IntegerField()),
                ('Team', models.CharField(max_length=20)),
                ('Height', models.IntegerField()),
                ('Position', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]