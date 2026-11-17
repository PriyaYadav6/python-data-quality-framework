
import argparse
import csv

from src.data_quality.config_loader import load_config
from src.data_quality.validator import run_validation


def main():

    parser = argparse.ArgumentParser(
        description="Python Data Quality Framework"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to YAML configuration file",
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    print(f"\nDataset: {config['dataset']}")

    # Load dataset
    data_path = f"data/{config['dataset']}.csv"

    with open(
        data_path,
        "r",
        newline="",
        encoding="utf-8",
    ) as file:

        reader = csv.DictReader(file)

        actual_columns = reader.fieldnames or []
        rows = list(reader)

    print(f"Total records: {len(rows)}")

    # Execute validation engine
    results = run_validation(
        rows,
        actual_columns,
        config,
    )

    # Display results
    print("\nDATA QUALITY REPORT")
    print("-" * 50)

    for result in results:

        status = "PASS" if result.passed else "FAIL"

        print(f"{result.name}: {status}")
        print(f"Records affected: {result.records_affected}")
        print(f"Message: {result.message}")

        if result.failed_records:

            print("\nInvalid Records:")

            for failed_record in result.failed_records:

                record = failed_record["record"]

                print(f"Order ID: {record.get('order_id')}")
                print(
                    f"Invalid Value: "
                    f"{failed_record['invalid_value']}"
                )
                print(
                    f"Expected Values: "
                    f"{', '.join(failed_record['expected_values'])}"
                )

        print("-" * 50)



if __name__ == "__main__":
    main()
