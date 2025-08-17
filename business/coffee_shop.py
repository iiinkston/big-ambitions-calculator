from typing import List
from .furniture import Furniture

BUSINESS_LABEL = "咖啡店"
CATEGORY_COUNT = 4  # 羊角面包、杯装咖啡、纸杯蛋糕、甜甜圈

COFFEE_SHOP_FURNITURE: List[Furniture] = [
    Furniture(key="tray_stack", name="一叠托盘", capacity=25, group="basket"),
    Furniture(key="checkout_counter", name="点单柜台", capacity=30, group="checkout"),
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    Furniture(
        key="display_case", name="面包展示柜", capacity=20, group="shelf_bakery"
    ),  # 羊角面包/纸杯蛋糕/甜甜圈 → 顾客容量 20
    Furniture(
        key="coffee_machine", name="工业咖啡机", capacity=30, group="shelf_coffee"
    ),  # 杯装咖啡 → 顾客容量 30
]
