import os

import pytest
from datetime import timedelta

import utils.timer as timer
from models import File, RecordData

@pytest.mark.parametrize("generate_test_file", (("en_US")), indirect=True)
def should_convert_json_performantly(cli_runner, generate_test_file: None, schemas, data_files):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    with timer:
        result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'json').stdout
    assert timer < timedelta(seconds=60)

@pytest.mark.parametrize("generate_test_file", (("en_US")), indirect=True)
def should_convert_xml_performantly(cli_runner, generate_test_file: None, data_files, schemas):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    with timer:
        result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'xml').stdout
    assert timer < timedelta(seconds=60)

@pytest.mark.parametrize("generate_test_file", (("en_US")), indirect=True)
def should_unparse_json_performantly(cli_runner, generate_test_file: None, schemas, data_files, data_output_directory, ):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    xml_output_path = os.path.join(data_output_directory, "test.xml")
    csv_output_path = os.path.join(data_output_directory, "test.csv")
    with timer:
        cli_runner('unparse', f'--schema', csv_schema, xml_output_path, '-o', csv_output_path, '-I', 'xml')
    

@pytest.mark.parametrize("generate_test_file", (("en_US")), indirect=True)
def should_unparse_xml_performantly(cli_runner, generate_test_file: None):
    pass