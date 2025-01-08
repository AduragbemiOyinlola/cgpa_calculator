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

    def get_grades(self, grades, units):

        units.append(int(input('enter course unit: ')))
        grades.append(input('enter grade: ').upper())

        while True:
            response = input('\nAdd more? (y/n): ')
            if response == 'y':
                try: 
                    units.append(int(input('enter course unit: ')))
                    grades.append(input('enter grade: ').upper())
                except ValueError:
                    print('You have entered a wrong format, kindly exit and start again.')
            else:
                break

    def calculate_cgpa(self):
        for i in range(len(self.grades)):
            self.w_s += self.grade_points[self.grades[i]] * self.units[i]

        self.CGPA = self.w_s/sum(self.units)
        print('\nCGPA is:',self.CGPA)

cgpa = CGPA()
cgpa.get_year('Enter year: ')
cgpa.get_semester('Enter semester: ')
cgpa.get_grades(cgpa.grades, cgpa.units)
cgpa.calculate_cgpa()