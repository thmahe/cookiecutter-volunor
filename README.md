# cookiecutter-volunor

Project template to quickly start writing Volunor based Command Line Interface tools with Python.

For more information about Volunor you can reach dedicated GitHub project: https://github.com/thmahe/volunor

## Typical Volunor project structure

```text
<project-name>
├── <package_name>
│   ├── cli.py ....... CLI Descriptor and entry-point script
│   ├── commands ..... Module reserved for commands declarations
│   └── core ......... Module reserved for functional code
├── tests
│   ├── commands ..... Tests performed on commands (Mocked command line arguments)
│   └── core ......... Tests for functional module
├── pyproject.toml ... Poetry based pyproject spec
└── tox.ini .......... Test environment configuration with tox
```

## Usage

```shell
# Create project using cookiecutter
$ cookiecutter https://github.com/thmahe/cookiecutter-volunor
>> [project_name]: my-project
>> [package_name]: my_package
>> [prog_name]: my-cli 

# Install project with pip
$ cd my_project
$ pip install .

# Run default 'greet' command from previously installed tool 'my-cli'
$ my-cli greet "John" --count 2
Hello John
Hello John
```
