from typing import List
from .furniture import Furniture

BUSINESS_LABEL = "快餐店"
CATEGORY_COUNT = 8  # 汉堡、薯条、热狗、冰淇淋、烤肉串、披萨、沙拉、汽水

FASTFOOD_STORE_FURNITURE: List[Furniture] = [
    # 基础
    Furniture(key="cash_register", name="收银机", capacity=20, group="checkout"),
    # 汉堡
    Furniture(
        key="industrial_grill_burger",
        name="工业烤架（汉堡）",
        capacity=20,
        group="shelf_burger",
    ),
    # 炸薯条
    Furniture(
        key="industrial_fryer",
        name="工业油炸机（薯条）",
        capacity=30,
        group="shelf_fries",
    ),
    # 热狗
    Furniture(key="hotdog_grill", name="热狗烤架", capacity=30, group="shelf_hotdog"),
    # 冰淇淋（两种家具可选，算法自动挑最优）
    Furniture(
        key="icecream_cabinet", name="冰淇淋柜", capacity=30, group="shelf_icecream"
    ),
    Furniture(
        key="small_freezer",
        name="小型工业冰柜（冰淇淋）",
        capacity=15,
        group="shelf_icecream",
    ),
    # 烤肉串
    Furniture(
        key="industrial_grill_kebab",
        name="工业烤架（烤肉串）",
        capacity=20,
        group="shelf_kebab",
    ),
    # 披萨
    Furniture(key="pizza_oven", name="比萨烤箱", capacity=20, group="shelf_pizza"),
    # 沙拉
    Furniture(key="salad_bar", name="沙拉台", capacity=20, group="shelf_salad"),
    # 汽水（两种家具可选）
    Furniture(key="fridge", name="饮料冰箱", capacity=20, group="shelf_drink"),
    Furniture(
        key="fridge_large", name="大型饮料冰箱", capacity=50, group="shelf_drink"
    ),
]
