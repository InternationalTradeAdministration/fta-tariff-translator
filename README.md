# FTA Tariff Rates - Azure Function App

Data translation that maps tariff rates with their respective publication documents.

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python v3.6.9
* Pip
* Virtualenv
* Virtualenvwrapper
* Azure credentials

## Environment Variables

* AzureWebJobsStorage: Azure storage connection string
* CONTAINER_NAME: The storage container to monitor for new tariff rates
* AZURE_AUTH_URL: Azure OAUTH token URL for the tenant
* TARIFF_DOCS_API: Tariff documents publishing api url
* TARIFF_DOCS_CLIENT_ID: Tariff documents publishing api client id
* TARIFF_DOCS_CLIENT_SECRET: Tariff documents publishing api client secret
* DEVELOPER_PORTAL_BASE_URL: Developer portal base URL
* DEVELOPER_PORTAL_API_KEY: Developer portal API Key

## Run Locally

The following local.settings.json needs to exist in the root of this project.
It's git ignored because it will contain access keys

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "<storage-connection-string>",
    "CONTAINER_NAME": "fta-tariff-rates",
    "AZURE_AUTH_URL": "<azure-auth-url>",
    "TARIFF_DOCS_API": "<tariff-docs-api>",
    "TARIFF_DOCS_CLIENT_ID": "<tariff-docs-client-id>",
    "TARIFF_DOCS_CLIENT_SECRET": "<tariff-docs-client-secret>",
    "DEVELOPER_PORTAL_BASE_URL": "<developer-portal-base-url>",
    "DEVELOPER_PORTAL_API_KEY": "<developer-portal-api-key>"
  }
}

```

  `func host start`
