import logging

import azure.functions as func
import os
import re
from azure.storage.blob.blockblobservice import BlockBlobService as bbs
from . import translator
from . import azure_auth
from . import tariff_docs
from io import StringIO

container_name = os.environ["CONTAINER_NAME"]


def main(tariffRates: func.InputStream):
    logging.info(f"Python blob trigger function processing blob \n"
                 f"Name: {tariffRates.name}\n"
                 f"Blob Size: {tariffRates.length} bytes")
    if '.csv' in tariffRates.name and 'translated' not in tariffRates.name:
        tariff_rates_csv = StringIO(tariffRates.read().decode('utf-8'))
        translated_file = translator.translate(
          tariff_rates_csv,
          get_publication_documents()
        )
        destination_file_name = tariffRates.name.replace(
          container_name,
          'translated'
        )
        save_file(destination_file_name, translated_file)


def get_publication_documents():
    access_token = azure_auth.get_access_token()
    return tariff_docs.get(access_token)


def save_file(file_name, file_contents):
    conn_str = os.environ['AzureWebJobsStorage']
    storage_account_name = re.search('AccountName=(.+?);', conn_str).group(1)
    storage_account_key = re.search('AccountKey=(.+?);', conn_str).group(1)
    block_blob_service = bbs(
        account_name=storage_account_name,
        account_key=storage_account_key
      )
    block_blob_service.create_blob_from_text(
        container_name=container_name,
        blob_name=file_name,
        text=file_contents
      )
