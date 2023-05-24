from django.db import models

from wagtail.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField

from modelcluster.fields import ParentalKey

import numpy


class About(Orderable):
    about = ParentalKey(
        'HomePage',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='about_block',
    )
    about_text = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=' ',
    )


class Skills(Orderable):
    skills = ParentalKey(
        'HomePage',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='skills_block',
    )
    skills_text = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=' ',
    )


class Price(Orderable):
    price = ParentalKey(
        'HomePage',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='price_block',
    )
    price_text = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Описание',
    )
    price_count = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Цена',
    )


class Products(Orderable):
    products = ParentalKey(
        'HomePage',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='products_block',
    )
    product_text = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=' ',
    )
    
    
    
class Advantage(Orderable):
    adv = ParentalKey(
        'HomePage',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='adv_block',
    )
    adv_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Изображение',
    )  
    adv_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Заголовок',
    )
    adv_text = RichTextField(
        verbose_name='Описание',
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                  'ol', 'ul', 'hr', 'bold', 'italic',
                  'link', 'superscript', 'subscript',
                  'strikethrough', 'blockquote'],
        help_text='Введите текст',
        blank=True,
        null=True,
    )
    
    
class FeedbackButtons(Orderable):
    button = ParentalKey(
        'HomePage',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='buttons_block',
    )
    button_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Текст кнопки',
    )
    button_link = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Ссылка',
    )


class HomePage(Page):
    subpage_types = ['NewPage']
    
    main_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Заглавный текст главной страницы',
    )
    sub_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Дополнительный текст главной страницы',
    )
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Изображение главной страницы',
    )    
    products_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Заголовок услуг',
    )
    advantage_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Заголовок блока "Преимущества"',
    )    
    feedback_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Заголовок Обратной связи',
    )
    feedback_text = RichTextField(
        verbose_name='Описание Обратной связи',
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                  'ol', 'ul', 'hr', 'bold', 'italic',
                  'link', 'superscript', 'subscript',
                  'strikethrough', 'blockquote'],
        help_text='Введите текст',
        blank=True,
        null=True,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('main_title'),
        FieldPanel('sub_title'),
        FieldPanel('main_image'),
        MultiFieldPanel(
            [InlinePanel('about_block'),],
            heading='Блок "Обо мне"',
        ),
        MultiFieldPanel(
            [InlinePanel('skills_block'),],
            heading='Блок "Навыки"',
        ),
        MultiFieldPanel(
            [InlinePanel('price_block'),],
            heading='Услуги и цены',
        ),
        FieldPanel('products_title'),
        MultiFieldPanel(
            [InlinePanel('products_block'),],
            heading='Услуги и цены',
        ),
        FieldPanel('advantage_title'),
        MultiFieldPanel(
            [InlinePanel('adv_block'),],
            heading='Преимущества',
        ),
        FieldPanel('feedback_title'),
        FieldPanel('feedback_text'),
        MultiFieldPanel(
            [InlinePanel('buttons_block'),],
            heading='Кнопки обратной связи',
        ),        
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        products_list = numpy.array_split(Products.objects.all(), 2)
        
        context['products_left'] = products_list[0]
        context['products_right'] = products_list[1]
        
        return context     
    
    

class NewPage(Page):    
    parent_page_types = ['HomePage']
    # template = 'home/new_style/index.html'
    
    title_field = models.CharField(
        max_length=200,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('title_field')
    ]
