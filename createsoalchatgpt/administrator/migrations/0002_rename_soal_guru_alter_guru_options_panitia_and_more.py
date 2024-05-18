# Generated by Django 5.0.5 on 2024-05-12 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Soal',
            new_name='Guru',
        ),
        migrations.AlterModelOptions(
            name='guru',
            options={'verbose_name_plural': 'Data Guru'},
        ),
        migrations.CreateModel(
            name='Panitia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengguna', models.CharField(blank=True, max_length=200, null=True)),
                ('alamat', models.TextField(blank=True, null=True, verbose_name='Alamat Panitia')),
                ('nik', models.CharField(blank=True, max_length=100, null=True)),
                ('no_hp', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Panitia',
            },
        ),
        migrations.DeleteModel(
            name='Jadwal',
        ),
    ]
