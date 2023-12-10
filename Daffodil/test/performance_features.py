import os
import multiprocessing
from multiprocessing.pool import ThreadPool
from xml.etree import ElementTree as ET

import pytest
from datetime import timedelta

from conftest import Timer
from models import File, RecordData

def should_convert_json_performantly(cli_runner, generate_test_file: None, schemas, data_files, timer: Timer):
    csv_schema = schemas["csv"]
    data_file_path = data_files["test_data.csv"]
    with timer:
        result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'json').stdout
    assert timer < timedelta(seconds=60)

def should_convert_xml_performantly(cli_runner, data_files, schemas, timer: Timer):
    csv_schema = schemas["csv"]
    data_file_path = data_files["test_data.csv"]
    with timer:
        result = cli_runner('parse', f'--schema', csv_schema, data_file_path, '-I', 'xml').stdout
    assert timer < timedelta(seconds=60)

def should_unparse_json_performantly(cli_runner, schemas, data_files, data_output_directory, timer: Timer):
    csv_schema = schemas["csv"]
    data_file_path = data_files["test_data.csv"]
    xml_output_path = os.path.join(data_output_directory, "test.xml")
    csv_output_path = os.path.join(data_output_directory, "test.csv")
    with timer:
        cli_runner('unparse', f'--schema', csv_schema, xml_output_path, '-o', csv_output_path, '-I', 'xml')
    assert timer < timedelta(seconds=60)
    
def should_unparse_xml_performantly(cli_runner, schemas, timer: Timer):
    csv_schema = schemas["csv"]
    xml_string = ET.tostring(ET.Element("root"), encoding="unicode", method="xml")
    with timer:
        result = cli_runner('unparse', f'--schema', csv_schema, xml_string, '-I', 'xml').stdout
    assert timer < timedelta(seconds=60)