from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields

class AssetCategory(models.Model):
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
    
    class Meta:
        verbose_name_plural = "Asset categories"
    
    def __str__(self):
        return self.name


class RegulatoryFramework(models.Model):
    class FrameworkName(models.TextChoices):
        HIPAA = ("HIPAA", _("Health Insurance Portability and Accountability Act"))
        GDPR = ("GDPR", _("General Data Protection Regulation"))
        CCPA = ("CCPA", _("California Consumer Privacy Act"))
        PCIDSS = ("PCIDSS", _("Payment Card Industry Data Security Standard"))
        FedRAMP = ("FEDRAMP", _("Federal Risk and Authorization Management Program"))
        SOX = ("SOX", _("Sarbanes–Oxley Act"))
        NYDFS = ("NYDFS", _("New York State Department of Financial Services"))
        CMMC =  ("CMMC", _("Cybersecurity Maturity Model Certification"))
        
    title = models.CharField(
        max_length = 10,
        choices = FrameworkName.choices,
        default=FrameworkName.HIPAA
    )
    framworks = {"HIPAA": "Health Insurance Portability and Accountability Act", 
                 "GDPR": "General Data Protection Regulation",
                 }
    #short_description = framworks.get(title)
    
    short_description = models.CharField(
        #blank = True, null=True,
        default = framworks.get(title)
        ) 
    
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}: {self.short_description}"
        
class Risk(models.Model):
    class RiskName(models.TextChoices):
        A012025 = ("A012025", _("Broken Access Control"))
        A022025 = ("A022025", _("Cryptographic Failures"))
        A032025 = ("A032025", _("Injection")) 
        A042025 = ("A042025", _("Insecure Design"))
        A052025 = ("A052025", _("Security Misconfiguration"))
        A062025 = ("A062025", _("Vulnerable and Outdated Components"))
        A072025 = ("A072025", _("Identification and Authentication Failures"))
        A082025 = ("A082025", _("Software and Data Integrity Failures"))
        A092025 = ("A092025", _("Security Logging and Monitoring Failures")) 
        A102025 = ("A102025", _("Server-Side Request Forgery - SSRF"))
        
    name = models.CharField(
        max_length = 10,
        choices = RiskName.choices,
        default=RiskName.A012025
    )
    
    risks = {
        "A012021": "Broken Access Control", 
        "A022025": "Cryptographic Failures",
        "A032025": "Injection",
        "A042025" : "Insecure Design"
        }
    
    #short_description = framworks.get(title)
    
    short_description = models.CharField(
        #blank = True, null=True,
        default = risks.get(name)
        ) 
    
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}: {self.short_description}"

class Vendor(models.Model):
    class Country(models.TextChoices):
        USA = ("USA", _("United State of America"))
        CAN = ("CAN", _("Canada"))
        UK = ("UK", _("United Kingdom"))
        FR = ("FR", _("France"))
        
    class State(models.TextChoices):
        NJ = ("NJ", _("New Jersey"))
        NY = ("NY", _("New York"))
        CA = ("CA", _("California"))
        NC = ("NC", _("North Carolina"))
        ND = ("ND", _("North Dakota"))
        OH = ("OH", _("Ohio"))
        OK = ("OK", _("Oklahoma"))
        
           
    name = models.CharField(max_length=126)
    addressline1 = models.CharField(null=True, blank=True)
    addressline2 = models.CharField(null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    
    country = models.CharField(
        max_length = 3,
        choices = Country.choices,
        default=Country.USA
    )
    
    state = models.CharField(
        max_length = 3,
        choices = State.choices,
        default=State.NY
    )
    
    def __str__(self):
        return self.name
    
class Asset(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        YEN = ("JPY", _("Yen"))
        
    name = models.CharField(max_length=512)
    description = models.TextField(null=True, blank=True)
    aka = models.CharField(max_length=512)
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.CharField(
        max_length=3,
        choices = Currency.choices,
        default=Currency.AMERICAN_DOLLAR,
    )
    
    #product_variation_ids = PostgresFields.ArrayField(
        #models.IntegerField(null=True, blank=True)
    #)
    
    regulatoryFrameworks = models.ManyToManyField(RegulatoryFramework, related_name="assets", blank=True)
    risks = models.ManyToManyField(Risk, related_name="assets", blank=True)
    
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    
    category = models.ForeignKey(
        AssetCategory,
        on_delete=models.SET_NULL,
        related_name="assets",
        #related_name="children_products",
        blank=True,
        null=True,
    )
    
    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.category}, {self.vendor}"
  
    
class AssetInline(admin.TabularInline):  # or admin.StackedInline for a different layout admin.TabularInline
    model = Asset
    #extra = 1  # Number of empty product forms to display
    fields = ['name', 'vendor', 'category']  # Specify fields to display
    readonly_fields = ['name', 'vendor','category']  # Make certain fields read-only


@admin.register(AssetCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [AssetInline]

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    filter_horizontal = ('regulatoryFrameworks','risks',)
       

