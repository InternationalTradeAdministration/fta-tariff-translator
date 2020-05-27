import os
import json
import requests

auth_url = os.environ["AZURE_AUTH_URL"]
client_id = os.environ["TARIFF_DOCS_CLIENT_ID"]
client_secret = os.environ["TARIFF_DOCS_CLIENT_SECRET"]


def get_access_token():
    payload = f"""
        grant_type = client_credentials&
        client_id = {client_id}&
        client_secret = {client_secret}&
        Resource = {client_id}"""

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", auth_url, data=payload, headers=headers)
    return json.loads(response.text)['access_token']
