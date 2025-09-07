from typing import List
from .furniture import Furniture

BUSINESS_LABEL = "礼品店"
CATEGORY_COUNT = 5  # 廉价礼品、昂贵礼品、廉价花卉、昂贵花卉、碳酸汽水

GIFT_STORE_FURNITURE: List[Furniture] = [
    # 基础
    Furniture(key="basket_stack", name="一叠购物篮", capacity=30, group="basket"),
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    Furniture(key="checkout_counter", name="结账柜台", capacity=30, group="checkout"),
    # 礼品
    Furniture(
        key="corner_shelf_gift_cheap",
        name="圆角货架（廉价礼品）",
        capacity=15,
        group="shelf_gift_cheap",
    ),
    Furniture(
        key="corner_shelf_gift_expensive",
        name="圆角货架（昂贵礼品）",
        capacity=15,
        group="shelf_gift_expensive",
    ),
    # 花卉
    Furniture(
        key="corner_shelf_flower_cheap",
        name="圆角货架（廉价花卉）",
        capacity=15,
        group="shelf_flower_cheap",
    ),
    Furniture(
        key="corner_shelf_flower_expensive",
        name="圆角货架（昂贵花卉）",
        capacity=15,
        group="shelf_flower_expensive",
    ),
    # 汽水
    Furniture(key="fridge", name="饮料冰箱", capacity=20, group="shelf_drink"),
    Furniture(
        key="fridge_large", name="大型饮料冰箱", capacity=50, group="shelf_drink"
    ),
]
