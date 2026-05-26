# =========================================
# STUDENT PERFORMANCE ANALYSIS PROJECT
# =========================================

# STEP 1 — Import Library
import pandas as pd

# STEP 2 — Load Dataset
df = pd.read_csv("student_data.csv")

# =========================================
# BASIC DATA UNDERSTANDING
# =========================================

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nSTATISTICS SUMMARY")
print(df.describe())

# =========================================
# DATA CLEANING
# =========================================

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Remove duplicates if any
df = df.drop_duplicates()

# =========================================
# BASIC ANALYSIS
# =========================================

# Average final marks
print("\nAVERAGE FINAL GRADE")
print(df["G3"].mean())

# Highest final grade
print("\nHIGHEST FINAL GRADE")
print(df["G3"].max())

# Lowest final grade
print("\nLOWEST FINAL GRADE")
print(df["G3"].min())

# =========================================
# GENDER ANALYSIS
# =========================================

print("\nAVERAGE FINAL GRADE BY GENDER")
print(df.groupby("sex")["G3"].mean())

print("\nSTUDENT COUNT BY GENDER")
print(df["sex"].value_counts())

# =========================================
# STUDY TIME ANALYSIS
# =========================================

print("\nAVERAGE GRADE BASED ON STUDY TIME")
print(df.groupby("studytime")["G3"].mean())

# =========================================
# PARENT EDUCATION ANALYSIS
# =========================================

print("\nMOTHER EDUCATION VS FINAL GRADE")
print(df.groupby("Medu")["G3"].mean())

print("\nFATHER EDUCATION VS FINAL GRADE")
print(df.groupby("Fedu")["G3"].mean())

# =========================================
# ABSENCE ANALYSIS
# =========================================

print("\nAVERAGE ABSENCES")
print(df["absences"].mean())

print("\nSTUDENTS WITH HIGH ABSENCES")
print(df[df["absences"] > 15][["sex", "age", "absences", "G3"]])

# =========================================
# TOP STUDENTS
# =========================================

print("\nTOP 10 STUDENTS")
top_students = df.sort_values("G3", ascending=False)

print(top_students.head(10))

# =========================================
# LOWEST PERFORMING STUDENTS
# =========================================

print("\nLOWEST 10 STUDENTS")
low_students = df.sort_values("G3")

print(low_students.head(10))

# =========================================
# CREATE NEW COLUMN
# =========================================

# Total internal marks
df["total"] = df["G1"] + df["G2"] + df["G3"]

# Average marks
df["average"] = df["total"] / 3

print("\nNEW COLUMNS CREATED")
print(df[["G1", "G2", "G3", "total", "average"]].head())

# =========================================
# STUDENTS ABOVE AVERAGE
# =========================================

print("\nSTUDENTS WITH AVERAGE ABOVE 15")

high_avg = df[df["average"] > 15]

print(high_avg[["sex", "age", "average"]])

# =========================================
# SORTING
# =========================================

print("\nTOP 5 STUDENTS BASED ON AVERAGE")

print(df.sort_values("average", ascending=False).head())

# =========================================
# FINAL INSIGHTS
# =========================================

print("\n========== PROJECT INSIGHTS ==========")

print("1. Average Final Grade :", df["G3"].mean())

print("2. Highest Final Grade :", df["G3"].max())

print("3. Lowest Final Grade :", df["G3"].min())

print("4. Total Students :", len(df))

print("5. Male/Female Count")
print(df["sex"].value_counts())

print("6. Study Time Impact")
print(df.groupby("studytime")["G3"].mean())

print("7. Parent Education Impact")
print(df.groupby("Medu")["G3"].mean())

print("========== PROJECT COMPLETED ==========")