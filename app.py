#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import ceil
from dataclasses import dataclass
from typing import Dict, List
from flask import Flask, render_template, request

app = Flask(__name__)

# ----------------------------
# 建筑容量（顾客/小时）
# ----------------------------
BUILDING_CAPACITY_PER_HOUR: Dict[str, int] = {
    "A1": 15,
    "A2": 15,
    "C1": 30,
    "C2": 30,
    "D2": 40,
    "M1": 75,
}

# ----------------------------
# 家具定义（书店）
# ----------------------------
@dataclass(frozen=True)
class Furniture:
    key: str
    name: str
    capacity: int  # 顾客容量/小时
    group: str     # basket / checkout / shelf

BOOKSTORE_FURNITURE: List[Furniture] = [
    Furniture(key="basket_stack",     name="一叠购物篮",     capacity=30, group="basket"),
    Furniture(key="checkout_counter", name="结账柜台（左/右）", capacity=30, group="checkout"),
    Furniture(key="cash_register",    name="收银机",         capacity=20, group="checkout"),
    Furniture(key="bookshelf_large",  name="书架（大）",     capacity=50, group="shelf"),
    Furniture(key="bookshelf_small",  name="书架（小）",     capacity=20, group="shelf"),
]

BUSINESS_SPECS: Dict[str, List[Furniture]] = {
    "bookstore": BOOKSTORE_FURNITURE,
}
BUSINESS_LABELS = {"bookstore": "书店"}

CATEGORY_COUNT = 6  # 书架类别数

# ----------------------------
# 通用组合求解：找出最少件数，若相同则总容量更小的解
# ----------------------------
def pick_min_combo_for_group(target: int, options: List[Furniture]):
    caps = [o.capacity for o in options]
    names = [o.name for o in options]
    keys  = [o.key for o in options]

    max_each = ceil(target / min(caps)) + 3
    best = None  # (件数, 总容量, counts)

    counts = [0]*len(options)

    def dfs(i, cur_count, cur_cap):
        nonlocal best
        if best and cur_count > best[0]:
            return
        if cur_cap >= target:
            cand = (cur_count, cur_cap, counts.copy())
            if (best is None or
                cand[0] < best[0] or
                (cand[0] == best[0] and cand[1] < best[1])):
                best = cand
            return
        if i == len(options):
            return
        for n in range(0, max_each+1):
            counts[i] = n
            dfs(i+1, cur_count+n, cur_cap+n*caps[i])
        counts[i] = 0

    dfs(0,0,0)

    if best is None:
        # 兜底：单一类型
        best = (10**9, 10**9, None)
        for idx, cap in enumerate(caps):
            n = ceil(target/cap)
            cand = (n, n*cap, [0]*len(options))
            cand[2][idx] = n
            if (cand[0]<best[0]) or (cand[0]==best[0] and cand[1]<best[1]):
                best = cand

    total_count, total_cap, best_counts = best
    combo = []
    for i,n in enumerate(best_counts):
        if n>0:
            combo.append({
                "furniture_name": names[i],
                "furniture_key": keys[i],
                "each_capacity": caps[i],
                "count": n,
                "subtotal_capacity": n*caps[i],
            })
    return {"total_count": total_count, "total_capacity": total_cap, "combo": combo}

# ----------------------------
# 计算整店方案
# ----------------------------
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

    for gname, opts in groups.items():
        if gname == "shelf":
            # 每个类别都必须独立达标 → 总数乘以类别数
            best = pick_min_combo_for_group(target, opts)
            total_count = best["total_count"] * CATEGORY_COUNT
            total_capacity = best["total_capacity"] * CATEGORY_COUNT
            combo = []
            for it in best["combo"]:
                combo.append({
                    "furniture_name": it["furniture_name"],
                    "furniture_key": it["furniture_key"],
                    "each_capacity": it["each_capacity"],
                    "count": it["count"] * CATEGORY_COUNT,
                    "subtotal_capacity": it["subtotal_capacity"] * CATEGORY_COUNT,
                })
            plan.append({
                "group": gname,
                "total_capacity": total_capacity,
                "total_count": total_count,
                "combo": combo,
            })
        else:
            best = pick_min_combo_for_group(target, opts)
            plan.append({
                "group": gname,
                "total_capacity": best["total_capacity"],
                "total_count": best["total_count"],
                "combo": best["combo"],
            })
            if gname == "checkout":
                checkout_points = best["total_count"]

    employees_min = checkout_points + 1
    return {"target": target, "plan": plan, "employees_min": employees_min}

# ----------------------------
# Web 路由
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    business = request.form.get("business", "bookstore")
    building = request.form.get("building", "C2")
    result = None
    if request.method == "POST":
        result = compute_min_setup(business, building)
    return render_template(
        "index.html",
        business=business,
        building=building,
        result=result,
        business_labels=BUSINESS_LABELS,
        business_keys=list(BUSINESS_SPECS.keys()),
        building_keys=list(BUILDING_CAPACITY_PER_HOUR.keys()),
        building_caps=BUILDING_CAPACITY_PER_HOUR,
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
