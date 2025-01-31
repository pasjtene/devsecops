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
    
    def __str__(self):
        return self.name
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=126)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        YEN = ("JPY", _("Yen"))
        
    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512)
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.CharField(
        max_length=3,
        choices = Currency.choices,
        default=Currency.AMERICAN_DOLLAR,
    )
    
    product_variation_ids = PostgresFields.ArrayField(
        models.IntegerField(null=True, blank=True)
    )
    
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    
    category = models.ForeignKey(
        ProductCategory,
        #on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    
    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.subtitle}, {self.vendor}"