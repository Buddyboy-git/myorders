# Generated by Django 4.0.4 on 2022-04-20 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobber',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('company_name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('nickname', models.CharField(default='', max_length=10)),
                ('jobber_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.jobber')),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='thumanns_product_import',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemnum', models.CharField(default='', max_length=12)),
                ('description', models.TextField(default='', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('priceunit', models.CharField(default='', max_length=4)),
                ('pickunit', models.CharField(default='', max_length=4)),
                ('avgweight', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='uom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=4)),
                ('name', models.TextField(default='', max_length=30)),
                ('default_nickname', models.CharField(default='', max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='store_history',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('jobber_company_name', models.CharField(default='', max_length=30)),
                ('product_default_uom_code', models.CharField(default='', max_length=4)),
                ('product_default_uom_nickname', models.CharField(default='', max_length=4)),
                ('supplier_name', models.CharField(default='', max_length=30)),
                ('product_itemnum', models.CharField(default='', max_length=12)),
                ('product_name', models.CharField(default='', max_length=30)),
                ('product_description', models.TextField(default='', max_length=80)),
                ('product_nickname', models.CharField(default='', max_length=10, unique=True)),
                ('store_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.store')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('itemnum', models.CharField(default='', max_length=12)),
                ('name', models.CharField(default='', max_length=30)),
                ('description', models.TextField(default='', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('priceunit', models.CharField(default='', max_length=4)),
                ('pickunit', models.CharField(default='', max_length=4)),
                ('avgweight', models.FloatField(default=0)),
                ('supplier_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
    ]