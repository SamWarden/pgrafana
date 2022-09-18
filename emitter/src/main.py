from dataclasses import asdict, dataclass, field
from datetime import datetime
import itertools
import json
import sys
import time
from typing import Any
import uuid


@dataclass
class Message:
    log_level: str
    request_id: str
    text: str
    additional_info: dict[str, Any]
    timestamp: int = field(init=False)
    time: str = field(init=False)

    def __post_init__(self):
        dt = datetime.now()
        self.timestamp = int(dt.timestamp())
        self.time = dt.isoformat()


def main() -> None:
    for level in itertools.cycle(("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")):
        message = Message(level, str(uuid.uuid4()), "Hello World", {"key": "value"})
        print(json.dumps(asdict(message)), file=sys.stderr)
        time.sleep(5)


if __name__ == "__main__":
    main()
