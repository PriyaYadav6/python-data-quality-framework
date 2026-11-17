
from src.data_quality.checks import (
    check_required_columns,
    check_nulls,
    check_duplicates,
    check_positive_values,
    check_allowed_values,
)


def test_required_columns_pass():

    actual = ["order_id", "customer_id", "amount"]
    required = ["order_id", "customer_id"]

    result = check_required_columns(actual, required)

    assert result.passed is True
    assert result.records_affected == 0


def test_required_columns_fail():

    actual = ["order_id", "amount"]
    required = ["order_id", "customer_id"]

    result = check_required_columns(actual, required)

    assert result.passed is False
    assert "customer_id" in result.message


def test_null_check_fail():

    rows = [
        {"customer_id": "C101"},
        {"customer_id": ""},
        {"customer_id": "C103"},
    ]

    result = check_nulls(rows, "customer_id")

    assert result.passed is False
    assert result.records_affected == 1


def test_duplicate_check_fail():

    rows = [
        {"order_id": "101"},
        {"order_id": "102"},
        {"order_id": "101"},
    ]

    result = check_duplicates(rows, "order_id")

    assert result.passed is False
    assert result.records_affected == 1


def test_positive_values_pass():

    rows = [
        {"amount": "100"},
        {"amount": "200"},
    ]

    result = check_positive_values(rows, "amount")

    assert result.passed is True


def test_positive_values_fail():

    rows = [
        {"amount": "100"},
        {"amount": "-50"},
    ]

    result = check_positive_values(rows, "amount")

    assert result.passed is False
    assert result.records_affected == 1


def test_allowed_values_fail():

    rows = [
        {"country": "IN"},
        {"country": "UAE"},
    ]

    result = check_allowed_values(
        rows,
        "country",
        ["IN", "DE", "US", "NL"],
    )

    assert result.passed is False
    assert result.records_affected == 1
def test_null_check_detects_whitespace():
    rows = [
        {"customer_id": "C101"},
        {"customer_id": "   "},
    ]

    result = check_nulls(rows, "customer_id")

    assert result.passed is False
    assert result.records_affected == 1


def test_positive_check_detects_non_numeric_value():
    rows = [
        {"amount": "100"},
        {"amount": "abc"},
    ]

    result = check_positive_values(rows, "amount")

    assert result.passed is False
    assert result.records_affected == 1

def test_allowed_values_detects_missing_column():
    rows = [
        {"country": "IN"},
        {"country": "DE"},
        {"order_id": "103"},
    ]

    result = check_allowed_values(
        rows,
        "country",
        ["IN", "DE", "US", "NL"],
    )

    assert result.passed is False
    assert result.records_affected == 0
    assert "missing" in result.message.lower()