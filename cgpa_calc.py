grades=[]
units=[]
w_s = 0

grade_points = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}
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
        
for i in range(len(grades)):
    w_s += grade_points[grades[i]] * units[i]

CGPA = w_s/sum(units)
print('\nCGPA is:',CGPA)