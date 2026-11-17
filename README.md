# Python Data Quality Framework

A configurable Python-based data quality framework that validates datasets using YAML-driven rules.

## Overview

This project demonstrates how data quality validations can be automated using reusable Python functions and external configuration files.

The framework reads CSV datasets, executes configured validation checks, identifies invalid records and generates a data quality report.

## Features

- Required-column validation
- Null-value validation
- Duplicate detection
- Positive-value validation
- Allowed-value validation
- YAML-based configuration
- Dynamic validation execution
- Record-level error reporting
- Command-line execution

## Technology Stack

- Python 3.12
- PyYAML
- Pytest
- CSV

## Architecture

```text
YAML Configuration
        |
        v
Configuration Loader
        |
        v
CSV Data Loader
        |
        v
Dynamic Validation Engine
        |
        v
Data Quality Checks
        |
        v
Validation Results
        |
        v
Data Quality Report
```

## Project Structure

- `config/`: YAML validation rules
- `data/`: Sample datasets
- `src/data_quality/`: Validation framework modules
- `tests/`: Automated tests
- `main.py`: Command-line application entry point

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd python-data-quality-framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Execution

Run the framework:

```bash
python main.py --config config/rules.yml
```

## Configuration Example

```yaml
dataset: orders

required_columns:
  - order_id
  - customer_id
  - amount
  - country

checks:
  not_null:
    - customer_id

  unique:
    - order_id

  positive:
    - amount

  allowed_values:
    country:
      - IN
      - DE
      - US
      - NL
```

## Sample Validation Output

The framework identifies failed validations and reports affected records, including invalid values and order IDs.

## Future Enhancements

- Source-to-target reconciliation
- JSON and CSV reporting
- Expanded automated test coverage
- Database integration
- Pipeline logging and monitoring

## Author

Priya Yadav

Data Engineer | Python | SQL | Azure Databricks | Snowflake