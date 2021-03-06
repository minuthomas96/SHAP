# Generated by Django 2.2 on 2020-11-04 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shap1app', '0002_auto_20201104_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_id', models.CharField(blank=True, max_length=10)),
                ('prod_name', models.CharField(blank=True, max_length=100)),
                ('prod_image', models.FileField(upload_to='')),
                ('prod_category', models.CharField(blank=True, max_length=100)),
                ('prod_subcategory', models.CharField(blank=True, max_length=100)),
                ('prod_price', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('stock_balance', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=10)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shap1app.product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shap1app.product')),
            ],
        ),
    ]
