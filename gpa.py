import streamlit as st

# App Title
st.title("CGPA Calculator")
st.write("This app calculates your CGPA based on the grades and units you input.")

# User Input Section
st.header("Enter Your Grades and Units")

# Input Number of Courses
num_courses = st.number_input("Enter the number of courses:", min_value=1, step=1)

# Grade Options
grade_options = ["A", "B", "C", "D", "E", "F"]

# Input Grades and Units
grades = []
units = []

st.write("Provide your grades and corresponding units:")
for i in range(num_courses):
    col1, col2 = st.columns(2)
    with col1:
        grade = st.selectbox(f"Grade for Course {i+1}:", grade_options, key=f"grade_{i}")
        grades.append(grade)
    with col2:
        unit = st.number_input(f"Unit for Course {i+1}:", min_value=1, key=f"unit_{i}")
        units.append(unit)

# Grade to Point Mapping
grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

# CGPA Calculation
if st.button("Calculate CGPA"):
    try:
        total_points = 0
        total_units = 0
        for grade, unit in zip(grades, units):
            points = grade_points[grade] * unit
            total_points += points
            total_units += unit

        cgpa = total_points / total_units if total_units > 0 else 0
        st.success(f"Your CGPA is: {cgpa:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")