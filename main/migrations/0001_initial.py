# Generated by Django 4.1 on 2022-10-03 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('address', models.TextField()),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('bid_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_bids', models.IntegerField(default=0)),
                ('total_likes', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(default=datetime.datetime(2022, 10, 4, 0, 43, 3, 806142))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2022, 10, 7, 0, 43, 3, 806142))),
                ('price', models.IntegerField()),
                ('status', models.CharField(default='Live', max_length=10)),
                ('buyer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.buyer')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('address', models.TextField()),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('sell_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.buyer')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seller'),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('bid_time', models.DateTimeField(default=datetime.datetime(2022, 10, 4, 0, 43, 3, 807144))),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.buyer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=25, unique=True)),
                ('type', models.CharField(default='Buyer', max_length=6)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
