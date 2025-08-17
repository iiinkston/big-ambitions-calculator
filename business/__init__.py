from .bookstore import (
    BOOKSTORE_FURNITURE,
    BUSINESS_LABEL as BOOKSTORE_LABEL,
    CATEGORY_COUNT as BOOKSTORE_CATEGORY_COUNT,
)
from .clothing_store import (
    CLOTHING_FURNITURE,
    BUSINESS_LABEL as CLOTHING_LABEL,
    CATEGORY_COUNT as CLOTHING_CATEGORY_COUNT,
)

from .coffee_shop import (
    COFFEE_SHOP_FURNITURE,
    BUSINESS_LABEL as COFFEE_SHOP_LABEL,
    CATEGORY_COUNT as COFFEE_SHOP_CATEGORY_COUNT,
)

# 各业务家具配置
BUSINESS_SPECS = {
    "bookstore": BOOKSTORE_FURNITURE,
    "clothing_store": CLOTHING_FURNITURE,
    "coffee_shop": COFFEE_SHOP_FURNITURE,
}

# 业务显示名称
BUSINESS_LABELS = {
    "bookstore": BOOKSTORE_LABEL,
    "clothing_store": CLOTHING_LABEL,
    "coffee_shop": COFFEE_SHOP_LABEL,
}

# 每个业务需要的品类数
CATEGORY_COUNT_BY_BUSINESS = {
    "bookstore": BOOKSTORE_CATEGORY_COUNT,
    "clothing_store": CLOTHING_CATEGORY_COUNT,
    "coffee_shop": COFFEE_SHOP_CATEGORY_COUNT,
}

# 各类建筑的客人容量（顾客/小时）
BUILDING_CAPACITY_PER_HOUR = {
    "A1": 15,
    "A2": 15,
    "C1": 30,
    "C2": 30,
    "D2": 40,
    "M1": 75,
    # 后续 office 等建筑在这里统一扩展
}
