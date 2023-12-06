import json
import xml.etree.ElementTree as ET
from test.models import File

from conftest import cli_runner_wrapper

def should_print_version_when_version_argument_supplied(cli_runner: cli_runner_wrapper):
    result = cli_runner("--version")
    assert result.stdout == "Apache Daffodil 3.6.0"


def should_print_error_if_ran_without_args(cli_runner: cli_runner_wrapper):
    result = cli_runner()
    assert result.stderr == "[error] Subcommand required"

# def should_should_convert_csv_to_xml(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
#     csv_schema = schemas["csv"]
#     data_file_path = data_files["basic.csv"]
#     result = cli_runner('parse',f'--schema', csv_schema, data_file_path, '-I', 'xml').stdout
#     print(result)
#     parsed_xml = ET.fromstring(result)
#     assert parsed_xml.tag == 'file'
    # assert result.stdout == "[error] Subcommand required"
    
def should_should_convert_csv_to_json(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    result = json.loads(cli_runner('parse',f'--schema', csv_schema, data_file_path, '-I', 'json').stdout)
    file_data = File(**result)
    print(records)
    records = file_data.file.record
    assert records[0].item[0] == "smith"
    # assert result == {'file': {'header': {'title': ['last', 'first', 'middle', 'DOB']}, 'record': [{'item': ['smith', 'robert', 'brandon', '1988-03-24']}, {'item': ['johnson', 'john', 'henry', '1986-01-23']}]}}
