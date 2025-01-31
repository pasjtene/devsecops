from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields

class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete = models.CASCADE
    )
    
    def __STR__(self):
        return self.name
# Create your models here.

class Product(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish_crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        YEN = ("JPY", _("Yen"))
        
    name = models.CharField(max_length=512)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.CharField(
        max_length=3,
        choices = Currency.choices,
    )

    def __STR__(self):
        return self.name