from PIL import Image
from django.db import models
from django.utils.html import format_html

from helper.models import get_slug, upload_image


class Rase(models.Model):
    title = models.CharField("Название", max_length=25)

    def rase_ico_upload_to(self, filename):
        return upload_image(self, 'ico', filename)

    ico = models.ImageField("Иконка", upload_to=rase_ico_upload_to)
    sort = models.PositiveSmallIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Раса'
        verbose_name_plural = 'Расы'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return get_slug(self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.ico.path)
            size = 24
            if img.height > size or img.width > size:
                output_size = (size, size)
                img.thumbnail(output_size)
                img.save(self.ico.path)
        except Image.UnidentifiedImageError:
            pass

    def get_ico(self):
        img = f"<img src='{self.ico.url}' title='{self.title}' width='20px'>"
        return format_html(img)

    get_ico.short_description = "Иконка"
