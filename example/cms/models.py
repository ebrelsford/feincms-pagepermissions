from django.utils.translation import ugettext_lazy as _

from feincms.content.richtext.models import RichTextContent
from feincms.module.page.models import Page


Page.register_extensions(
    'pagepermissions.extension'
)

Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
        ('main', _('Main content area')),
    ),
})

Page.create_content_type(RichTextContent)
