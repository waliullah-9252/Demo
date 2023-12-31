# Generated by Django 4.2.7 on 2023-12-13 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=200)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
            ],
        ),
    ]
