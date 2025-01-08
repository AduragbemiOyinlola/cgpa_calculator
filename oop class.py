class CGPA:
    def __init__(self):
        self.grades = []
        self.units = []
        self.w_s = 0
        self.grade_points = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}

    def get_year(self, year):
        self.year = int(input(year))

    def get_semester(self, semester):
        self.semester = int(input(semester))

    