from flask import Flask, render_template, request
from business import BUSINESS_SPECS, BUSINESS_LABELS, BUILDING_CAPACITY_PER_HOUR
from business.planner import compute_min_setup

app = Flask(__name__)

# 建筑分类
RETAIL_BUILDINGS = ["A1", "A2", "C1", "C2", "D2", "M1"]
OFFICE_BUILDINGS = ["A3", "C1", "C2", "D2", "K1"]

# 业务分类
BUSINESS_CATEGORY = {
    # 零售类
    "bookstore": "retail",
    "clothing_store": "retail",
    "coffee_shop": "retail",
    "electronics_store": "retail",
    "fast_food": "retail",
    "florist": "retail",
    "fruit_store": "retail",
    "gift_shop": "retail",
    "gym": "retail",
    "hairdresser": "retail",
    "jewelry_store": "retail",
    "liquor_store": "retail",
    "nightclub": "retail",
    "supermarket": "retail",
    # 办公室类
    "law_firm": "office",
    "accounting_firm": "office",
}


def get_available_buildings(business: str):
    """根据业务返回可用建筑代码"""
    category = BUSINESS_CATEGORY.get(business, "retail")
    return RETAIL_BUILDINGS if category == "retail" else OFFICE_BUILDINGS


@app.route("/", methods=["GET", "POST"])
def index():
    business = request.form.get("business", "bookstore")
    available_buildings = get_available_buildings(business)

    # 默认选第一个可用建筑
    building = request.form.get("building") or available_buildings[0]

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
        building_keys=available_buildings,  # 按业务过滤
        building_caps=BUILDING_CAPACITY_PER_HOUR,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
