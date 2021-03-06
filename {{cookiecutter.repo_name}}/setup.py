from pathlib import Path
import setuptools

readme = Path('README.md')
root_version = Path('VERSION')
res_folder = Path('{{cookiecutter.package_name}}') / 'res'
res_folder.mkdir(exist_ok=True)
package_res_version = res_folder / 'VERSION'

package_res_version.write_text(root_version.read_text())

setuptools.setup(
    name='{{cookiecutter.program_name}}',
    version=package_res_version.read_text(),
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    description='',
    long_description=readme.read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'{{cookiecutter.package_name}}': ['{{cookiecutter.package_name}}/res/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['{{cookiecutter.program_name_cli}}={{cookiecutter.package_name}}.__main__:console_script_entry']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)

package_res_version.unlink()
