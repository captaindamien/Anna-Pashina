# Generated by Django 4.1.5 on 2023-04-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_about_me_about_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='product_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок услуг'),
        ),
    ]
