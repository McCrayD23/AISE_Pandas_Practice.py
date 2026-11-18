import pandas as pd
import matplotlib.pyplot as plt

data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.dtypes)
print(df.describe())

# 1. How many students are in each course:
students_per_course = df.groupby("course")["student"].count()
print("\n1. Students per course:")
print(students_per_course)

# 2. Average score per course
avg_score_per_course = df.groupby("course")["score"].mean()
print("\n2. Average score per course:")
print(avg_score_per_course)

# 3. Top 3 students by score
top_3_students = df.sort_values("score", ascending=False).loc[0:3]
print("\n3. Top 3 students by score:")
print(top_3_students[["student", "course", "score"]])

# 4. Avg hours studied for students who passed vs. who didn't pass
avg_hours_passed = df.groupby("passed")["hours_studied"].mean()
print("\n4. Average hours studied for student who passed vs. who didn't pass:")
print(avg_hours_passed)

# 5. Create a "grade" column: 90+ = "A", 80-89= "B", 70-79 = "C", below 70 = "F"
df["grade"] = "F"   # Starts everyone at "F", then overwrite higher brackets
df.loc[(df["score"] >= 70) &(df["score"] <= 79), "grade"] = "C"
df.loc[(df["score"] >= 80) & (df["score"] <= 89), "grade"] = "B"
df.loc[df["score"] >= 90, "grade"] = "A"

print("\n5. DataFrame with new grade column:")
print(df[["student", "score", "grade"]])

# 6. Distribution of grades per course + MatPlotlib chart
grade_dist = df.groupby(["course", "grade"], observed=False)["student"].count()
print("\n6. Distribution of grades per course:")
print(grade_dist)