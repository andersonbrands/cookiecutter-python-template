from functools import partial
from unittest import mock

import pytest

from {{cookiecutter.package_name}}.cli.api import clear_log_method, dump_log_method


@pytest.mark.parametrize(
    'api_method, matching_method', (
            (clear_log_method, '{{cookiecutter.package_name}}.clear_log'),
            (partial(dump_log_method, '.'), '{{cookiecutter.package_name}}.dump_log'),
    )
)
def test_api_method_calls_matching_method(api_method, matching_method):
    with mock.patch(matching_method) as _patched:
        api_method()
        _patched.assert_called_once()
