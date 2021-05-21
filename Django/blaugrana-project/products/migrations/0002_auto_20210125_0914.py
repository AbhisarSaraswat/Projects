# Generated by Django 2.2.17 on 2021-01-25 09:14

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=products.models.get_image_filename, verbose_name='Image')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
