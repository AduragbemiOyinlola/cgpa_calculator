import streamlit as st

# App Title and Description
st.title("CGPA Calculator")
st.write("This app calculates your CGPA based on the grades and units you input.")

# User Input Section
col1, col2 = st.columns(2)
with col1:
    year = st.number_input("What year?", min_value=1, max_value=7, step=1)
with col2:
    semester = st.number_input("What semester?", min_value=1, max_value=2)

# Grade Options
grade_options = ["A", "B", "C", "D", "E", "F"]

# Input Grades and Units
grades_sem1 = []
units_sem1 = []
# Input Grades and Units
grades_sem2 = []
units_sem2 = []

# GPA per Semester
gpa_per_semester = []

def get_grades_units(year_label):
    # Columns for First Semester and Second Semester
    col1, col2 = st.columns(2)

    # Grade to Point Mapping
    grade_points = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 0
    }

     # GPA Calculation Function
    def calculate_gpa(semester_grades, semester_units):
        total_points = 0
        total_units = 0
        for grade, unit in zip(semester_grades, semester_units):
            points = grade_points[grade] * unit
            total_points += points
            total_units += unit
        return total_points / total_units if total_units > 0 else 0

    with col1:
        st.subheader("First Semester")
        num_courses_sem1 = st.number_input(
            f"Number of Courses (First Semester - {year_label}):", min_value=1, step=1, key=f"num_courses_sem1_{year_label}"
        )

        for i in range(int(num_courses_sem1)):
            grade = st.selectbox(
                f"Grade for Course {i + 1} (First Semester - {year_label}):",
                grade_options,
                key=f"sem1_grade_{year_label}_{i}",
            )
            unit = st.number_input(
                f"Unit for Course {i + 1} (First Semester - {year_label}):",
                min_value=1,
                key=f"sem1_unit_{year_label}_{i}",
            )
            grades_sem1.append(grade)
            units_sem1.append(unit)

            gpa_sem1 = calculate_gpa(grades_sem1, units_sem1)
            gpa_per_semester.append(gpa_sem1)

    with col2:
        st.subheader("Second Semester")
        num_courses_sem2 = st.number_input(
            f"Number of Courses (Second Semester - {year_label}):", min_value=1, step=1, key=f"num_courses_sem2_{year_label}"
        )

        for i in range(int(num_courses_sem2)):
            grade = st.selectbox(
                f"Grade for Course {i + 1} (Second Semester - {year_label}):",
                grade_options,
                key=f"sem2_grade_{year_label}_{i}",
            )
            unit = st.number_input(
                f"Unit for Course {i + 1} (Second Semester - {year_label}):",
                min_value=1,
                key=f"sem2_unit_{year_label}_{i}",
            )
            grades_sem2.append(grade)
            units_sem2.append(unit)

            gpa_sem2 = calculate_gpa(grades_sem2, units_sem2)
            gpa_per_semester.append(gpa_sem2)
        
# Combination of Year and Semester
if semester == 2:
    for i in range(1, year+1):
        st.header(f"Year {i}")
        get_grades_units(f"Year {i}")

elif semester == 1 and year > 1:
    for i in range(1, year):
        st.header(f"Year {i}")
        get_grades_units(f"Year {i}")

    st.header(f"Year {year}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("First Semester")
        num_courses_sem1 = st.number_input(
            "Number of Courses (First Semester):", min_value=1, step=1, key="num_courses_sem1"
        )
        for i in range(int(num_courses_sem1)):
            grade = st.selectbox(
                f"Grade for Course {i + 1} (First Semester):", grade_options, key=f"sem1_grade_{i}"
            )
            grades_sem1.append(grade)
            unit = st.number_input(
                f"Unit for Course {i + 1} (First Semester):", min_value=1, key=f"sem1_unit_{i}"
            )
            units_sem1.append(unit)

else:
    st.header(f"Year {year}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("First Semester")
        num_courses_sem1 = st.number_input(
            "Number of Courses (First Semester):", min_value=1, step=1, key="num_courses_sem1"
        )
        for i in range(int(num_courses_sem1)):
            grade = st.selectbox(
                f"Grade for Course {i + 1} (First Semester):", grade_options, key=f"sem1_grade_{i}"
            )
            grades_sem1.append(grade)
            unit = st.number_input(
                f"Unit for Course {i + 1} (First Semester):", min_value=1, key=f"sem1_unit_{i}"
            )
            units_sem1.append(unit)

if st.button("Calculate CGPA"):
    cgpa = sum(gpa_per_semester) / len(gpa_per_semester)
    st.success(f"Your CGPA is: {cgpa:.2f}")