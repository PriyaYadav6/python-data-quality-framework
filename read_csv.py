import csv

allowed_values = ["IN", "DE", "US", "NL"]

with open(
    "data/orders.csv",
    "r",
    encoding="utf-8",
    newline=""
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        country = row["country"]

        if country not in allowed_values:
            print(
                f"Invalid country: {country} "
                f"| Order ID: {row['order_id']}"
            )