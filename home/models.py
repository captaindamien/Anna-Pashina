from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    subpage_types = ['NewPage']
    
    # main_title = models.CharField(
    #     max_length=200,
    #     blank=True,
    #     null=True,
    #     verbose_name='Заглавный встречающий текст',
    # )
    # sub_title = models.CharField(
    #     max_length=200,
    #     blank=True,
    #     null=True,
    #     verbose_name='Дополнительный встречающий текст',
    # )
    # main_photo = models.ImageField(
    #     upload_to = 'images/',
    #     blank = True,
    #     null = True,
    #     verbose_name = 'Изображение для окончания турнира'
    # )
    
    

class NewPage(Page):    
    parent_page_types = ['HomePage']
    # template = 'home/new_style/index.html'
    
    title_field = models.CharField(
        max_length=200,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('title_field')
    ]
