from typing import List
from .furniture import Furniture

BUSINESS_LABEL = "服装店"
CATEGORY_COUNT = 8  # 经典/现代 × 廉价/昂贵 × 男女

CLOTHING_FURNITURE: List[Furniture] = [
    Furniture(key="basket_stack", name="一叠购物篮", capacity=30, group="basket"),
    Furniture(
        key="checkout_counter", name="结账柜台（左/右）", capacity=30, group="checkout"
    ),
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    Furniture(key="rack_large", name="衣架", capacity=10, group="shelf"),
    Furniture(key="rack_slanted", name="斜向衣架", capacity=5, group="shelf"),
]
