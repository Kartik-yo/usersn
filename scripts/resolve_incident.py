import requests
from requests.auth import HTTPBasicAuth
import sys

# ServiceNow details
BASE_URL = "https://dev199705.service-now.com"
USERNAME = "SN-REST-GA"
PASSWORD = "JDwOKqZ[vGqU:ks>qCWJLOr>SL+{#r+5eE%9#cQQolx}H4vKQqw)h5G5)g#$Dma^pi9gOa*m[diyZ^piG?XghzcrkFY?>t6VnJ#M"

def resolve_incident(incident_sys_id, resolution_notes):
    UPDATE_INCIDENT_API = f"{BASE_URL}/api/now/table/incident/{incident_sys_id}"
    payload = {
        "state": "6",  # Resolved state in ServiceNow
        "close_notes": resolution_notes
    }
    response = requests.put(
        UPDATE_INCIDENT_API,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers={"Content-Type": "application/json"},
        json=payload
    )
    if response.status_code == 200:
        print("Incident Resolved Successfully:", response.json())
    else:
        print("Error Resolving Incident:", response.text)
        sys.exit(1)

if __name__ == "__main__":
    incident_sys_id = sys.argv[1]
    resolution_notes = sys.argv[2] if len(sys.argv) > 2 else "Pipeline completed successfully."
    resolve_incident(incident_sys_id, resolution_notes)
