
from .checks import (
    check_required_columns,
    check_nulls,
    check_duplicates,
    check_positive_values,
    check_allowed_values,
)

from .models import CheckResult


# Maps YAML rule names to Python functions
CHECK_REGISTRY = {
    "not_null": check_nulls,
    "unique": check_duplicates,
    "positive": check_positive_values,
    "allowed_values": check_allowed_values,
}


def run_validation(
    rows: list[dict[str, str]],
    actual_columns: list[str],
    config: dict,
) -> list[CheckResult]:

    results = []

    # Step 1: Validate required columns
    schema_result = check_required_columns(
        actual_columns,
        config["required_columns"],
    )

    results.append(schema_result)

    # Stop further checks if required columns are missing
    if not schema_result.passed:
        return results

    # Step 2: Read configured checks
    configured_checks = config.get("checks", {})

    # Step 3: Execute checks dynamically
    for check_name, columns in configured_checks.items():

        if check_name not in CHECK_REGISTRY:
            raise ValueError(
                f"Unsupported validation check: {check_name}"
            )

        check_function = CHECK_REGISTRY[check_name]

        # Allowed values have a different configuration structure
        if check_name == "allowed_values":

            for column, allowed_values in columns.items():

                result = check_function(
                    rows,
                    column,
                    allowed_values,
                )

                results.append(result)

        else:

            for column in columns:

                result = check_function(
                    rows,
                    column,
                )

                results.append(result)

    return results
