import uuid
""" A fuction named `student_info` that takes a list `students` that contains
 dictionnaries of type student
{
    id: 123897
    first_name: 'Maria',
    last_name: 'Denotte'
    courses: {('physic', 12), ('math', 18)}
}
inside that function I want :
  - a function that prints the firstname and lastname of each student
  - a function that returns the average for a given course
  - a function that returns the average for a given in all his courses
  - a function that returns that prints everything we know about a student
id2: 10984, first_name2: 'Maria',
last_name2 ='Denotte',
courses2: {('physic', 12), ('math', 18)} """


def func_student(ma_liste):

    def ope(operation):
        if operation == 'print':
            return imprimer
        if operation == 'average_all':
            return average_course
        if operation == 'student':
            return student_info
        if operation == 'average_student':
            return average_student

    def imprimer():
        for i in ma_liste:
            print('-'*15, 'student with id:', i['id'], '-'*15)
            print('first name:', i['first_name'])
            print(type(i))
            print(f"last name: {i.get('last_name')}")

    def average_course(param_cour):
        aver_p = 0
        for i in ma_liste:
            p_phy = i["courses"][param_cour]
            aver_p = aver_p + p_phy
        return aver_p/len(ma_liste)

    def student_info(first_name, last_name):
        counter = 0
        for i in ma_liste:
            if i['last_name'] == last_name and i['first_name'] == first_name:
                counter = 1
                return i
        if counter != 1:
            raise KeyError("L'élève n'a pas été retrouvé(e)")

    def average_student(first_name, last_name):
        for i in ma_liste:
            if i['last_name'] == last_name and i['first_name'] == first_name:
                avg = 0
                for v in i["courses"].values():
                    avg = avg + v
                return avg/len(i["courses"])

    return ope  # go out of the function and in def ope
                # close the first def func_student(ma_liste):



ma_liste = [{
    "id": uuid.uuid4(),
    'first_name': 'Maria',
    'last_name': 'Denotte',
    'courses': {
        "physic": 12, "math": 18}
}, {
    "id": uuid.uuid4(),
    'first_name': 'Robert',
    'last_name': 'Miche',
    'courses': {
        "physic": 10, "math": 10}
}]

manage_students = func_student(ma_liste)
print(manage_students('print')())
print(manage_students('average_all')('physic'))
print(manage_students('student')('Maria', 'Denotte'))
print(manage_students('average_student')('Maria', 'Denotte'))
