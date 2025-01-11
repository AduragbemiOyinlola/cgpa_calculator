import streamlit as st

# App Title and Description
st.title("CGPA Calculator")
st.write("This app calculates your CGPA based on the grades and units you input.")

# CGPA Calculation options
st.sidebar.title("How would you like to calculate your CGPA?")
options = ["From scratch", "From previous GPA"]
calculation_option = st.sidebar.radio("Select CGPA Calculation Option", options)

# Option 1: From Scratch
if calculation_option == "From scratch":
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

        # Column for first semesters
        with col1:
            st.subheader("First Semester")
            num_courses_sem1 = st.number_input(
                f"Number of Courses:", min_value=1, step=1, key=f"num_courses_sem1_{year_label}"
            )

            # Create columns for first semester grades and units
            col3, col4 = st.columns(2)

            # Column for first semester grade
            with col3:
                for i in range(int(num_courses_sem1)):
                    grade = st.selectbox(
                        f"Grade for Course {i + 1}:",
                        grade_options,
                        key=f"sem1_grade_{year_label}_{i}",
                    )
                    grades_sem1.append(grade)

            # Column for first semester unit
            with col4:
                for i in range(int(num_courses_sem1)):
                    unit = st.number_input(
                        f"Unit for Course {i + 1}:",
                        min_value=1,
                        key=f"sem1_unit_{year_label}_{i}",
                    )
                    units_sem1.append(unit)

            gpa_sem1 = calculate_gpa(grades_sem1, units_sem1)
            gpa_per_semester.append(gpa_sem1)

        # Column for second semesters
        with col2:
            st.subheader("Second Semester")
            num_courses_sem2 = st.number_input(
                f"Number of Courses:", min_value=1, step=1, key=f"num_courses_sem2_{year_label}"
            )

            # Create columns for second semester grades and units
            col5, col6 = st.columns(2)

            # Column for second semester grade
            with col5:
                for i in range(int(num_courses_sem2)):
                    grade = st.selectbox(
                        f"Grade for Course {i + 1}:",
                        grade_options,
                        key=f"sem2_grade_{year_label}_{i}",
                    )
                    grades_sem2.append(grade)

            # Column for second semester unit
            with col6:
                for i in range(int(num_courses_sem2)):
                    unit = st.number_input(
                        f"Unit for Course {i + 1}:",
                        min_value=1,
                        key=f"sem2_unit_{year_label}_{i}",
                    )
                    units_sem2.append(unit)

            gpa_sem2 = calculate_gpa(grades_sem2, units_sem2)
            gpa_per_semester.append(gpa_sem2)
            
    # Combination of Year and Semester
    if semester == 2:
        for i in range(1, year+1):
            with st.expander("Field to input data", expanded=True): 
                st.header(f"Year {i}")
                get_grades_units(f"Year {i}")

    elif semester == 1 and year > 1:
        for i in range(1, year):
            with st.expander("Field to input data", expanded=True): 
                st.header(f"Year {i}")
                get_grades_units(f"Year {i}")

        with st.expander("Field to input data", expanded=True): 
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
        with st.expander("Field to input data", expanded=True): 
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

    # Calculate CGPA
    if st.button("Calculate CGPA"):
        cgpa = sum(gpa_per_semester) / len(gpa_per_semester)
        st.success(f"Your CGPA is: {cgpa:.2f}")

# Option 2: From Previous GPA
else:
    previous_cgpa = st.number_input("What is your previous CGPA?", min_value=0.0, max_value=5.0)

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
        total_points = 0
        total_units = 0
        for grade, unit in zip(grades, units):
            points = grade_points[grade] * unit
            total_points += points
            total_units += unit

        gpa = total_points / total_units
        cgpa = (previous_cgpa + gpa) / 2
        st.success(f"Your CGPA is: {cgpa:.2f}")