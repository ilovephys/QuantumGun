# Generated by Django 3.1.4 on 2020-12-26 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0002_auto_20201219_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contentDescription', models.TextField(max_length=150)),
                ('postdate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now=True)),
                ('category', models.CharField(choices=[('Python', 'Python'), ('Django', 'Django'), ('DataScience', 'DataScience'), ('FIRE', 'FIRE'), ('Education', 'Education'), ('PythonHuck', 'PythonHuck'), ('MathPhys', 'MathPhys'), ('Other', 'Other')], max_length=50)),
                ('eyeCatch', models.ImageField(blank=True, null=True, upload_to='static/img', verbose_name='アイキャッチ画像')),
                ('pageView', models.PositiveIntegerField(default=0)),
                ('content', models.TextField()),
                ('link', models.PositiveIntegerField(blank=True, null=True)),
                ('content2', models.TextField(blank=True, null=True)),
                ('link2', models.PositiveIntegerField(blank=True, null=True)),
                ('content3', models.TextField(blank=True, null=True)),
                ('link3', models.PositiveIntegerField(blank=True, null=True)),
                ('content4', models.TextField(blank=True, null=True)),
                ('link4', models.PositiveIntegerField(blank=True, null=True)),
                ('content5', models.TextField(blank=True, null=True)),
                ('link5', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
