class Student:
  def __init__(self, name,id,cgpa):
    self.name = name
    self.id = id
    self.cgpa = cgpa

  def myfunc(self):
    print("Student name is "  + self.name)
    print("Student id is "  +str(self.id))
    print("CGPA is " + str(self.cgpa))

p1 = Student("Al", 36, 3.02)
p2 = Student("Mohammad", 46, 3.20)
p3 = Student("Fahad", 38, 3.29)
p4 = Student("Faj", 42, 3.40)
p5 = Student("Farz", 62, 3.92)
p1.myfunc()
p2.myfunc()
p3.myfunc()
p4.myfunc()
p5.myfunc()

print("\n")
print("\n")

class Teacher:
  def __init__(self, name,employeeid,role):
    self.name = name
    self.employeeid = employeeid
    self.role = role

  def t_func(self):
    print("Teacher name is "  + self.name)
    print("Employee id is "  +str(self.employeeid))
    print("role is " + str(self.role))

t1 = Teacher("Ali", 3621, 'Instractor')
t2 = Teacher("Fahd", 5621, 'Instractor')
t3 = Teacher("Md", 3641, 'jr.Instractor')
t4 = Teacher("Akash", 5621, 'Instractor')
t5 = Teacher("Abir", 3221, 'jr.Instractor')

t1.t_func()
t2.t_func()
t3.t_func()
t4.t_func()
t5.t_func()
