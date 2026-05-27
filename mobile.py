import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("mobile_usage.csv")

# Print dataset
print(df)

# -----------------------------
# LINE GRAPH
# -----------------------------

days = df["Day"]
hours = df["Hours"]

plt.plot(
    days,
    hours,
    marker="o",
    color="blue"
)

plt.title("Daily Mobile Usage")

plt.xlabel("Days")
plt.ylabel("Hours")

plt.show()

# -----------------------------
# BAR CHART
# -----------------------------

plt.bar(
    days,
    hours,
    color="green"
)

plt.title("Mobile Usage Bar Chart")

plt.xlabel("Days")
plt.ylabel("Hours")

plt.show()

# -----------------------------
# HISTOGRAM
# -----------------------------

plt.hist(
    hours,
    bins=5,
    color="orange",
    edgecolor="black"
)

plt.title("Usage Distribution")

plt.xlabel("Hours")
plt.ylabel("Frequency")

plt.show()