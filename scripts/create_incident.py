import requests
from requests.auth import HTTPBasicAuth
import os
import sys

# ServiceNow details
BASE_URL = "https://dev199705.service-now.com"
CREATE_INCIDENT_API = f"{BASE_URL}/api/now/table/incident"

# Fetch credentials from environment variables
EMAIL = "kartikmesh2406@gmail.com"
PASSWORD = "fG3MSnurE!&rA@4"

def create_incident(description, pipeline_name):
    if not EMAIL or not PASSWORD:
        print("Error: ServiceNow credentials are not set.")
        sys.exit(1)

    payload = {
        "short_description": f"Pipeline Failed: {pipeline_name}",
        "description": description,
        "urgency": "1",  # High urgency
        "impact": "1"   # High impact
    }
    response = requests.post(
        CREATE_INCIDENT_API,
        auth=HTTPBasicAuth(EMAIL, PASSWORD),
        headers={"Content-Type": "application/json"},
        json=payload
    )
    if response.status_code == 201:
        print("Incident Created Successfully:", response.json())
    else:
        print("Error Creating Incident:", response.text)
        sys.exit(1)

if __name__ == "__main__":
    pipeline_name = sys.argv[1] if len(sys.argv) > 1 else "Unknown Pipeline"
    description = sys.argv[2] if len(sys.argv) > 2 else "No description provided."
    create_incident(description, pipeline_name)
