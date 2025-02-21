from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User, auth
from django.utils.translation import gettext_lazy as _


class SecurityManagementRequirement(models.Model):
    class RequirementList(models.TextChoices):
        # FISMA https://security.cms.gov/learn/federal-information-security-modernization-act-fisma
        # PCIDSS https://pcidssguide.com/pci-dss-requirements/
        ISO27001_1 = ("ISO27001_S1", _("Step 1: Define the Scope and Objectives"))
        ISO27001_11 = ("ISO27001_11", _("1- Define the Scope"))
        ISO27001_111 = ("ISO27001_111", _("1-1: Identify the boundaries of your ISMS (e.g., specific departments, systems, or locations)."))
        ISO27001_112 = ("ISO27001_112", _("1-2: Consider legal, regulatory, and contractual requirements."))
        ISO27001_12 = ("ISO27001_12", _("2- Set Objectives"))
        ISO27001_121 = ("ISO27001_121", _("2-1: Define the goals of your ISMS (e.g., protecting customer data, ensuring business continuity)."))
        ISO27001_122 = ("ISO27001_122", _("2-2: Align objectives with business goals and stakeholder expectations."))
        ISO27001_2 = ("ISO27001_2", _("Step 2: Obtain Management Support"))
        ISO27001_21 = ("ISO27001_21", _("2-1: Secure Leadership Commitment"))
        ISO27001_211 = ("ISO27001_211", _("2-1-1: Ensure top management understands the importance of the ISMS and provides necessary resources."))
        ISO27001_22 = ("ISO27001_22", _("2-2: Define Roles and Responsibilities"))
        ISO27001_221 = ("ISO27001_221", _("2-2-1: Appoint an ISMS Manager or team to oversee implementation."))
        ISO27001_222 = ("ISO27001_222", _("2-2-2: Assign roles for risk management, internal audits, and compliance."))
        ISO27001_3 = ("ISO27001_3", _("Step 3: Conduct a Risk Assessment"))
        ISO27001_31 = ("ISO27001_31", _("3-1: Identify Assets"))
        ISO27001_311 = ("ISO27001_311", _("3-1-1: List all information assets (e.g., hardware, software, data, personnel"))
        ISO27001_32 = ("ISO27001_32", _("3-2: Identify Threats and Vulnerabilities"))
        ISO27001_321 = ("ISO27001_321", _("3-2-1: Determine potential threats (e.g., cyberattacks, natural disasters), conduct threat modeling for detailed identification and management "))
        ISO27001_322 = ("ISO27001_322", _("3-2-1: Identify Vulnerabilities (e.g., weak passwords, outdated software), conduct vulnerability assessment, establish a vulnerability management team for larger organizations"))
        ISO27001_33 = ("ISO27001_33", _("3-3: Assess Risks"))
        ISO27001_331 = ("ISO27001_331", _("3-3-1: Evaluate the likelihood and impact of each risk."))
        ISO27001_332 = ("ISO27001_332", _("3-3-2: Use a risk matrix to prioritize risks.")) 
        ISO27001_4 = ("ISO27001_4", _("Step 4: Implement Risk Treatment Plans."))
        
        
        
    
    name = models.CharField(
        max_length = 15,
        choices = RequirementList.choices,
        default=RequirementList.ISO27001_1
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
    parent_requirement = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_requirements')
    
    def __str__(self):
        return f"{self.name}: {self.short_description}"
    
    def sub_requirement(self):
        return self.parent_requirement is not None 

class SecurityManagementFramework(models.Model):
    class FrameworkName(models.TextChoices):
        ISO27001 = ("ISO27001", _("Information Security Management System (ISMS)"))
        NIST_CSF = ("NIST_CSF", _("NIST Cybersecurity Framework (CSF)"))
        NIS = ("NIS", _("Network and Information Systems (NIS) Directive"))
        CIS = ("CIS", _("CIS Controls (Center for Internet Security Controls)"))
        COBIT = ("COBIT", _("Control Objectives for Information and Related Technologies"))
        ITIL = ("ITIL", _("Information Technology Infrastructure Library"))
        OWASP = ("OWASP", _(" (Open Web Application Security Project)"))
        NIST_SP_800_53 =  ("NIST_SP_800_53", _("NIST SP 800-53 security controls"))
        HITRUST =  ("HITRUST", _("Health Information Trust Alliance"))
        SOC2 = ("SOC2", _("System and Organization Controls 2"))
        
    title = models.CharField(
        max_length = 15,
        choices = FrameworkName.choices,
        default=FrameworkName.ISO27001
    )
    framworks = {"ISO27001": "Information Security Management System (ISMS)", 
                 "NIST_CSF": "NIST Cybersecurity Framework (CSF)",
                  "NIS": "NIST Cybersecurity Framework (CSF)",
                 }
    #short_description = framworks.get(title)
    
    short_description = models.CharField(
        #blank = True, null=True,
        default = framworks.get(title)
        ) 
    
    description = models.TextField(null=True, blank=True)
    security_management_requirements = models.ManyToManyField(SecurityManagementRequirement, related_name="securityManagementFrameworks", blank=True)
    
    
    def __str__(self):
        return f"{self.title}: {self.short_description}"
    

@admin.register(SecurityManagementFramework)
class SecurityManagementFrameworkAdmin(admin.ModelAdmin):
    list_display = ('title','short_description')
    #list_filter = ('title')
    filter_horizontal = ('security_management_requirements',)