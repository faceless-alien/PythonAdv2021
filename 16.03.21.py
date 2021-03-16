class Teacher():
    def __init__(self, name, surname, subject):
        self.name = name
        self.surname = surname
        self.subject = subject
class Student():
    def __init__(self,name,surname,subjects):
        self.name = name
        self.surname = surname
        self.subjects = subjects
class Subject():
    def __init__(self, name):
        self.name=name
teachers=[]
students=[]
subjects=[]
for i in range(int(input())):
    i=Subject(input())
    subjects.append(i)
print('Now teachers \n')
for i in range(int(input())):
    i=input().split()
    if len(i)>3:
        raise Exception('Один учитель может вести только один предмет')
    for j in range(len(subjects)):
        if subjects[j].name==i[2]:
            x=Teacher(i[0],i[1],subjects[j])
            teachers.append(x)
            break
    else:
        tmp=Subject(i[2])
        x=Teacher(i[0],i[1],tmp)
        subjects.append(tmp)
        teachers.append(x)
print('And students \n')
for i in range(int(input())):
    i=input().split()
    fl=0
    some_subjects=[]
    for j in range(len(subjects)):
        for x in i[2:]:
            if subjects[j]==x:
                fl+=1
                some_subjects.append(subjects[j])
    if fl==len(i[2:]):
        new_student=Student(i[0],i[1],some_subjects)
        students.append(new_student)
    else:
        raise Exception('Такого предмета нет')
for i in students: print(i.name, i.surname, i.subjects)
