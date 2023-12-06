import os
import subprocess
from dataclasses import dataclass
from typing import Callable

import pytest


_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))


@dataclass
class CliRunResult:
    stdout: str
    stderr: str


class OutputHelper:

    def __init__(self, output_folder: str):
        self._output_folder = output_folder


cli_runner_wrapper = Callable[[(str, ...)], CliRunResult]


@pytest.fixture
def daffodil_path() -> str:
    return os.path.join(_ROOT_PATH, "daffodil-src\\bin\\daffodil")


@pytest.fixture
def cli_runner(daffodil_path: str) -> cli_runner_wrapper:
    def wrapper(*args: str) -> CliRunResult:
        result = subprocess.run([daffodil_path, *args], shell=True, capture_output=True)
        cleaned_stdout = result.stdout.decode(encoding="utf-8")[:-2]  # remove last line change
        cleaned_stderr = result.stderr.decode(encoding="utf-8")[:-2]  # remove last line change
        return CliRunResult(cleaned_stdout, cleaned_stderr)

    return wrapper


@pytest.fixture
def schemas() -> {str: str}:
    schema_path = os.path.join(_ROOT_PATH, "data\\schemas")
    return {file.split(".")[0]: os.path.join(schema_path, file) for file in os.listdir(schema_path)}


@pytest.fixture
def data_files() -> {str: str}:
    data_file_path = os.path.join(_ROOT_PATH, "data\\data_files")
    return {file: os.path.join(data_file_path, file) for file in os.listdir(data_file_path)}