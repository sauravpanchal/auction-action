# Generated by Django 4.1 on 2022-09-05 11:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 17, 14, 10, 59871)),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 8, 17, 14, 10, 58871)),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 17, 14, 10, 58871)),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_bids',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wishlistitem',
            name='buyer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.buyer'),
        ),
    ]