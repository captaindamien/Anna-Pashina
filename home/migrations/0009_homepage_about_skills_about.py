# Generated by Django 4.1.5 on 2023-04-17 04:17

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_slide_image_homepage_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавный текст главной страницы'),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('skills_text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Блок навыков')),
                ('my_skills', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills_block', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('about_text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Блок обо мне')),
                ('about_me', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_block', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
