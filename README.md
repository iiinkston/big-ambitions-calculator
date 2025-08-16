# Big Ambitions Capacity Calculator

一个用于 **自动计算店铺最优布局方案** 的交互式应用，基于 **Flask + Python** 构建，并已部署在 Render 上。  
通过输入建筑类型，系统会自动计算所需的书架、收银台、购物篮等家具数量，以及最少所需员工数。

---

## 在线演示
你可以直接在浏览器中访问本应用：  
[Big Ambitions Calculator - Live Demo](https://big-ambitions-calculator.onrender.com/)

---

## 功能特点
- 输入店铺建筑类型（如 A1, A2, C1, C2, D2, M1）  
- 自动计算目标容量下的最佳家具组合  
- 优化规则：  
  - 尽量减少家具总数量  
  - 总容量尽量接近目标，不会过多浪费  
- 结账区（收银机/柜台）自动合并选择最佳方案  
- 自动计算最少所需员工人数  

---

## 技术栈
- **后端**: [Flask](https://flask.palletsprojects.com/)  
- **部署**: [Render](https://render.com/)  
- **语言**: Python 3.13  

---

## 本地运行
如果你想在本地运行该应用，可以按照以下步骤操作：

```bash
# 克隆仓库
git clone https://github.com/iiinkston/big-ambitions-calculator.git
cd big-ambitions-calculator

# 建立虚拟环境
python -m venv .venv
source .venv/bin/activate   # Windows 使用: .venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动应用
python app.py
