# Generated by Django 4.0.2 on 2022-04-14 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_brand_buyer_maincategory_seller_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
