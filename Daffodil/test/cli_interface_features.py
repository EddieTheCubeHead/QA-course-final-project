import json
import xml.etree.ElementTree as ET
from models import File, RecordData

from conftest import cli_runner_wrapper

def should_print_version_when_version_argument_supplied(cli_runner: cli_runner_wrapper):
    result = cli_runner("--version")
    assert result.stdout == "Apache Daffodil 3.6.0"


def should_print_error_if_ran_without_args(cli_runner: cli_runner_wrapper):
    result = cli_runner()
    assert result.stderr == "[error] Subcommand required"

def should_convert_csv_to_xml(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    result = cli_runner('parse',f'--schema', csv_schema, data_file_path, '-I', 'xml').stdout
    
    parsed_xml = ET.fromstring(result)
    assert parsed_xml.tag == '{http://example.com}file'
    assert len(parsed_xml.findall('header/title')) == 4
    assert len(parsed_xml.findall('record')) == 2

    records = []
    for record in parsed_xml.findall('record'):
        items = [item.text for item in record.findall('item')]
        records.append(RecordData(item=items))
    assert records[0].item[0] == "smith"
    assert records[1].item[1] == "john"
    
    
def should_convert_csv_to_json(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    result = json.loads(cli_runner('parse',f'--schema', csv_schema, data_file_path, '-I', 'json').stdout)
    file_data = File(**result)
    records = file_data.file.record
    assert records[0].item[0] == "smith"
    assert records[1].item[1] == "john"
    # assert result == {'file': {'header': {'title': ['last', 'first', 'middle', 'DOB']}, 'record': [{'item': ['smith', 'robert', 'brandon', '1988-03-24']}, {'item': ['johnson', 'john', 'henry', '1986-01-23']}]}}
