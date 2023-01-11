from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    subpage_types = ['NewPage']
    

class NewPage(Page):    
    parent_page_types = ['HomePage']
    landing_page_template = 'home/new_style/index.html',
    
    title_field = models.CharField(
        max_length=200,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('title_field')
    ]
