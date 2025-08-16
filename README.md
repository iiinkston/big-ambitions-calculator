# Big Ambitions · 满流量最低家具计算器（Web）

一个可交互的 Flask 小应用。选择业务类型与建筑代码，输出在满流量下的**最低家具件数**与**最低人手**。

当前内置业务：**书店**（家具容量取自你提供的游戏内页面）。

## 运行

```bash
pip install -r requirements.txt
python app.py
# 浏览器打开 http://127.0.0.1:5000
```

## 扩展其它业务

在 `app.py` 中的 `BUSINESS_SPECS` 增加一个列表，按照：

- `group` 为功能组（如：`basket` / `checkout` / `shelf`），同组内会“按单一家具最省件数”覆盖建筑容量；
- `capacity` 为该家具的顾客容量（人/小时）；
- `name` 为显示名；

即可支持新的业态。
