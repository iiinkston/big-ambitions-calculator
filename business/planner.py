from math import ceil
from typing import Dict, List
from .furniture import Furniture
from . import (
    BUSINESS_SPECS,
    BUSINESS_LABELS,
    CATEGORY_COUNT_BY_BUSINESS,
    BUILDING_CAPACITY_PER_HOUR,
)


def pick_min_combo_for_group(target: int, options: List[Furniture]):
    caps = [o.capacity for o in options]
    names = [o.name for o in options]
    keys = [o.key for o in options]

    max_each = ceil(target / min(caps)) + 3
    best = None
    counts = [0] * len(options)

    def dfs(i, cur_count, cur_cap):
        nonlocal best
        if best and cur_count > best[0]:
            return
        if cur_cap >= target:
            cand = (cur_count, cur_cap, counts.copy())
            if (
                best is None
                or cand[0] < best[0]
                or (cand[0] == best[0] and cand[1] < best[1])
            ):
                best = cand
            return
        if i == len(options):
            return
        for n in range(0, max_each + 1):
            counts[i] = n
            dfs(i + 1, cur_count + n, cur_cap + n * caps[i])
        counts[i] = 0

    dfs(0, 0, 0)

    if best is None:
        best = (10**9, 10**9, None)
        for idx, cap in enumerate(caps):
            n = ceil(target / cap)
            cand = (n, n * cap, [0] * len(options))
            cand[2][idx] = n
            if (cand[0] < best[0]) or (cand[0] == best[0] and cand[1] < best[1]):
                best = cand

    total_count, total_cap, best_counts = best
    combo = []
    for i, n in enumerate(best_counts):
        if n > 0:
            combo.append(
                {
                    "furniture_name": names[i],
                    "furniture_key": keys[i],
                    "each_capacity": caps[i],
                    "count": n,
                    "subtotal_capacity": n * caps[i],
                }
            )
    return {"total_count": total_count, "total_capacity": total_cap, "combo": combo}


def compute_min_setup(business: str, building_code: str):
    if business not in BUSINESS_SPECS:
        raise ValueError("暂不支持该业务类型")
    if building_code not in BUILDING_CAPACITY_PER_HOUR:
        raise ValueError("未知建筑代码")

    target = BUILDING_CAPACITY_PER_HOUR[building_code]
    groups: Dict[str, List[Furniture]] = {}
    for f in BUSINESS_SPECS[business]:
        groups.setdefault(f.group, []).append(f)

    plan = []
    checkout_points = 0

    # 默认分类数（书店/服装店用）
    category_count = CATEGORY_COUNT_BY_BUSINESS.get(business, 1)

    # --- 咖啡店逻辑 ---
    if business == "coffee_shop":
        # 面包展示柜：3个品类
        best_bakery = pick_min_combo_for_group(target, groups.get("shelf_bakery", []))
        total_count = best_bakery["total_count"] * 3
        total_capacity = best_bakery["total_capacity"] * 3
        combo = []
        for it in best_bakery["combo"]:
            combo.append(
                {
                    "furniture_name": it["furniture_name"],
                    "furniture_key": it["furniture_key"],
                    "each_capacity": it["each_capacity"],
                    "count": it["count"] * 3,
                    "subtotal_capacity": it["subtotal_capacity"] * 3,
                }
            )
        plan.append(
            {
                "group": "面包展示柜",
                "total_capacity": total_capacity,
                "total_count": total_count,
                "combo": combo,
            }
        )

        # 工业咖啡机
        best_coffee = pick_min_combo_for_group(target, groups.get("shelf_coffee", []))
        plan.append(
            {
                "group": "工业咖啡机",
                "total_capacity": best_coffee["total_capacity"],
                "total_count": best_coffee["total_count"],
                "combo": best_coffee["combo"],
            }
        )

        # 收银 / 托盘
        for gname, opts in groups.items():
            if gname in ["basket", "checkout"]:
                best = pick_min_combo_for_group(target, opts)
                plan.append(
                    {
                        "group": gname,
                        "total_capacity": best["total_capacity"],
                        "total_count": best["total_count"],
                        "combo": best["combo"],
                    }
                )
                if gname == "checkout":
                    checkout_points = best["total_count"]

    # --- 礼品店逻辑 ---
    elif business == "gift_store":
        # 廉价礼品
        best_gift_cheap = pick_min_combo_for_group(
            target, groups.get("shelf_gift_cheap", [])
        )
        plan.append(
            {
                "group": "廉价礼品",
                "total_capacity": best_gift_cheap["total_capacity"],
                "total_count": best_gift_cheap["total_count"],
                "combo": best_gift_cheap["combo"],
            }
        )

        # 昂贵礼品
        best_gift_expensive = pick_min_combo_for_group(
            target, groups.get("shelf_gift_expensive", [])
        )
        plan.append(
            {
                "group": "昂贵礼品",
                "total_capacity": best_gift_expensive["total_capacity"],
                "total_count": best_gift_expensive["total_count"],
                "combo": best_gift_expensive["combo"],
            }
        )

        # 廉价花卉
        best_flower_cheap = pick_min_combo_for_group(
            target, groups.get("shelf_flower_cheap", [])
        )
        plan.append(
            {
                "group": "廉价花卉",
                "total_capacity": best_flower_cheap["total_capacity"],
                "total_count": best_flower_cheap["total_count"],
                "combo": best_flower_cheap["combo"],
            }
        )

        # 昂贵花卉
        best_flower_expensive = pick_min_combo_for_group(
            target, groups.get("shelf_flower_expensive", [])
        )
        plan.append(
            {
                "group": "昂贵花卉",
                "total_capacity": best_flower_expensive["total_capacity"],
                "total_count": best_flower_expensive["total_count"],
                "combo": best_flower_expensive["combo"],
            }
        )

        # 汽水
        best_drink = pick_min_combo_for_group(target, groups.get("shelf_drink", []))
        plan.append(
            {
                "group": "碳酸汽水",
                "total_capacity": best_drink["total_capacity"],
                "total_count": best_drink["total_count"],
                "combo": best_drink["combo"],
            }
        )

        # 收银 / 购物篮
        for gname, opts in groups.items():
            if gname in ["basket", "checkout"]:
                best = pick_min_combo_for_group(target, opts)
                plan.append(
                    {
                        "group": gname,
                        "total_capacity": best["total_capacity"],
                        "total_count": best["total_count"],
                        "combo": best["combo"],
                    }
                )
                if gname == "checkout":
                    checkout_points = best["total_count"]

    # --- 其他通用逻辑（书店、服装店、电器商店等） ---
    else:
        for gname, opts in groups.items():
            if gname == "shelf":
                best = pick_min_combo_for_group(target, opts)
                total_count = best["total_count"] * category_count
                total_capacity = best["total_capacity"] * category_count
                combo = []
                for it in best["combo"]:
                    combo.append(
                        {
                            "furniture_name": it["furniture_name"],
                            "furniture_key": it["furniture_key"],
                            "each_capacity": it["each_capacity"],
                            "count": it["count"] * category_count,
                            "subtotal_capacity": it["subtotal_capacity"]
                            * category_count,
                        }
                    )
                plan.append(
                    {
                        "group": gname,
                        "total_capacity": total_capacity,
                        "total_count": total_count,
                        "combo": combo,
                    }
                )
            else:
                best = pick_min_combo_for_group(target, opts)
                plan.append(
                    {
                        "group": gname,
                        "total_capacity": best["total_capacity"],
                        "total_count": best["total_count"],
                        "combo": best["combo"],
                    }
                )
                if gname == "checkout":
                    checkout_points = best["total_count"]

    employees_min = checkout_points + 1
    return {
        "target": target,
        "plan": plan,
        "employees_min": employees_min,
        "business_label": BUSINESS_LABELS[business],
    }
