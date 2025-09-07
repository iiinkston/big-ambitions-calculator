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

from .electronics_store import (
    ELECTRONICS_FURNITURE,
    BUSINESS_LABEL as ELECTRONICS_LABEL,
    CATEGORY_COUNT as ELECTRONICS_CATEGORY_COUNT,
)

from .gift_store import (
    GIFT_STORE_FURNITURE,
    BUSINESS_LABEL as GIFT_STORE_LABEL,
    CATEGORY_COUNT as GIFT_STORE_CATEGORY_COUNT,
)

from .jewelry_store import (
    JEWELRY_STORE_FURNITURE,
    BUSINESS_LABEL as JEWELRY_LABEL,
    CATEGORY_COUNT as JEWELRY_CATEGORY_COUNT,
)

from .flower_store import (
    FLOWER_STORE_FURNITURE,
    BUSINESS_LABEL as FLOWER_LABEL,
    CATEGORY_COUNT as FLOWER_CATEGORY_COUNT,
)


# 各业务家具配置
BUSINESS_SPECS = {
    "bookstore": BOOKSTORE_FURNITURE,
    "clothing_store": CLOTHING_FURNITURE,
    "coffee_shop": COFFEE_SHOP_FURNITURE,
    "electronics_store": ELECTRONICS_FURNITURE,
    "gift_store": GIFT_STORE_FURNITURE,
    "jewelry_store": JEWELRY_STORE_FURNITURE,
    "flower_store": FLOWER_STORE_FURNITURE,
}

# 业务显示名称
BUSINESS_LABELS = {
    "bookstore": BOOKSTORE_LABEL,
    "clothing_store": CLOTHING_LABEL,
    "coffee_shop": COFFEE_SHOP_LABEL,
    "electronics_store": ELECTRONICS_LABEL,
    "gift_store": GIFT_STORE_LABEL,
    "jewelry_store": JEWELRY_LABEL,
    "flower_store": FLOWER_LABEL,
}

# 每个业务需要的品类数
CATEGORY_COUNT_BY_BUSINESS = {
    "bookstore": BOOKSTORE_CATEGORY_COUNT,
    "clothing_store": CLOTHING_CATEGORY_COUNT,
    "coffee_shop": COFFEE_SHOP_CATEGORY_COUNT,
    "electronics_store": ELECTRONICS_CATEGORY_COUNT,
    "gift_store": GIFT_STORE_CATEGORY_COUNT,
    "jewelry_store": JEWELRY_CATEGORY_COUNT,
    "flower_store": FLOWER_CATEGORY_COUNT,
}

# 各类建筑的客人容量（顾客/小时）
BUILDING_CAPACITY_PER_HOUR = {
    "A1": 15,
    "A2": 15,
    "C1": 30,
    "C2": 30,
    "D2": 40,
    "M1": 75,
    # TODO: 后续 office 等建筑在这里统一扩展
}
