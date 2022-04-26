class Human:
    
    def __init__(self,name,surname,second_name,age):
        self.name=name
        self.surname=surname
        self.second_name=second_name
        self.age=age
    
    
class Student(Human):
    def __init__(self,name,surname,second_name,age,mark):
        super().__init__(name,surname,second_name,age)
        self.mark=mark
    def who_am_i():
        print("я ученик")
    def hello(self):
        print("привет, мне "+str(self.age)+" лет, меня зовут "+self.name+" "+self.surname+" "+self.second_name+",мой средний балл "+self.mark)
class Teacher(Human):
    def who_am_i():
        print("я учитель")
    def __init__(self,name,surname,second_name,age,subject):
        super().__init__(name,surname,second_name,age)
        self.subject=subject
    def hello(self):
        print("привет, мне "+str(self.age)+" лет, меня зовут "+self.name+" "+self.surname+" "+self.second_name+",я веду урок "+self.subject)
students=dict()
teachers=dict()
print("ученики")
for i in range(1,6):
    print('имя')
    name=input()
    print('фамилия')
    surname=input()
    print('отчесво')
    second_name=input()
    print('возраст')
    age=input()
    print('средний балл')
    mark=input()
    students[i]=Student(name,surname,second_name,age,mark)
print("учителя")
for i in range(1,4):
    print('имя')
    name=input()
    print('фамилия')
    surname=input()
    print('отчесво')
    second_name=input()
    print('возраст')
    age=input()
    print('урок')
    subject=input()
    teachers[i]=Teacher(name,surname,second_name,age,subject)
for i in range(1,4):
    students[i].hello()
for i in range(1,4):
    teachers[i].hello()