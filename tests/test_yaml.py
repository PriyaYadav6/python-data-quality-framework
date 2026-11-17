
from src.data_quality.config_loader import load_config


def test_yaml_configuration_loads_successfully():

    config = load_config("config/rules.yml")

    assert config is not None
    assert config["dataset"] == "orders"


def test_required_columns_exist():

    config = load_config("config/rules.yml")

    assert "order_id" in config["required_columns"]
    assert "customer_id" in config["required_columns"]


def test_validation_rules_exist():

    config = load_config("config/rules.yml")

    checks = config["checks"]

    assert "not_null" in checks
    assert "unique" in checks
    assert "positive" in checks
    assert "allowed_values" in checks


def test_allowed_country_values():

    config = load_config("config/rules.yml")

    allowed_countries = config["checks"]["allowed_values"]["country"]

    assert "IN" in allowed_countries
    assert "DE" in allowed_countries
    assert "US" in allowed_countries
    assert "NL" in allowed_countries
