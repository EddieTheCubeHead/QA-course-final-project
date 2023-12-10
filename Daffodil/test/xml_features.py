import os
from xml.etree import ElementTree as ET

from conftest import cli_runner_wrapper
from models import RecordData


def should_convert_csv_to_xml(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'xml').stdout

    parsed_xml = ET.fromstring(result)
    # noinspection HttpUrlsUsage
    assert parsed_xml.tag == '{http://example.com}file'
    assert len(parsed_xml.findall('header/title')) == 4
    assert len(parsed_xml.findall('record')) == 3

    records = []
    for record in parsed_xml.findall('record'):
        items = [item.text for item in record.findall('item')]
        records.append(RecordData(item=items))
    assert records[0].item[0] == "smith"
    assert records[1].item[1] == "john"


def should_unparse_xml_to_csv(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str},
                              data_output_directory: str):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    xml_output_path = os.path.join(data_output_directory, "output.xml")
    csv_output_path = os.path.join(data_output_directory, "output.csv")
    cli_runner('parse', f'--schema', csv_schema, data_file_path, '-o', xml_output_path, '-I', 'xml')
    cli_runner('unparse', f'--schema', csv_schema, xml_output_path, '-o', csv_output_path, '-I', 'xml')

    with open(csv_output_path, 'r', newline='') as output_file, open(data_file_path, 'r', newline='') as expected_file:
        generated_content = output_file.read().replace('\r\n', '\n')
        expected_content = expected_file.read().replace('\r\n', '\n')
    assert generated_content == expected_content


def should_convert_empty_csv_to_xml(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["empty.csv"]
    result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'xml').stdout
    assert not result


def should_unparse_empty_xml_to_csv(cli_runner: cli_runner_wrapper, schemas: {str: str}):
    csv_schema = schemas["csv"]
    xml_string = ET.tostring(ET.Element("root"), encoding="unicode", method="xml")
    result = cli_runner('unparse', f'--schema', csv_schema, xml_string, '-I', 'xml').stdout
    assert not result
