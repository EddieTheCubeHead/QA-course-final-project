import csv
import os

from conftest import cli_runner_wrapper
from models import File


def should_convert_csv_to_json(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'json').stdout
    file_data = File.model_validate_json(result)
    records = file_data.file.record
    assert len(records) == 3
    assert records[0].item[0] == "smith"
    assert records[1].item[1] == "john"


def should_unparse_json_to_csv(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str},
                               data_output_directory: str):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    json_output_path = os.path.join(data_output_directory, "output.json")
    csv_output_path = os.path.join(data_output_directory, "output.csv")
    cli_runner('parse', f'--schema', csv_schema, data_file_path, '-o', json_output_path, '-I', 'json')
    cli_runner('unparse', f'--schema', csv_schema, json_output_path, '-o', csv_output_path, '-I', 'json')

    with open(csv_output_path, 'r', newline='') as output_file, open(data_file_path, 'r', newline='') as expected_file:
        generated_content = output_file.read().replace('\r\n', '\n')
        expected_content = expected_file.read().replace('\r\n', '\n')
    assert generated_content == expected_content


def should_convert_csv_to_json_csvlib(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]

    result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'json').stdout
    file_data = File.model_validate_json(result)
    records = file_data.file.record
    with open(data_file_path) as f:
        reader = csv.DictReader(f)
        item_index = 0
        for row in reader:
            field_index = 0
            for field in reader.fieldnames:
                assert records[item_index].item[field_index] == row[field]
                field_index += 1
            item_index += 1


def should_convert_empty_csv_to_json(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str}):
    csv_schema = schemas["csv"]
    data_file_path = data_files["empty.csv"]
    result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'json').stdout
    assert not result


def should_unparse_empty_json_to_csv(cli_runner: cli_runner_wrapper, schemas: {str: str}):
    csv_schema = schemas["csv"]
    result = cli_runner('unparse', f'--schema', csv_schema, '{}', '-I', 'json').stdout
    assert not result


def should_not_unparse_invalid_json_to_csv(cli_runner: cli_runner_wrapper, schemas: {str: str}, data_files: {str: str},
                                           data_output_directory: str):
    csv_schema = schemas["csv"]
    data_file_path = data_files["basic.csv"]
    invalid_json_path = data_files["invalid.json"]
    csv_output_path = os.path.join(data_output_directory, "output.csv")
    cli_runner('unparse', f'--schema', csv_schema, invalid_json_path, '-o', csv_output_path, '-I', 'json')

    with open(csv_output_path, 'r', newline='') as output_file, open(data_file_path, 'r', newline='') as expected_file:
        generated_content = output_file.read().replace('\r\n', '\n')
        expected_content = expected_file.read().replace('\r\n', '\n')
    assert generated_content != expected_content
