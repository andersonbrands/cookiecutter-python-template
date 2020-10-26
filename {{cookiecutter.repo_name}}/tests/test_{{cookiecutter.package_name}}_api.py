from unittest import mock

from {{cookiecutter.package_name}}.cli.api import clear_log_method


def test_clear_log_method_calls_clear_log():
    with mock.patch('{{cookiecutter.package_name}}.clear_log') as _clear_log:
        clear_log_method()
        _clear_log.assert_called_once()
