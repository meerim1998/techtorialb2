exam1 = float(input("Enter your first exam score:"))
exam2 = float(input("Enter your second exam score:"))
exam3 = float(input("Enter your third exam score:"))
attendance = float(input("Enter your attendance in the class %"))

exam_1_pass = exam1 >= 20 
exam_2_pass = exam2 >= 30
exam_3_pass = exam3 >= 50
total_exam = exam_1_pass == exam_2_pass == exam_3_pass

exam_total_average = (exam1 + exam2 + exam3) // 3 
passing_exam = exam_total_average >= 65 
attendance_pass = attendance >= 80

total_pass = passing_exam == attendance_pass == total_exam

print("Result:",total_pass)