from conftest import cli_runner_wrapper


def should_print_version_when_version_argument_supplied(cli_runner: cli_runner_wrapper):
    result = cli_runner("--version")
    assert result.stdout == "Apache Daffodil 3.6.0"


def should_print_error_if_ran_without_args(cli_runner: cli_runner_wrapper):
    result = cli_runner()
    assert result.stderr == "[error] Subcommand required"
