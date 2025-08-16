from flask import Flask, render_template, request
from business.bookstore import (
    BUSINESS_SPECS,
    BUSINESS_LABELS,
    BUILDING_CAPACITY_PER_HOUR,
)
from business.planner import compute_min_setup

app = Flask(__name__)


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
