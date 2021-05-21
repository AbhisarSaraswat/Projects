# Generated by Django 2.2.17 on 2021-01-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('type', models.CharField(max_length=250)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
