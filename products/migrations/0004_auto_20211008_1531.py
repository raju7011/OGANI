# Generated by Django 2.2.2 on 2021-10-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211006_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productseosection',
            name='seo_tite',
            field=models.CharField(max_length=500),
        ),
    ]
