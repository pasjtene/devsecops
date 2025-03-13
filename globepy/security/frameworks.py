"""
Frameworks supported in the globeGRC application
Listed frameworks will be imported in the database upon initialization of the app
Author: Pascal T.
initial Date: 03/02/2022
"""

from pathlib import Path
import os
from django.contrib import messages
import psycopg2
import json

FRAMEWORKS = {
    'IS027001': {
        'requirements': [
            {
                'codename': 'Req1',
                'Order': 1,
                'short_description': 'short',
                'Description': "Long"
             
             },
            {}
        ]
    }
}


# JSON data
iso27001_data_save = {
    "framework": "ISO27001",
    "framework_id": 1,
    "requirements": [
        {"requirement": "Establish the context of the organization", "codename": "A.4.1"},
        {"requirement": "Define the ISMS scope", "codename": "A.4.3"},
        {"requirement": "Perform a risk assessment", "codename": "A.6.1.2"},
        {"requirement": "Implement risk treatment plans", "codename": "A.6.1.3"},
        {"requirement": "Develop a Statement of Applicability", "codename": "A.6.1.3.d"},
        {"requirement": "Implement access control policies", "codename": "A.9.1.1"},
        {"requirement": "Monitor and review the ISMS", "codename": "A.9.3"},
        {"requirement": "Conduct internal audits", "codename": "A.9.2"},
        {"requirement": "Perform management reviews", "codename": "A.9.3"},
        {"requirement": "Continuously improve the ISMS", "codename": "A.10.1"}
    ]
}



iso27001_data = {
  "framework": "ISO27001",
  "framework_id": 1,
  "description": "ISO/IEC 27001 is  An international standard for information security management systems (ISMS).\
    It provides a systematic approach to managing sensitive company information, ensuring confidentiality, integrity, and availability." ,
  "recommendations": "Take action for each recommended step, provide details of what actions you have taken. This will guide you through a systematic approach to a successful ISMS implementation.",
  "requirements": [
    {
      "id": 1,
      "requirement": "Step 1: Define the Scope and Objectives",
      "codename": "S.1",
      "order": 100,
      "parent_requirement_id": "None"
    },
    {
      "id": 2,
      "requirement": "1-1: Define the Scope",
      "codename": "S.1.1",
      "order": 105,
      "parent_requirement_id": 1
    },
    {
      "id": 3,
      "requirement": "1-1-1: Identify the boundaries of your ISMS (e.g., specific departments, systems, or locations).",
      "codename": "1-1-1",
      "order": 3,
      "parent_requirement_id": 2
    },
    {
      "id": 4,
      "requirement": "1-1-2: Consider legal, regulatory, and contractual requirements.",
      "codename": "1-1-2",
      "order": 4,
      "parent_requirement_id": 2
    },
    {
      "id": 5,
      "requirement": "1-2: Set Objectives",
      "codename": "1-2",
      "order": 5,
      "parent_requirement_id": 1
    },
    {
      "id": 6,
      "requirement": "1-2-1: Define the goals of your ISMS (e.g., protecting customer data, ensuring business continuity).",
      "codename": "1-2-1",
      "order": 6,
      "parent_requirement_id": 5
    },
    {
      "id": 7,
      "requirement": "1-2-2: Align objectives with business goals and stakeholder expectations.",
      "codename": "1-2-2",
      "order": 7,
      "parent_requirement_id": 5
    },
    {
      "id": 8,
      "requirement": "Step 2: Obtain Management Support",
      "codename": "Step 2",
      "order": 8,
      "parent_requirement_id": "None"
    },
    {
      "id": 9,
      "requirement": "2-1: Secure Leadership Commitment",
      "codename": "2-1",
      "order": 9,
      "parent_requirement_id": 8
    },
    {
      "id": 10,
      "requirement": "2-1-1: Ensure top management understands the importance of the ISMS and provides necessary resources.",
      "codename": "2-1-1",
      "order": 10,
      "parent_requirement_id": 9
    },
     {
      "id": 11,
      "requirement": "2-2: Define Roles and Responsibilities",
      "codename": "2-2",
      "order": 11,
      "parent_requirement_id": 8
    },
    {
      "id": 12,
      "requirement": "2-2-1: Appoint an ISMS Manager or team to oversee implementation.",
      "codename": "2-2-1",
      "order": 12,
      "parent_requirement_id": 11
    },
    {
      "id": 13,
      "requirement": "2-2-2: Assign roles for risk management, internal audits, and compliance.",
      "codename": "2-2-2",
      "order": 13,
      "parent_requirement_id": 11
    }, 
     {
      "id": 14,
      "requirement": "Step 3: Conduct a Risk Assessment",
      "codename": "Step 3",
      "order": 14,
      "parent_requirement_id": "None"
    },
   {
      "id": 15,
      "requirement": "3-1: Identify Assets",
      "codename": "3-1",
      "order": 15,
      "parent_requirement_id": 14
    },
    {
      "id": 16,
      "requirement": "3-1-1: List all information assets (e.g., hardware, software, data, personnel",
      "codename": "3-1-1",
      "order": 16,
      "parent_requirement_id": 15
    },
   {
      "id": 17,
      "requirement": "3-2: Identify Threats and Vulnerabilities",
      "codename": "3-2",
      "order": 17,
      "parent_requirement_id": 14
    },
   {
      "id": 18,
      "requirement": "3-2-1: Determine potential threats (e.g., cyberattacks, natural disasters), conduct threat modeling for detailed identification and management",
      "codename": "3-2-1",
      "order": 18,
      "parent_requirement_id": 17
    },
    {
      "id": 19,
      "requirement": "3-2-2: Identify Vulnerabilities (e.g., weak passwords, outdated software), conduct vulnerability assessment, establish a vulnerability management team for larger organizations", 
      "codename": "3-2-2",
      "order": 19,
      "parent_requirement_id": 17
    },
    {
      "id": 20,
      "requirement": "3-3: Assess Risks", 
      "codename": "3-3",
      "order": 20,
      "parent_requirement_id": 14
    },
     {
      "id": 21,
      "requirement": "3-3-1: Evaluate the likelihood and impact of each risk.", 
      "codename": "3-3-1",
      "order": 21,
      "parent_requirement_id": 20
    },
    {
      "id": 22,
      "requirement": "3-3-2: Use a risk matrix to prioritize risks.", 
      "codename": "3-3-2",
      "order": 22,
      "parent_requirement_id": 20
    },
     {
      "id": 23,
      "requirement": "Step 4: Implement Risk Treatment Plans.", 
      "codename": "Step 4",
      "order": 23,
      "parent_requirement_id": "None"
    },
    {
      "id": 24,
      "requirement": "4-1: Select Controls", 
      "codename": "4-1",
      "order": 24,
      "parent_requirement_id": 23
    },
    {
      "id": 25,
      "requirement": "4-1-1: Choose controls from Annex A of ISO/IEC 27001 to mitigate identified risks. Examples include access control, encryption, and incident management.",
      "codename": "4-1-1",
      "order": 25,
      "parent_requirement_id": 24
    },    
  
      
  ]
}

soc2_data= {
  "framework": "SOC2",
  "requirements": [
    {
      "id": 1,
      "requirement": "Step 1: Review Key Characteristics of SOC 2",
      "codename": "Step 1",
      "order": 1,
      "parent_requirement_id": "None"
    },
    {
      "id": 2,
      "requirement": "1-1: Focus on Controls: SOC 2 is all about demonstrating that you have the right controls in place to protect data.",
      "codename": "1-1",
      "order": 2,
      "parent_requirement_id": 1
    },
    {
      "id": 3,
      "requirement": "1-2: Consider the Report Type to be produced: There are two types of SOC 2 reports ",
      "codename": "1-2",
      "order": 3,
      "parent_requirement_id": 1
    },
    {
      "id": 4,
      "requirement": "1-2-1: Type 1: A snapshot in time. It reports on the design of controls at a specific point in time",
      "codename": "1-2-1",
      "order": 4,
      "parent_requirement_id": 3
    },
    {
      "id": 5,
      "requirement": "1-2-2: Type 2: Over a period of time. It reports on the design and operating effectiveness of controls over a specified period (e.g., 6 months). This is generally considered more valuable.",
      "codename": "1-2-2",
      "order": 5,
      "parent_requirement_id": 3
    },
    {
      "id": 6,
      "requirement": "Step 3: Verify Criteria (Trust Services Criteria): SOC 2 reports are based on one or more of the following Trust Services Criteria:",
      "codename": "Step 3",
      "parent_requirement_id": "None"
    },
    {
      "id": 7,
      "requirement": "3-1: Security: Protection of information and systems against unauthorized access, use, disclosure, disruption, modification, or destruction.",
      "codename": "3-1",
      "order": 7,
      "parent_requirement_id": 6
    },
    {
      "id": 8,
      "requirement": "3-2: Processing Integrity: Ensuring that system processing is complete, accurate, timely, and authorized.",
      "codename": "3-2",
      "order": 8,
      "parent_requirement_id": 6
    },
    {
      "id": 9,
      "requirement": "3-3: Confidentiality: Protecting sensitive information from unauthorized disclosure.",
      "codename": "3-3",
      "order": 9,
      "parent_requirement_id": 6
    },
    {
      "id": 10,
      "requirement": "3-3: Privacy: Protecting personal information in accordance with applicable privacy principles.",
      "codename": "3-3",
      "order": 10,
      "parent_requirement_id": 6
    }
  ]
}


iso27001_data_2 = {
  "framework": "ISO27001",
  "requirements": [
    {
      "id": 1,
      "requirement": "Establish the context of the organization",
      "codename": "A.4.1",
      "order": 1,
      "parent_requirement_id": "None"
    },
    {
      "id": 2,
      "requirement": "Define the ISMS scope",
      "codename": "A.4.3",
      "order": 2
    },
    {
      "id": 3,
      "requirement": "Perform a risk assessment",
      "codename": "A.6.1.2",
      "order": 3
    },
    {
      "id": 4,
      "requirement": "Implement risk treatment plans",
      "codename": "A.6.1.3",
      "order": 4
    },
    {
      "id": 5,
      "requirement": "Develop a Statement of Applicability",
      "codename": "A.6.1.3.d",
      "order": 5
    },
    {
      "id": 6,
      "requirement": "Implement access control policies",
      "codename": "A.9.1.1",
      "order": 6
    },
    {
      "id": 7,
      "requirement": "Monitor and review the ISMS",
      "codename": "A.9.3",
      "order": 7
    },
    {
      "id": 8,
      "requirement": "Conduct internal audits",
      "codename": "A.9.2",
      "order": 8
    },
    {
      "id": 9,
      "requirement": "Perform management reviews",
      "codename": "A.9.3",
      "order": 9
    },
    {
      "id": 10,
      "requirement": "Continuously improve the ISMS",
      "codename": "A.10.1",
      "order": 10
    }
  ]
}


# Convert the JSON object to a string
json_data = json.dumps(iso27001_data)

# Database connection details
db_config = {
    #"dbname": "frameworksdb",
    "dbname": 'cryptodata',
    "user": "cryptouser",
    "password": "jt.pas1235",
    "host": "localhost",
    "port": "5432"
}

# Install psycopg2 if you haven’t already: pip install psycopg2
# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS security_ismsframework (
        id SERIAL PRIMARY KEY,
        framework_name VARCHAR(50) NOT NULL,
        framework_id INT NOT NULL,
        description VARCHAR(500) NOT NULL,
        recommendations VARCHAR(500) NOT NULL,
        requirements JSONB NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

# Insert the JSON data into the table
    insert_query = """
    INSERT INTO security_ismsframework (framework_name, framework_id, description, recommendations, requirements)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, (iso27001_data["framework"], json_data))
    conn.commit()

    print("Data inserted successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()