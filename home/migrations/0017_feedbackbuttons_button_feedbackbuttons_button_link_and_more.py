# Generated by Django 4.1.5 on 2023-04-17 23:42

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_advantage_adv_advantage_adv_image_advantage_adv_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackbuttons',
            name='button',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buttons_block', to='home.homepage'),
        ),
        migrations.AddField(
            model_name='feedbackbuttons',
            name='button_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='feedbackbuttons',
            name='button_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст кнопки'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='feedback_text',
            field=wagtail.fields.RichTextField(blank=True, help_text='Введите текст', null=True, verbose_name='Описание Обратной связи'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='feedback_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок Обратной связи'),
        ),
    ]
