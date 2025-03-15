from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields
from django.contrib.auth.models import User, auth
from security.models import SecurityManagementFramework, SecurityManagementRequirement, Framework

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



class SecurityRequirement(models.Model):
    class RequirementList(models.TextChoices):
        # FISMA https://security.cms.gov/learn/federal-information-security-modernization-act-fisma
        # PCIDSS https://pcidssguide.com/pci-dss-requirements/
        PCIDSSR1 = ("PCIDSSR1", _("Configure and use firewalls to protect cardholder data"))
        PCIDSSR11 = ("PCIDSSR11", _("Create and implement standards for configuration of firewalls and routers"))
        PCIDSSR12 = ("PCIDSSR12", _("Create a firewall and router configuration that restricts connections betweenuntrusted networks and all system components in the cardholder data environment")) 
        PCIDSSR13 = ("PCIDSSR13", _("Restrict direct global access to any system component of the cardholder data medium over the internet."))
        PCIDSSR14 = ("PCIDSSR14", _("Install personal firewall software on all mobile devices that are connected to the internet and used to access the network when they are out of the network"))
        PCIDSSR15 = ("PCIDSSR15", _("Make sure that security policies and operational procedures for managing firewalls are documented, in use, and known to all affected parties"))
        PCIDSSR2 = ("PCIDSSR2", _("Do not use the vendor’s default settings for system passwords and other security parameters"))
        PCIDSSR21 = ("PCIDSSR21", _("Always change the default settings and values ​​provided by the manufacturer and remove or disable unnecessary default accounts before installing any system on the network"))
        PCIDSSR22 = ("PCIDSSR22", _("Create configuration standards for all components of the system")) 
        PCIDSSR23 = ("PCIDSSR23", _("Encrypt all non-console administrative access to devices using strong encryption"))
        FISMAR1 = ("FISMAR1", _("Implement continuous monitoring"))
        FISMAR2 = ("FISMAR2", _("Conduct annual security reviews"))
        FISMAR3 = ("FISMAR3", _("Perform risk assessment"))
        FISMAR4 = ("FISMAR4", _("Document the controls in the system security plan"))
        FISMAR5 = ("FISMAR5", _("Meet baseline security controls"))
        FISMAR6 = ("FISMAR6", _("Perform system risk categorization"))
        # https://www.itgovernance.eu/blog/en/summary-of-the-gdprs-10-key-requirements#International-data-transfers
        # https://gdpr-info.eu/art-35-gdpr/
        GDPR1 = ("GDPR1", _("Lawful, fair and transparent processing: - The first GDPR data protection principle (in Article 5) mandates that organisations document a lawful basis, such as legitimate interest or consent, for processing personal data."))
        GDPR2 = ("GDPR2", _("Limitation of purpose, data and storage: -The second, third and fifth GDPR data protection principles reflect another key tenet of the Regulation: that you minimise your personal data collection and processing"))
        GDPR3 = ("GDPR3", _("Data accuracy, integrity and confidentiality: -You must ensure that personal data you hold is accurate and complete, otherwise it’s not fit for purpose."))
        GDPR4 = ("GDPR4", _("Data protection impact assessment - DPIA: Article 35(3)"))
        GDPR5 = ("GDPR5", _("Privacy by design - GDPR Article 25"))
        GDPR6 = ("GDPR6", _("A Contract is established between data Controller and data processor- GDPR Article 28"))
        GDPR7 = ("GDPR7", _("Data subject rights: GDPR Chapter III (Articles 12–22) -The right to be informed, -The right of access, -The right to rectification, -The right to erasure, -The right to restrict processing, -The right to data portability, -The right to object, -Rights in relation to automated decision-making, including profiling"))
        GDPR8 = ("GDPR8", _("Data protection officer: The requirements for a DPO, including when to appoint one are laid out in Articles 37–39"))
        GDPR9 = ("GDPR9", _("International data transfers- The scope of GDPR is limited to organisations based or operating in the EU. Chapter V (Articles 44–50) restricts international data transfers outside the EEA, unless appropriate safeguards are in place."))
        GDPR10 = ("GDPR10", _("Personal data breach reporting: - the GDPR (Article 33) requires the data controller to report any data breach to its supervisory authority within 72 hours of becoming aware of the breach"))
        #https://www.simplepractice.com/resource/hipaa-compliance-checklist/
        HIPAA1 = ("HIPAA1",_("Appoint an individual or individuals within your practice to oversee HIPAA compliance efforts—generally known as a Privacy Officer or Security Officer. Depending on your business structure, you may take this responsibility yourself."))
        HIPAA2 = ("HIPAA2",_("Create policies and procedures to ensure HIPAA compliance (for example, email procedures, PHI data storage procedures)."))
    
    name = models.CharField(
        max_length = 15,
        choices = RequirementList.choices,
        default=RequirementList.PCIDSSR15
    )
    
    secRequirements = {               
        "PCIDSSR2": "Do not use the vendors default settings for system passwords and other security parameters",
        "PCIDSSR21": "Always change the default settings and values ​​provided by the manufacturer and remove or disable unnecessary default accounts before installing any system on the network",
        "PCIDSSR22": "Create configuration standards for all components of the system", 
        "PCIDSSR23": "Encrypt all non-console administrative access to devices using strong encryption",
        }
    
    #short_description = framworks.get(title)
    
    short_description = models.CharField(
        #blank = True, null=True,
        default = secRequirements.get(name)
        ) 
    
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}: {self.short_description}"        

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
        FISMA =  ("FISMA", _("Federal Information Security Modernization Act"))
        
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
    securityRequirements = models.ManyToManyField(SecurityRequirement, related_name="regulatoryFrameworks", blank=True)
    
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
        "A042025" : "Insecure Design",
        "A052025" : "Security Misconfiguration",
        }
    
    #short_description = framworks.get(title)
    
    short_description = models.CharField(
        #blank = True, null=True,
        default = risks.get(name)
        ) 
    
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}: {self.short_description}"

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
    """
    Represents any asset that can be managed. Compliance, Security and Risk framework are assigned to assets.
    Assets can be of many types, Including people, process, data, hardware, software and more. Assets can also be classified 
    in categories.
    
    Attributes:
        Type: type of Asset
        Category: Category of the asset
        regulatoryFrameworks: The compliance frameworks assigned to the asset. Many frameworks can be assigned to an asset
        SecurityManagementFrameworks: The security management framework assigned to an asset (e.g: ISO27001, NIST_CSF, NIST_SP 800-53)
        
    """
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        YEN = ("JPY", _("Yen"))
    
    IMPACT_LEVEL_CHOICES = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]
    
    class Impact_level(models.TextChoices):
        Low = ("Low", _("Low")) #Limited adverse effect in case of a compromise
        Moderate = ("Moderate", _("Moderate")) #Serious adverse effect in case of a compromise
        High = ("High", _("High")) #Severe adverse effect in case of a compromise
        Critical = ("critical", _("Critical")) #Catastrophic adverse effect in case of a compromise
    
    class Risk_status(models.TextChoices):
        Reduced = ("Reduced", _("Reduced")) #Controls have been implemented and the risk is reduced
        Mitigated = ("Mitigated", _("Mitigated")) #Controls have been implemented and the risk is - Mitigated
        Accepted = ("Accepted", _("Accepted")) #The risk is accepted. impact is manageable 
        Transfered = ("Transfered", _("Transfered")) #Risk is transfered to a third party
        Avoided = ("Avoided", _("Avoided")) #Asset is not used a a way that it can constitute any risk - Avoided
        Mitigating = ("Mitigating", _("Mitigating")) #Controls are being implemented - Mitigating
        Monitoring = ("Monitoring", _("Monitoring")) #Controls have been implemented and the risk is monitored
            
    name = models.CharField(max_length=512)
    description = models.TextField(null=True, blank=True)
    aka = models.CharField(max_length=512, null=True, blank=True)
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True
    )
    
    quantity = models.PositiveIntegerField(default=1)
    
    impact_level = models.CharField(
        max_length=12,
        choices = IMPACT_LEVEL_CHOICES,
        default="Moderate",
    )
    
    risk_status = models.CharField(
        max_length=10,
        choices = Risk_status.choices,
        default=Risk_status.Mitigating,
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
    SecurityManagementFrameworks = models.ManyToManyField(SecurityManagementFramework, related_name="assets", blank=True)
    framworks = models.ManyToManyField(Framework, related_name="assets", blank=True)
    
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
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.category}, {self.vendor}"


class RequirementAction(models.Model):
    """
    Represents an item of requirement status created by user for a  given requirement for a security framework assigned to an asset
    This is expected to create a large table, so may later be hosted as a microservice to serve only this purpose
    A similar separate entity is created for compliance frameworks in the asset module. The purpose of separation is to reduce table size.

    Attributes:
        asset: The aset for which this is created. automatically assigned
        framework: The compliance framework for which this is created
        requirement: An item of the list of requirements needed to achieve compliance
        ...
    """
    class CompletionStatus(models.TextChoices):
        Complete = ("Complete", _("Complete"))
        InProgress = ("InProgress", _("InProgress"))
        Canceled = ("Canceled", _("Canceled"))
        Paused = ("Paused", _("Paused"))
        
   
    COMPLETION_STATUS_CHOICES = [
        ('Complete', 'Complete'),
        ('InProgress', 'InProgress'),
        ('Canceled', 'Canceled'),
        ('Paused','Paused')
    ]
    description = models.CharField(max_length=100, default="Give a short description, framework and asset")
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        )
    
    
    framework_name = models.CharField(max_length=20)
    requirement_codename = models.CharField(max_length=20)
    requirement_id = models.IntegerField()
    framework_id = models.IntegerField()
    
    
    details = models.TextField(max_length=500) #give detail of the current compliance status of the requirement
    implementation_percent = models.PositiveIntegerField(
        default=0,
        null=True, blank=True,
    )
    
    completion_Status = models.CharField(
        max_length=12,
        choices=CompletionStatus.choices,
        default=CompletionStatus.InProgress
    )
    implementation_start_date = models.DateTimeField(null=True, blank=True)
    
    
    expected_completion_date = models.DateTimeField(null=True, blank=True)
    actual_implementation_date = models.DateTimeField(null=True, blank=True)
    
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="requirement_actions_owned"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="requirement_actions_assigned"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="requirement_actions_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description  


class RequirementStatus(models.Model):
    """
    Represents an item of requirement status created by user for a  given requirement for a security framework assigned to an asset
    This is expected to create a large table, so may later be hosted as a microservice to serve only this purpose
    A similar separate entity is created for compliance frameworks in the asset module. The purpose of separation is to reduce table size.

    Attributes:
        asset: The aset for which this is created. automatically assigned
        framework: The compliance framework for which this is created
        requirement: An item of the list of requirements needed to achieve compliance
        ...
    """
    class CompletionStatus(models.TextChoices):
        Complete = ("Complete", _("Complete"))
        InProgress = ("InProgress", _("InProgress"))
        Canceled = ("Canceled", _("Canceled"))
        Paused = ("Paused", _("Paused"))
        
   
    COMPLETION_STATUS_CHOICES = [
        ('Complete', 'Complete'),
        ('InProgress', 'InProgress'),
        ('Canceled', 'Canceled'),
        ('Paused','Paused')
    ]
    description = models.CharField(max_length=100, default="Give a short description, framework and asset")
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        )
    
    framework = models.ForeignKey(
        SecurityManagementFramework,
        on_delete=models.CASCADE
    )
    
    
    requirement = models.ForeignKey(
        SecurityManagementRequirement,
        on_delete=models.CASCADE,
        #related_name="requirement"
        )
    details = models.TextField(max_length=500) #give detail of the current compliance status of the requirement
    implementation_percent = models.PositiveIntegerField(
        default=0,
        null=True, blank=True,
    )
    
    completion_Status = models.CharField(
        max_length=12,
        choices=CompletionStatus.choices,
        default=CompletionStatus.InProgress
    )
    implementation_start_date = models.DateTimeField(null=True, blank=True)
    
    
    expected_completion_date = models.DateTimeField(null=True, blank=True)
    actual_implementation_date = models.DateTimeField(null=True, blank=True)
    
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="security_requirement_items_owned"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="security_requirement_items_assigned"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="security_requirement_items_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description  

class ComplianceStatus(models.Model):
    """
    Represents an item of compliance status created by user for a  given requirement for a compliance framework assigned to an asset
    This is expected to create a large table, so may later be hosted as a microservice to serve only this purpose
    A similar separate entity is created for security frameworks in the security model. The purpose of separation is to reduce table size.

    Attributes:
        asset: The aset for which this is created. automatically assigned
        framework: The compliance framework for which this is created
        requirement: An item of the list of requirements needed to achieve compliance
        ...
    """
    class CompletionStatus(models.TextChoices):
        Complete = ("Complete", _("Complete"))
        InProgress = ("InProgress", _("InProgress"))
        Canceled = ("Canceled", _("Canceled"))
        Paused = ("Paused", _("Paused"))
        
   
    COMPLETION_STATUS_CHOICES = [
        ('Complete', 'Complete'),
        ('InProgress', 'InProgress'),
        ('Canceled', 'Canceled'),
        ('Paused','Paused')
    ]
    description = models.CharField(max_length=100, default="Give a short description, framework and asset")
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        )
    
    framework = models.ForeignKey(
        RegulatoryFramework,
        on_delete=models.CASCADE
    )
    
    requirement = models.ForeignKey(
        SecurityRequirement,
        on_delete=models.CASCADE,
        #related_name="requirement"
        )
    details = models.TextField(max_length=300) #give detail of the current compliance status of the requirement
    implementation_percent = models.PositiveIntegerField(
        default=0,
        null=True, blank=True,
    )
    
    completion_Status = models.CharField(
        max_length=12,
        choices=CompletionStatus.choices,
        default=CompletionStatus.InProgress
    )
    implementation_start_date = models.DateTimeField(null=True, blank=True)
    
    
    expected_completion_date = models.DateTimeField(null=True, blank=True)
    actual_implementation_date = models.DateTimeField(null=True, blank=True)
    
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="compliance_items_owned"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="compliance_items_assigned"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="compliance_items_created"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description
    
class AssetInline(admin.TabularInline):  # or admin.StackedInline for a different layout admin.TabularInline
    model = Asset
    #extra = 1  # Number of empty product forms to display
    fields = ['name', 'vendor', 'category']  # Specify fields to display
    readonly_fields = ['name', 'vendor','category']  # Make certain fields read-only


@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [AssetInline]

@admin.register(RegulatoryFramework)
class RegulatoryFrameworkAdmin(admin.ModelAdmin):
    list_display = ('title','short_description')
    #list_filter = ('title')
    filter_horizontal = ('securityRequirements',)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'impact_level','risk_status')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    filter_horizontal = ('regulatoryFrameworks','risks','SecurityManagementFrameworks','frameworks')


@admin.register(ComplianceStatus)
class ComplianceStatusAdmin(admin.ModelAdmin):
    list_display = ('asset', 'framework', 'requirement', 'details','owner')
    list_filter = ('asset','framework',)
    search_fields = ('framework', 'requirement')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
    #filter_horizontal = ('asset','framework','requirement','owner')


