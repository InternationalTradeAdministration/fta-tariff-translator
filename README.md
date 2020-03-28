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

The following local.settins.json needs to exist in the root of this project.
It's git ignored because it will contain access keys

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": <storage-connection-string>,
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "ContainerName": "fta-tariff-rates"
  }
}

```

## Run Locally

  `func host start`
