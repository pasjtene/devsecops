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
iso27001_data = {
    "framework": "ISO27001",
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

# Convert the JSON object to a string
json_data = json.dumps(iso27001_data)

# Database connection details
db_config = {
    "dbname": "frameworksdb",
    "user": "cryptouser",
    "password": "jt.pas1235",
    "host": "localhost",
    "port": "5432"
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cryptodata',
        'USER': 'cryptouser',
        'PASSWORD': 'jt.pas1235',
        'HOST': 'localhost',
        'PORT': '', 
    }
}
# Install psycopg2 if you haven’t already: pip install psycopg2
# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS isms_framework (
        id SERIAL PRIMARY KEY,
        framework_name VARCHAR(50) NOT NULL,
        requirements JSONB NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

# Insert the JSON data into the table
    insert_query = """
    INSERT INTO isms_framework (framework_name, requirements)
    VALUES (%s, %s);
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