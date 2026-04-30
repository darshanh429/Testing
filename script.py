import os
import json
import yaml
import requests
from requests.auth import HTTPBasicAuth

with open("jira_data.yml", "r") as f:
    data = yaml.safe_load(f)

issue_key = data["issue_key"]
priority = data["priority"]
summary=data["summary"]

JIRA_URL = "https://bosch-pmt.atlassian.net"
EMAIL = os.environ["JIRA_EMAIL"]
TOKEN = os.environ["JIRA_TOKEN"]

url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}"

payload = {
    "fields": {
        "priority": {
            "name": priority
        }
        "summary":summary
    }
}

response = requests.put(
    url,
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    auth=HTTPBasicAuth(EMAIL, TOKEN),
    data=json.dumps(payload)
)

print("Status:", response.status_code)
print(response.text)