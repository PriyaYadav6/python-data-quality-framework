
# Checks.py
from typing import List

from .models import CheckResult


def check_required_columns(
    actual_columns: List[str],
    required_columns: List[str],
) -> CheckResult:

    missing_columns = [
        column
        for column in required_columns
        if column not in actual_columns
    ]

    if missing_columns:
        return CheckResult(
            name="Required columns",
            passed=False,
            records_affected=0,
            message=f"Missing columns: {', '.join(missing_columns)}",
        )

    return CheckResult(
        name="Required columns",
        passed=True,
        records_affected=0,
        message="All required columns are present",
    )


def check_nulls(
    rows: list[dict[str, str]],
    column: str,
) -> CheckResult:

    if any(column not in row for row in rows):
        return CheckResult(
            name=f"Null {column}",
            passed=False,
            records_affected=0,
            message=f"Column {column} is missing from one or more records",
        )

    null_count = sum(
        1 for row in rows
        if row[column] is None or not row[column].strip()
    )

    return CheckResult(
        name=f"Null {column}",
        passed=null_count == 0,
        records_affected=null_count,
        message=(
            f"{null_count} null values found in {column}"
            if null_count
            else f"No null values found in {column}"
        ),
    )


def check_duplicates(
    rows: list[dict[str, str]],
    column: str,
) -> CheckResult:

    if any(column not in row for row in rows):
        return CheckResult(
            name=f"Duplicate {column}",
            passed=False,
            records_affected=0,
            message=f"Column {column} is missing from one or more records",
        )

    seen = set()
    duplicate_count = 0

    for row in rows:
        value = row[column]

        if value in seen:
            duplicate_count += 1
        else:
            seen.add(value)

    return CheckResult(
        name=f"Duplicate {column}",
        passed=duplicate_count == 0,
        records_affected=duplicate_count,
        message=(
            f"{duplicate_count} duplicate values found in {column}"
            if duplicate_count
            else f"No duplicate values found in {column}"
        ),
    )


def check_positive_values(
    rows: list[dict[str, str]],
    column: str,
) -> CheckResult:

    if any(column not in row for row in rows):
        return CheckResult(
            name=f"Positive {column}",
            passed=False,
            records_affected=0,
            message=f"Column {column} is missing from one or more records",
        )

    invalid_count = 0

    for row in rows:
        try:
            value = float(row[column])

            if value <= 0:
                invalid_count += 1

        except (ValueError, TypeError):
            invalid_count += 1

    return CheckResult(
        name=f"Positive {column}",
        passed=invalid_count == 0,
        records_affected=invalid_count,
        message=(
            f"{invalid_count} invalid or non-positive values found in {column}"
            if invalid_count
            else f"All values in {column} are positive"
        ),
    )



def check_allowed_values(
    rows: list[dict[str, str]],
    column: str,
    allowed_values: list[str],
) -> CheckResult:

    if any(column not in row for row in rows):
        return CheckResult(
            name=f"Allowed values {column}",
            passed=False,
            records_affected=0,
            message=f"Column {column} is missing from one or more records",
        )

    failed_records = []

    for row in rows:
        value = row[column]

        if value not in allowed_values:
            failed_records.append({
                "record": row,
                "invalid_column": column,
                "invalid_value": value,
                "expected_values": allowed_values,
            })

    invalid_count = len(failed_records)

    return CheckResult(
        name=f"Allowed values {column}",
        passed=invalid_count == 0,
        records_affected=invalid_count,
        message=(
            f"{invalid_count} invalid values found in {column}"
            if invalid_count
            else f"All values in {column} are valid"
        ),
        failed_records=failed_records,
    )