
"""

    To populate the database with the iso27001_data, we can use Django's manage.py 
    shell or create a custom management command.
    Using Django Shell
    
    python3 manage.py shell

Author: Pascal T.
initial Date: 03/02/2022
"""


from .models import ISMSFramework


iso27001_data = {
    "framework": "ISO27001",
    "requirements": [
        {"id": 1, "requirement": "Establish the context of the organization", "codename": "A.4.1", "order": 1},
        {"id": 2, "requirement": "Define the ISMS scope", "codename": "A.4.3", "order": 2},
        {"id": 3, "requirement": "Perform a risk assessment", "codename": "A.6.1.2", "order": 3},
        {"id": 4, "requirement": "Implement risk treatment plans", "codename": "A.6.1.3", "order": 4},
        {"id": 5, "requirement": "Develop a Statement of Applicability", "codename": "A.6.1.3.d", "order": 5},
        {"id": 6, "requirement": "Implement access control policies", "codename": "A.9.1.1", "order": 6},
        {"id": 7, "requirement": "Monitor and review the ISMS", "codename": "A.9.3", "order": 7},
        {"id": 8, "requirement": "Conduct internal audits", "codename": "A.9.2", "order": 8},
        {"id": 9, "requirement": "Perform management reviews", "codename": "A.9.3", "order": 9},
        {"id": 10, "requirement": "Continuously improve the ISMS", "codename": "A.10.1", "order": 10}
    ]
}


for req in iso27001_data["requirements"]:
    ISMSFramework.objects.create(
        framework_name=iso27001_data["framework"],
        requirement=req
    )