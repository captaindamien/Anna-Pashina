# Generated by Django 4.1.5 on 2023-01-11 03:48

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='opener_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='opener_text',
            field=wagtail.fields.RichTextField(blank=True, help_text='Введите текст', null=True, verbose_name='Текст заглавного блока'),
        ),
    ]
