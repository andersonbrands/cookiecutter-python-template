from pathlib import Path
from typing import Union

import {{cookiecutter.package_name}}
from {{cookiecutter.package_name}} import R, logger


def version_method():
    logger.info(f'{R.string.program_name} v{R.string.version}')
    pass


def clear_log_method():
    {{cookiecutter.package_name}}.clear_log()


def dump_log_method(dst: Union[str, Path]):
    {{cookiecutter.package_name}}.dump_log(dst)
