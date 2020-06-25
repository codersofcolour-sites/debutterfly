from django.db import models
from wagtail.core import blocks

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""
    
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    # caption = models.CharField(max_length=225, blank=True, null=True)

    panels = [
        ImageChooserPanel("carousel_image"),
        # FieldPanel("caption"),
    ]

class HomePage(Page):

    templates = "home/home_page.html"

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

  
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('body', classname="full"),
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading="Banner Options"),
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5, min_num=1,label="Image"),
        ], heading="Carousel Images"),
        StreamFieldPanel("content"),
    ]

    body = RichTextField(blank=True)


class Meta:

    verbose_name = "Home Page"
    verbose_name_plural = "Home Pages"