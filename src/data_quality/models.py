
from dataclasses import dataclass, field


@dataclass
class CheckResult:
    name: str
    passed: bool
    records_affected: int
    message: str
    failed_records: list[dict] = field(default_factory=list)
