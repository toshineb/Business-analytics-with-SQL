# 📊 Business Analytics Dashboard – Python + Streamlit + MySQL

Welcome to the **Business Analytics Dashboard** project — a professional-grade, interactive analytics application built with **Python, Streamlit, MySQL, and Plotly**.

Designed by a **data analyst and data scientist**, this dashboard connects to a live MySQL database, processes employee/customer data, and presents dynamic insights through **filterable charts, KPIs, and tables**. This project demonstrates **real-time business intelligence capabilities** ideal for executive decision-making.

---

## 📸 Dashboard Preview

![Business Dashboard Screenshot](./Screenshot%202025-07-04%20172422.png)

> The dashboard above features side filters, metric cards, pie and bar charts, and a tabular explorer — giving users full control over the insights they extract.

---

## 🎯 Project Purpose

This project was built to simulate an internal business reporting tool that allows HR, Finance, or Ops teams to explore metrics like:

- 🌍 Salary distribution by **department and country**
- 👥 Total employees/customers by **gender, unit, or region**
- 📈 KPIs such as **annual salary totals**, **max vs. min salary range**, and more
- 🔄 Fully **filterable interface** using department, country, and business unit

---

## 🧠 What Makes This Project Stand Out?

- ✅ **Live MySQL Integration** (via `mysql.connector`) for realistic data connectivity
- 🎨 **Streamlit UI** with sidebar filtering and custom-styled CSS
- 📊 **Plotly Express Visualizations** (bar, pie) that are intuitive and interactive
- 🧮 **Metrics Cards** powered by `streamlit_extras` to highlight key values
- 📂 **Tabular explorer** with customizable column selection and statistical summary

---

## 🧰 Tech Stack

| Tool             | Purpose                             |
|------------------|-------------------------------------|
| **Python**        | Data handling & dashboard backend   |
| **Streamlit**     | Frontend interface & interactivity  |
| **MySQL**         | Data storage & retrieval            |
| **Pandas**        | Data manipulation                   |
| **Plotly**        | Data visualization                  |
| **streamlit_extras** | UI Enhancements (metrics)       |

---

## 📁 File Structure

```bash
📦 business-dashboard/
├── Main.py               # Streamlit dashboard script
├── mysql_con.py          # MySQL connection & data fetch
├── style.css             # Custom CSS styling (optional)
├── requirements.txt      # Python dependencies
└── README.md             # Project overview
