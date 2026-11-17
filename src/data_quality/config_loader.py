
import yaml
from pathlib import Path


def load_config(config_path: str) -> dict:

    path = Path(config_path)

    # Step 1: Check whether the file exists
    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    # Step 2: Read YAML configuration
    try:
        with open(path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

    except yaml.YAMLError as error:
        raise ValueError(
            f"Invalid YAML configuration: {error}"
        ) from error

    # Step 3: Validate configuration structure
    if not isinstance(config, dict):
        raise ValueError("Configuration must be a YAML dictionary")

    if not config.get("dataset"):
        raise ValueError("Dataset name is required")

    if not isinstance(config.get("required_columns"), list):
        raise ValueError("required_columns must be a list")

    if not isinstance(config.get("checks"), dict):
        raise ValueError("checks must be a dictionary")

    return config
