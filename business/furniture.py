from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Furniture:
    key: str
    name: str
    capacity: int  # 顾客容量/小时
    group: str  # basket / checkout / shelf
