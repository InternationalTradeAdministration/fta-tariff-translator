import os
import json
import requests


tariff_docs_api = os.environ["TARIFF_DOCS_API"]


def get(token):
    payload = "{\"query\": \"$filter=Publication eq 'FTA Publication'\"}"
    headers = {
      'Content-Type': "application/json",
      'Authorization': "Bearer " + token
    }
    response = requests.request("POST", tariff_docs_api, data=payload, headers=headers)
    return json.loads(response.text)
