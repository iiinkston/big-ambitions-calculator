from typing import Dict, List
from .furniture import Furniture

# 建筑容量（顾客/小时）
BUILDING_CAPACITY_PER_HOUR: Dict[str, int] = {
    "A1": 15,
    "A2": 15,
    "C1": 30,
    "C2": 30,
    "D2": 40,
    "M1": 75,
}

BOOKSTORE_FURNITURE: List[Furniture] = [
    Furniture(key="basket_stack", name="一叠购物篮", capacity=30, group="basket"),
    Furniture(
        key="checkout_counter", name="结账柜台（左/右）", capacity=30, group="checkout"
    ),
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    Furniture(key="bookshelf_large", name="书架（大）", capacity=50, group="shelf"),
    Furniture(key="bookshelf_small", name="书架（小）", capacity=20, group="shelf"),
]

BUSINESS_SPECS: Dict[str, List[Furniture]] = {
    "bookstore": BOOKSTORE_FURNITURE,
}
BUSINESS_LABELS = {"bookstore": "书店"}
CATEGORY_COUNT = 6  # 书架类别数
