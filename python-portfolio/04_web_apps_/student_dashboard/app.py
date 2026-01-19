import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📊 Student Performance Dashboard")

# Sidebar upload
st.sidebar.header("📁 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload students.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("students.csv")

# Clean columns
df.columns = df.columns.str.strip().str.lower()

# Calculations
df["total"] = df[["maths", "science", "english"]].sum(axis=1)
df["average"] = df["total"] / 3

# Pass / Fail
df["result"] = df["average"].apply(lambda x: "Pass" if x >= 60 else "Fail")

# Grade logic


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


df["grade"] = df["average"].apply(assign_grade)

# Sidebar filter
st.sidebar.header("🔍 Filters")
selected_student = st.sidebar.selectbox(
    "Select Student",
    ["All"] + df["name"].tolist()
)

filtered_df = df if selected_student == "All" else df[df["name"]
                                                      == selected_student]

# Display table
st.subheader("📋 Student Performance Table")
st.dataframe(filtered_df, use_container_width=True)

# KPIs
st.subheader("📌 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Class Avg", round(df["average"].mean(), 2))
col2.metric("Highest Avg", round(df["average"].max(), 2))
col3.metric("Lowest Avg", round(df["average"].min(), 2))
col4.metric("Pass %", round((df["result"] == "Pass").mean() * 100, 2))

# Topper(s)
st.subheader("🏆 Top Performer(s)")
max_total = df["total"].max()
toppers = df[df["total"] == max_total]
st.dataframe(toppers[["name", "total", "average", "grade"]])

# Visualization
st.subheader("📊 Subject-wise Marks Comparison")
fig, ax = plt.subplots()
df.plot(x="name", y=["maths", "science", "english"], kind="bar", ax=ax)
plt.ylabel("Marks")
plt.xlabel("Students")
plt.xticks(rotation=45)
st.pyplot(fig)
