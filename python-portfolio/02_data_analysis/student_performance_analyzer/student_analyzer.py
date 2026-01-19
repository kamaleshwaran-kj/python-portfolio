import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Calculate total and average
df["total"] = df[["maths", "science", "english"]].sum(axis=1)
df["average"] = df["total"] / 3

# Pass / Fail logic
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

# Display final data
print("\n--- Final Student Performance Report ---")
print(df)

# Class average
print("\nClass Average Marks:")
print(df[["maths", "science", "english"]].mean())

# Top performer
max_total = df["total"].max()
toppers = df[df["total"] == max_total]

print("\n🏆 Top Performer(s):")
print(toppers[["name", "total", "average", "grade"]])


# Save analyzed results
df.to_csv("student_results.csv", index=False)
print("\n📁 Results saved to student_results.csv")

# Visualization
df.plot(x="name", y=["maths", "science", "english"], kind="bar")
plt.title("Student Marks Comparison")
plt.ylabel("Marks")
plt.xlabel("Students")
plt.tight_layout()
plt.show()
