import unittest
import translator
import csv
import json
from io import StringIO


class TestStringMethods(unittest.TestCase):
    def test_tariff_with_publishing_document(self):
        publishing_docs_json = open('mocks/sample_tariff_publications.json')
        tariff_rates_csv = open('mocks/tariff_rates.csv', newline='')
        publishing_docs_list = json.load(publishing_docs_json)
        results = translator.translate(tariff_rates_csv, publishing_docs_list)
        csv_reader = csv.DictReader(StringIO(results))
        rows = list(csv_reader)
        self.assertEqual(rows[0]['Link_Url'], 'https://blob.net/john_wick.pdf')
        self.assertEqual(rows[0]['Link_Url2'], 'https://blob.net/outbreak.pdf')
        self.assertEqual(rows[2]['Link_Url'], 'https://blob.net/matrix.pdf')
        self.assertEqual(rows[2]['Link_Url2'], '')
        self.assertEqual(rows[3]['Link_Url'], 'https://cool_okay.io')
        self.assertEqual(rows[3]['Link_Url2'], 'https://cool-oils.io')
        self.assertEqual(rows[3]['Link_Url3'], 'https://cool-seeds.io')
        self.assertEqual(rows[3]['Link_Url4'], 'https://cool-ouzo.io')
        publishing_docs_json.close()
        tariff_rates_csv.close()

    def test_usmca_tariff_with_publishing_document(self):
        publishing_docs_json = open('mocks/sample_tariff_publications.json')
        usmca_rates_csv = open('mocks/usmca_tariff_rates.csv', newline='')
        publishing_docs_list = json.load(publishing_docs_json)
        results = translator.translate(usmca_rates_csv, publishing_docs_list)
        csv_reader = csv.DictReader(StringIO(results))
        rows = list(csv_reader)
        self.assertEqual(rows[0]['Link_Url'], 'https://blob.net/outbreak.pdf')
        self.assertEqual(rows[0]['Link_Url2'], '')
        publishing_docs_json.close()
        usmca_rates_csv.close()

    def test_country_translation_partner_name(self):
        row = {
            'ReporterName': 'United States',
            'PartnerName': 'Greece USMCA'
        }
        country = translator.get_country(row)
        self.assertEqual(country, 'greece')

    def test_country_translation_reporter_name(self):
        row = {
            'ReporterName': 'Greece USMCA',
            'PartnerName': 'United States'
        }
        country = translator.get_country(row)
        self.assertEqual(country, 'greece')

    def test_get_link_header(self):
        self.assertEqual(translator.get_url_header(0), 'Link_Url')
        self.assertEqual(translator.get_url_header(1), 'Link_Url2')
        self.assertEqual(translator.get_url_header(2), 'Link_Url3')


if __name__ == '__main__':
    unittest.main()
