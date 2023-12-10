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
    assert timer < date
    file_data = File.model_validate_json(result)

@pytest.mark.parametrize("generate_test_file", (("en_US")), indirect=True)
def should_convert_xml_performantly(cli_runner, generate_test_file: None):
    pass

@pytest.mark.parametrize("generate_test_file", (("en_US")), indirect=True)
def should_unparse_json_performantly(cli_runner, generate_test_file: None):
    pass

@pytest.mark.parametrize("generate_test_file", (("en_US")), indirect=True)
def should_unparse_xml_performantly(cli_runner, generate_test_file: None):
    pass