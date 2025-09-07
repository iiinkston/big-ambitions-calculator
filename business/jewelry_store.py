from typing import List
from .furniture import Furniture

BUSINESS_LABEL = "珠宝店"
CATEGORY_COUNT = 4  # 廉价珠宝、昂贵珠宝、雅鱼手表、赞纳手表

JEWELRY_STORE_FURNITURE: List[Furniture] = [
    Furniture(key="basket_stack", name="一叠购物篮", capacity=30, group="basket"),
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    Furniture(key="checkout_counter", name="结账柜台", capacity=30, group="checkout"),
    # 珠宝类
    Furniture(
        key="jewelry_display_cheap",
        name="珠宝展示柜（廉价）",
        capacity=15,
        group="shelf_jewelry_cheap",
    ),
    Furniture(
        key="jewelry_display_exp",
        name="珠宝展示柜（昂贵）",
        capacity=15,
        group="shelf_jewelry_exp",
    ),
    # 手表类
    Furniture(
        key="watch_display_yayu",
        name="产品展示桌（雅鱼手表）",
        capacity=10,
        group="shelf_watch_yayu",
    ),
    Furniture(
        key="watch_display_zana",
        name="产品展示桌（赞纳手表）",
        capacity=10,
        group="shelf_watch_zana",
    ),
]
