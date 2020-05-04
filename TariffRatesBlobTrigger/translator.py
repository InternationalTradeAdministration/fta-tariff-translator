import csv
import tempfile


def translate(tariff_rates_csv, publishing_docs_list):
    max_urls = 0
    result = []
    publishing_metadata = format_publishing_metadata(publishing_docs_list)
    tariff_rates = csv.DictReader(tariff_rates_csv)
    for row in tariff_rates:
        country = get_country(row)
        publishing_metadata_key = country + '#' + row['HS6'][0:2]

        publishing_doc_urls = None
        if (publishing_metadata_key in publishing_metadata.keys()):
            publishing_doc_urls = publishing_metadata[publishing_metadata_key]
        else:
            publishing_doc_urls = []

        for i in range(len(publishing_doc_urls)):
            url_header = get_url_header(i)
            row[url_header] = publishing_doc_urls[i]
            max_urls = i if i > max_urls else max_urls
        result.append(row)
    return dict_list_to_csv(result, max_urls)


def get_country(row):
    reporter_name = row['ReporterName']
    partner_name = row['PartnerName']
    tmp_country = reporter_name if partner_name == 'United States' else partner_name
    return tmp_country.replace('USMCA', '').strip().lower()


def format_publishing_metadata(publishing_docs):
    publishing_metadata = {}
    for doc in publishing_docs:
        countries = doc.get('Country', 'None').split(';')
        hs2_codes = doc.get('FTA_Publication_HS_Code', 'None').split(';')
        for country in countries:
            for hs2 in hs2_codes:
                publishing_metadata_key = country.lower() + '#' + hs2[0:2]
                publishing_metadata_url = doc.get('metadata_storage_path')
                if (publishing_metadata_key in publishing_metadata.keys()):
                    publishing_metadata[publishing_metadata_key].append(publishing_metadata_url)
                else:
                    publishing_metadata[publishing_metadata_key] = [publishing_metadata_url]
    return publishing_metadata


def dict_list_to_csv(data, max_urls):
    row_keys = list(data[0].keys())
    for i in range(max_urls + 1):
        url_header = get_url_header(i)
        if url_header not in row_keys:
            row_keys.append(url_header)

    temp_file = tempfile.NamedTemporaryFile(mode="r+", delete=False)
    with open(temp_file.name, "w") as csv_file:
        dict_writer = csv.DictWriter(csv_file, row_keys, quotechar='"')
        dict_writer.writeheader()
        dict_writer.writerows(data)
    file_as_string = temp_file.read()
    temp_file.close()
    return file_as_string


def get_url_header(index):
    return 'Link_Url' if index == 0 else 'Link_Url'+str(index+1)
