# Generated by Django 4.0.2 on 2022-04-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_buyer_date_seller_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='user_status',
            field=models.CharField(default='Buyer', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='user_status',
            field=models.CharField(default='Buyer', max_length=20),
            preserve_default=False,
        ),
    ]
