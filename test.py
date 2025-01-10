import streamlit as st

st.title("CGPA Calculator")
st.write("This app calculates your CGPA based on the grades and units you input.")

# Number of years
year = st.number_input("What year?", min_value=1, max_value=7, step=1)
semester = st.number_input("What semester?", min_value=1, max_value=2)

# Grade Options
grade_options = ["A", "B", "C", "D", "E", "F"]

def get_grades_units():
    # Input Grades and Units
    grades_sem1 = []
    units_sem1 = []
    grades_sem2 = []
    units_sem2 = []

    # Columns for First Semester and Second Semester
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

    with col2:
        st.subheader("Second Semester")
        num_courses_sem2 = st.number_input(
            "Number of Courses (Second Semester):", min_value=1, step=1, key="num_courses_sem2"
        )
        for i in range(int(num_courses_sem2)):
            grade = st.selectbox(
                f"Grade for Course {i + 1} (Second Semester):", grade_options, key=f"sem2_grade_{i}"
            )
            grades_sem2.append(grade)
            unit = st.number_input(
                f"Unit for Course {i + 1} (Second Semester):", min_value=1, key=f"sem2_unit_{i}"
            )
            units_sem2.append(unit)