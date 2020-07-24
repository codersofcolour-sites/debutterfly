from django.db import models


from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.embeds.finders.base import EmbedFinder
from wagtail.core.blocks import RawHTMLBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks


from streams import blocks


class FlexPage(Page):
    """Flexible page class."""

    template = "flex/flex_page.html"
    # embed = EmbedBlock

    content = StreamField(
        [   
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
            ("embed_block", EmbedBlock()),
            ("html_block", blocks.RawHTMLBlock()),
            ("image_chooser_block", ImageChooserBlock()),
            ("cards", blocks.CardBlock()),
            ("carousel_images", blocks.CarouselImages()),
           
        ],
        null=True,
        blank=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),  
    ]

    class Meta: # noqa
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"