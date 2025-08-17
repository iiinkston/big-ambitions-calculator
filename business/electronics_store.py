from typing import List
from .furniture import Furniture

BUSINESS_LABEL = "电器商店"
CATEGORY_COUNT = 6  # 电器类别数

ELECTRONICS_FURNITURE: List[Furniture] = [
    Furniture(key="basket_stack", name="成叠的购物篮", capacity=30, group="basket"),
    Furniture(
        key="checkout_counter", name="结账柜台（左/右）", capacity=30, group="checkout"
    ),
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    Furniture(
        key="product_display_table", name="产品展示桌", capacity=10, group="shelf"
    ),
]
