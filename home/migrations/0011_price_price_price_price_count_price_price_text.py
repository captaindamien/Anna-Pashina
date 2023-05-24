# Generated by Django 4.1.5 on 2023-04-17 04:52

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_advantage_feedbackbuttons_price_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='price',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_block', to='home.homepage'),
        ),
        migrations.AddField(
            model_name='price',
            name='price_count',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='price',
            name='price_text',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
