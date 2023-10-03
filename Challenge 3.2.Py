class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


Students = [
    Student("balamurugan", "A336", 9.8),
    Student("yuvraj", "A338", 7.0),
    Student("vishwa", "A337", 9.0),
    Student("annal", "A335", 10.0),
]

sorted_students = sort_students(Students)

for student in sorted_students:
  print("Name : {} ,Roll Number : {}, CGPA : {}".format(
      student.name, student.roll_number, student.cgpa))
