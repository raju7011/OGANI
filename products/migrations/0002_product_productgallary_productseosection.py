# Generated by Django 2.2.2 on 2021-10-06 10:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('selling_price', models.IntegerField()),
                ('marked_price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('stock', models.CharField(max_length=255)),
                ('shipping_time', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('cover_image', models.FileField(upload_to='products/cover~_image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSeoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_tite', models.CharField(max_length=255)),
                ('seo_description', models.TextField()),
                ('seo_keywords', models.CharField(max_length=2500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='products/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
