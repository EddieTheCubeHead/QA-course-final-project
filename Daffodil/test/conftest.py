import os
import subprocess
from dataclasses import dataclass
from typing import Callable

import pytest


@dataclass
class CliRunResult:
    stdout: str
    stderr: str


cli_runner_wrapper = Callable[[(str, ...)], CliRunResult]


@pytest.fixture
def daffodil_path() -> str:
    root_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(root_path, "daffodil-src\\bin\\daffodil")


@pytest.fixture
def cli_runner(daffodil_path: str) -> cli_runner_wrapper:
    def wrapper(*args: str) -> CliRunResult:
        result = subprocess.run([daffodil_path, *args], shell=True, capture_output=True)
        cleaned_stdout = result.stdout.decode(encoding="utf-8")[:-2]  # remove last line change
        cleaned_stderr = result.stderr.decode(encoding="utf-8")[:-2]  # remove last line change
        return CliRunResult(cleaned_stdout, cleaned_stderr)

    return wrapper
