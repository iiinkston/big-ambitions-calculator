from typing import List
from .furniture import Furniture

BUSINESS_LABEL = "花店"
CATEGORY_COUNT = 4  # 廉价花卉、昂贵花卉、廉价礼品、昂贵礼品（汽水单独算）

FLOWER_STORE_FURNITURE: List[Furniture] = [
    # 基础设施
    Furniture(key="basket_stack", name="一叠购物篮", capacity=30, group="basket"),
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    Furniture(key="checkout_counter", name="结账柜台", capacity=30, group="checkout"),
    # 花卉/礼品 → 圆角货架
    Furniture(
        key="corner_shelf_flower_cheap",
        name="圆角货架（廉价花卉）",
        capacity=15,
        group="shelf_flower_cheap",
    ),
    Furniture(
        key="corner_shelf_flower_exp",
        name="圆角货架（昂贵花卉）",
        capacity=15,
        group="shelf_flower_exp",
    ),
    Furniture(
        key="corner_shelf_gift_cheap",
        name="圆角货架（廉价礼品）",
        capacity=15,
        group="shelf_gift_cheap",
    ),
    Furniture(
        key="corner_shelf_gift_exp",
        name="圆角货架（昂贵礼品）",
        capacity=15,
        group="shelf_gift_exp",
    ),
    # 汽水 → 冰箱
    Furniture(key="fridge", name="饮料冰箱", capacity=20, group="shelf_drink"),
    Furniture(
        key="fridge_large", name="大型饮料冰箱", capacity=50, group="shelf_drink"
    ),
]
