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

    # 获取当前业务需要的品类数
    category_count = CATEGORY_COUNT_BY_BUSINESS.get(business, 1)

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
                        "subtotal_capacity": it["subtotal_capacity"] * category_count,
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
