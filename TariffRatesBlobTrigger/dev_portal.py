import requests
import logging
import os

base_url = os.environ["DEVELOPER_PORTAL_BASE_URL"]
api_key = os.environ["DEVELOPER_PORTAL_API_KEY"]


def refresh(fileName):
    country_api_mappings = {
        "Australia.csv": "/v1/australia_tariff_rates",
        "Bahrain.csv": "/v1/bahrain_tariff_rates",
        "Canada+USMCA.csv": "/v1/canada_tariff_rates",
        "Chile.csv": "/v1/chile_tariff_rates",
        "Colombia.csv": "/v1/colombia_tariff_rates",
        "Costa+Rica.csv": "/v1/costa_rica_tariff_rates",
        "Dominican+Republic.csv": "/v1/dominican_republic_tariff_rates",
        "El+Salvador.csv": "/v1/el_salvador_tariff_rates",
        "Guatemala.csv": "/v1/guatemala_tariff_rates",
        "Honduras.csv": "/v1/honduras_tariff_rates",
        "Japan.csv": "/v1/japan_tariff_rates",
        "Korea.csv": "/v1/south_korea_tariff_rates",
        "Mexico+USMCA.csv": "/v1/mexico_tariff_rates",
        "Morocco.csv": "/v1/morocco_tariff_rates",
        "Nicaragua.csv": "/v1/nicaragua_tariff_rates",
        "Oman.csv": "/v1/oman_tariff_rates",
        "Panama.csv": "/v1/panama_tariff_rates",
        "Peru.csv": "/v1/peru_tariff_rates",
        "Singapore.csv": "/v1/singapore_tariff_rates"
    }

    if (fileName in country_api_mappings.keys()):
        country_api = country_api_mappings[fileName]
        api_url = f"{base_url}{country_api}/freshen.json?api_key={api_key}"
        logging.info(f"Refreshing dev portal API: {api_url}")
        requests.request("GET", api_url)
